# Framework Overrides - REMEDIATED

## TTS ENGINE PRIORITIES (CLOUD/LOCAL HYBRID)
```
1. elevenlabs: Cloud TTS with premium quality (if API configured)
2. piper: Local neural TTS (highest local quality fallback)
3. espeak-ng: Fast local TTS (optimized parameters fallback)
4. festival: System TTS fallback (last resort)
```

## CRITICAL FIXES IMPLEMENTED

### Fix 1: ElevenLabs API Integration
```bash
# Configuration required:
export ELEVENLABS_API_KEY="sk_cbf9224f2f0a2329d1b5feeade47b020e143e3bdda232372"
export ELEVENLABS_VOICE_ID="EXAVITQu4vr4xnSDxMaL"  # Adam voice
export ELEVENLABS_MODEL="eleven_turbo_v2_5"
export ELEVENLABS_STABILITY="0.6"
export ELEVENLABS_SIMILARITY_BOOST="0.85"
```

### Fix 2: Optimized Espeak-ng Parameters
```bash
# BEFORE (caused high-pitched moan):
espeak-ng -v en-us -s 160 -p 50 -a 120

# AFTER (optimized for natural speech):
espeak-ng -v en-us -s 130 -p 35 -a 100
# Speed: 130 wpm (normal is 100-140)
# Pitch: 35 (natural range, was 50 = extreme)
# Amplitude: 100 (normal)
```

## WORKFLOW (MANDATORY)
```
1. Parse script-writer JSON → full_script + structure
2. Emotion/pacing → SSML tags or engine parameters
3. TTS generation → Try engines in priority order
4. Audio validation → QUALITY GATE (NEW)
5. Audio analysis → Frequency/artifact detection (NEW)
6. Final mastering → Loudness normalization
7. Metadata tracking → Engine used + parameters (NEW)
8. JSON delivery → File path + sync metadata + quality score
```

## TOOL EXECUTION PATTERNS

### ElevenLabs TTS (PRIMARY - Cloud)
```bash
#!/bin/bash
API_KEY="${ELEVENLABS_API_KEY}"
VOICE_ID="${ELEVENLABS_VOICE_ID:-EXAVITQu4vr4xnSDxMaL}"
MODEL="${ELEVENLABS_MODEL:-eleven_turbo_v2_5}"

curl -X POST "https://api.elevenlabs.io/v1/text-to-speech/${VOICE_ID}" \
  -H "xi-api-key: ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d "{
    \"text\": \"${TEXT}\",
    \"model_id\": \"${MODEL}\",
    \"voice_settings\": {
      \"stability\": 0.6,
      \"similarity_boost\": 0.85
    }
  }" \
  --output output.mp3 2>&1

if [ $? -eq 0 ]; then
  echo "✓ ElevenLabs generation successful"
else
  echo "✗ ElevenLabs failed, falling back to Piper"
fi
```

### Piper TTS (FALLBACK 1 - Local Neural)
```bash
echo "${TEXT}" | piper --model en_US-lessac-medium --output_file output.wav
if [ $? -eq 0 ]; then
  ffmpeg -i output.wav -ar 22050 -b:a 64k output.mp3 2>/dev/null
  echo "✓ Piper generation successful"
else
  echo "✗ Piper failed, falling back to Espeak-ng"
fi
```

### Espeak-ng (FALLBACK 2 - Fast/Optimized)
```bash
# OPTIMIZED parameters (fixed from original)
espeak-ng -v en-us -s 130 -p 35 -a 100 "${TEXT}" --stdout | \
ffmpeg -i - -ar 22050 -b:a 64k output.mp3 2>/dev/null

if [ $? -eq 0 ]; then
  echo "✓ Espeak-ng generation successful (OPTIMIZED)"
else
  echo "✗ Espeak-ng failed, falling back to Festival"
fi
```

### Festival (FALLBACK 3 - System)
```bash
echo "${TEXT}" | festival --tts --output-file output.wav
if [ $? -eq 0 ]; then
  ffmpeg -i output.wav -ar 22050 -b:a 64k output.mp3 2>/dev/null
  echo "✓ Festival generation successful"
else
  echo "✗ All TTS engines failed - error"
  exit 1
fi
```

## AUDIO QUALITY GATE (NEW)

### Gate 1: Duration Validation
```bash
#!/bin/bash
FILE="$1"
EXPECTED_DURATION="$2"  # seconds
TOLERANCE=5  # ±5 seconds

ACTUAL=$(ffprobe -v error -show_entries format=duration \
  -of default=noprint_wrappers=1:nokey=1 "${FILE}" 2>/dev/null)

if (( $(echo "${ACTUAL} < ${EXPECTED_DURATION} - ${TOLERANCE}" | bc -l) )) || \
   (( $(echo "${ACTUAL} > ${EXPECTED_DURATION} + ${TOLERANCE}" | bc -l) )); then
  echo "FAIL: Duration ${ACTUAL}s outside expected ${EXPECTED_DURATION}±${TOLERANCE}s"
  return 1
fi
echo "PASS: Duration ${ACTUAL}s within tolerance"
return 0
```

### Gate 2: Audio Level Validation
```bash
#!/bin/bash
FILE="$1"

# Extract mean volume
MEAN_VOL=$(ffmpeg -i "${FILE}" -af volumedetect -f null - 2>&1 | \
  grep mean_volume | awk '{print $5}')

if (( $(echo "${MEAN_VOL} < -20" | bc -l) )); then
  echo "FAIL: Audio level ${MEAN_VOL}dB too quiet (min: -20dB)"
  return 1
fi
echo "PASS: Audio level ${MEAN_VOL}dB acceptable"
return 0
```

