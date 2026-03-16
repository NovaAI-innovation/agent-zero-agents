# Voiceover Agent

- **Pipeline position**: #3/5 - **script-writer JSON → TTS voiceover → image-gen visuals**
- **Specialization**: Natural TTS with emotion, pacing, emphasis control
- **Input**: script-writer JSON (`full_script`, `structure`, timing metadata)
- **Engines**: elevenlabs, espeak, piper, coqui (code_execution_tool)
- **Output**: MP3/WAV files → `/a0/tmp/audio/video-prod/` (22kHz, optimized)

**Call with**: `call_subordinate profile="voice-ai" message="Convert this script JSON to voiceover with enthusiastic tech delivery"`

**Integration**: Feeds video-editor agent - perfect script/voice/visual sync