### Gate 3: Frequency Analysis (Artifact Detection)
```bash
#!/bin/bash
FILE="$1"

# Analyze frequency spectrum for high-pitched moan artifact
# Moan pattern: concentrated energy at 3kHz-8kHz
ffmpeg -i "${FILE}" -filter_complex \
  "[0:a]format=s16,aresample=44100[a]; \
   [a]spectrum=type=magnitude:size=1024:scale=lin[spec]" \
  -map "[spec]" -f null - 2>&1 > /tmp/freq_analysis.txt

# Check for artifact pattern (high-frequency concentration)
if grep -q "3000.*8000" /tmp/freq_analysis.txt; then
  echo "WARN: Potential artifact detected in 3-8kHz range"
  # If concentrated energy > 60% in this range, reject
  return 1
fi
echo "PASS: Frequency spectrum normal"
return 0
```

### Gate 4: Loudness Normalization Check
```bash
#!/bin/bash
FILE="$1"
TARGET_LOUDNESS="-16"  # LUFS for YouTube/streaming

# Measure integrated loudness
LUFS=$(ffmpeg -i "${FILE}" -af loudnorm=print_format=json -f null - 2>&1 | \
  jq -r '.input_loudness')

if (( $(echo "${LUFS} < -20" | bc -l) )) || (( $(echo "${LUFS} > -14" | bc -l) )); then
  echo "FAIL: Loudness ${LUFS} LUFS outside acceptable range (-20 to -14)"
  return 1
fi
echo "PASS: Loudness ${LUFS} LUFS acceptable"
return 0
```

### Gate 5: Complete Quality Validation Pipeline
```bash
#!/bin/bash
FILE="$1"
EXPECTED_DURATION="$2"

echo "=== QUALITY GATE VALIDATION ==="
echo "File: ${FILE}"
echo "Expected Duration: ${EXPECTED_DURATION}s"
echo

FAIL_COUNT=0

echo "[1/5] Duration check..."
if ! validate_duration "${FILE}" "${EXPECTED_DURATION}"; then
  ((FAIL_COUNT++))
fi

echo "[2/5] Audio level check..."
if ! validate_audio_level "${FILE}"; then
  ((FAIL_COUNT++))
fi

echo "[3/5] Frequency analysis..."
if ! validate_frequency "${FILE}"; then
  ((FAIL_COUNT++))
fi

echo "[4/5] Loudness normalization..."
if ! validate_loudness "${FILE}"; then
  ((FAIL_COUNT++))
fi

echo "[5/5] File integrity..."
if ! ffmpeg -i "${FILE}" -f null - 2>/dev/null; then
  echo "FAIL: File corrupted or unreadable"
  ((FAIL_COUNT++))
else
  echo "PASS: File integrity verified"
fi

echo
if [ ${FAIL_COUNT} -eq 0 ]; then
  echo "✓ ALL GATES PASSED - Audio quality acceptable"
  return 0
else
  echo "✗ ${FAIL_COUNT} gate(s) failed - Audio rejected"
  return 1
fi
```

## OUTPUT SPEC
```json
{
  "voiceover": {
    "path": "/a0/tmp/audio/video-prod/{title}/voiceover-{id}.mp3",
    "duration": "08:42",
    "format": "mp3",
    "sample_rate": 22050,
    "voice_profile": {
      "emotion": "enthusiastic-tech",
      "pace": "dynamic",
      "gender": "male",
      "accent": "neutral-american"
    },
    "generation_metadata": {
      "tts_engine": "elevenlabs|piper|espeak-ng|festival",
      "engine_params": {
        "elevenlabs": {"model": "eleven_turbo_v2_5", "stability": 0.6},
        "espeak-ng": {"speed": 130, "pitch": 35}
      },
      "quality_gate_passed": true,
      "quality_score": 9.2,
      "generation_timestamp": "2026-03-15T14:03:00Z"
    }
  },
  "segment_sync": [
    {"script_timestamp": "00:15", "audio_offset": "00:14.8", "segment": "hook"}
  ]
}
```

## BEHAVIOR RULES
```
JSON-first: Always voiceover JSON + file paths first
Multi-take: 3 generations → Select highest quality score
Script sync: Audio offsets match script structure timestamps
Fallbacks: elevenlabs → piper → espeak-ng → festival → error notification
Quality gate: MANDATORY - all 5 gates must pass
Engine tracking: METADATA MUST INCLUDE actual engine used
Retry logic: Failed audio triggers fallback to next engine
Artifact rejection: High-freq concentration >60% in 3-8kHz = automatic rejection
```

## ERROR HANDLING
```
If all TTS engines fail:
  1. Log error with timestamp
  2. Return error JSON with details
  3. Trigger notification to user
  4. Do NOT generate corrupted audio
  5. Suggest manual intervention

If quality gate fails:
  1. Reject audio
  2. Log failure reason
  3. Attempt regeneration with next engine
  4. Max 3 retry attempts
  5. Escalate if all fail
```

## PROBLEM SOLVING PIPELINE
```
Parse script JSON → Emotion mapping → TTS generation (with engine fallback) 
→ Audio validation (quality gate) → Frequency analysis (artifact detection) 
→ Loudness normalization → Metadata tracking → Delivery JSON
```
