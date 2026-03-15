#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
OUTPUT_DIR="$AGENT_DIR/outputs"
STYLE_FILE="$AGENT_DIR/styles/mdcourse_preamble.tex"
LOG_FILE="$OUTPUT_DIR/generation.log"

mkdir -p "$OUTPUT_DIR"

log() {
  local msg="$1"
  printf '[%s] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$msg" | tee -a "$LOG_FILE"
}

usage() {
  cat <<USAGE
Usage:
  build_sale_ready_pdf.sh <input.md|input_directory> [output.pdf|output_directory]

Examples:
  build_sale_ready_pdf.sh agents/pdf-creator/inputs/RAND-001.md
  build_sale_ready_pdf.sh agents/pdf-creator/inputs/ agents/pdf-creator/outputs/
USAGE
}

if [[ $# -lt 1 ]]; then
  usage
  exit 1
fi

INPUT_PATH="$1"
OUTPUT_ARG="${2:-}"

if ! command -v pandoc >/dev/null 2>&1; then
  log "ERROR: pandoc is not installed or not in PATH."
  exit 2
fi

if ! command -v xelatex >/dev/null 2>&1; then
  log "ERROR: xelatex is not installed or not in PATH."
  exit 2
fi

if [[ ! -e "$INPUT_PATH" ]]; then
  log "ERROR: input path does not exist: $INPUT_PATH"
  exit 3
fi

TMP_DIR="$(mktemp -d)"
COMBINED_MD="$TMP_DIR/combined.md"
META_FILE="$TMP_DIR/meta.yml"

cleanup() {
  rm -rf "$TMP_DIR"
}
trap cleanup EXIT

rank_for_file() {
  local path="$1"
  local name
  name="$(basename "$path" | tr '[:upper:]' '[:lower:]')"

  if [[ "$name" =~ ^(readme|index|overview|blueprint).*\.md$ ]]; then
    echo "010"
    return
  fi

  if [[ "$name" =~ module[-_[:space:]]*([0-9]+) ]]; then
    printf "1%03d\n" "${BASH_REMATCH[1]}"
    return
  fi

  if [[ "$name" == *assessment* ]]; then
    echo "400"
    return
  fi

  if [[ "$name" == *multimedia* ]]; then
    echo "500"
    return
  fi

  if [[ "$name" == *marketing* ]]; then
    echo "600"
    return
  fi

  if [[ "$name" == *pricing* ]]; then
    echo "700"
    return
  fi

  if [[ "$name" == *delivery* ]]; then
    echo "800"
    return
  fi

  echo "900"
}

strip_front_matter() {
  awk '
    NR == 1 && $0 ~ /^---[[:space:]]*$/ { in_yaml = 1; next }
    in_yaml == 1 && $0 ~ /^---[[:space:]]*$/ { in_yaml = 0; next }
    in_yaml == 0 { print }
  ' "$1"
}

extract_front_matter() {
  awk '
    NR == 1 && $0 ~ /^---[[:space:]]*$/ { in_yaml = 1; next }
    in_yaml == 1 && $0 ~ /^---[[:space:]]*$/ { exit }
    in_yaml == 1 { print }
  ' "$1"
}

meta_value() {
  local key="$1"
  awk -F': *' -v k="$key" '$1 == k { $1=""; sub(/^: */, ""); print; exit }' "$META_FILE" \
    | sed -E 's/^"|"$//g' \
    | sed -E "s/^'|'$//g"
}

declare -a MARKDOWN_FILES

if [[ -d "$INPUT_PATH" ]]; then
  while IFS= read -r -d '' file; do
    MARKDOWN_FILES+=("$file")
  done < <(find "$INPUT_PATH" -type f -name '*.md' -print0)

  if [[ ${#MARKDOWN_FILES[@]} -eq 0 ]]; then
    log "ERROR: no markdown files found in directory: $INPUT_PATH"
    exit 4
  fi

  mapfile -t SORTED_LINES < <(
    for file in "${MARKDOWN_FILES[@]}"; do
      printf '%s|%s\n' "$(rank_for_file "$file")" "$file"
    done | sort -t'|' -k1,1 -k2,2
  )

  MARKDOWN_FILES=()
  for line in "${SORTED_LINES[@]}"; do
    MARKDOWN_FILES+=("${line#*|}")
  done
else
  MARKDOWN_FILES=("$INPUT_PATH")
fi

FIRST_FILE="${MARKDOWN_FILES[0]}"
extract_front_matter "$FIRST_FILE" > "$META_FILE"

DEFAULT_TITLE="$(basename "${INPUT_PATH%/}")"
DEFAULT_TITLE="${DEFAULT_TITLE%.md}"
TITLE="$(meta_value title)"
AUTHOR="$(meta_value author)"
DOC_DATE="$(meta_value created_at)"
COURSE_CODE="$(meta_value code)"
KEYWORDS="$(meta_value keywords)"

TITLE="${TITLE:-$DEFAULT_TITLE}"
AUTHOR="${AUTHOR:-mdcourse-gen-redesign}"
DOC_DATE="${DOC_DATE:-$(date +%Y-%m-%d)}"
COURSE_CODE="${COURSE_CODE:-N/A}"

cat > "$COMBINED_MD" <<EOF
---
title: "$TITLE"
author: "$AUTHOR"
date: "$DOC_DATE"
---

# $TITLE

**Course Code:** $COURSE_CODE  
**Author:** $AUTHOR  
**Date:** $DOC_DATE

\newpage

EOF

for file in "${MARKDOWN_FILES[@]}"; do
  log "Including source markdown: $file"
  strip_front_matter "$file" >> "$COMBINED_MD"
  printf '\n\n\\newpage\n\n' >> "$COMBINED_MD"
done

if [[ -n "$OUTPUT_ARG" ]]; then
  if [[ -d "$OUTPUT_ARG" ]]; then
    OUTPUT_PDF="$OUTPUT_ARG/${DEFAULT_TITLE}.pdf"
  else
    OUTPUT_PDF="$OUTPUT_ARG"
  fi
else
  OUTPUT_PDF="$OUTPUT_DIR/${DEFAULT_TITLE}.pdf"
fi

mkdir -p "$(dirname "$OUTPUT_PDF")"

log "Rendering PDF with Pandoc"
PANDOC_CMD=(
  pandoc "$COMBINED_MD"
  -o "$OUTPUT_PDF"
  --from markdown+yaml_metadata_block+raw_html
  --pdf-engine=xelatex
  --toc
  --toc-depth=3
  --number-sections
  -H "$STYLE_FILE"
  --metadata title="$TITLE"
  --metadata author="$AUTHOR"
  --metadata date="$DOC_DATE"
)

if [[ -n "$KEYWORDS" ]]; then
  PANDOC_CMD+=(--metadata "keywords=$KEYWORDS")
fi

"${PANDOC_CMD[@]}" >> "$LOG_FILE" 2>&1

if [[ ! -s "$OUTPUT_PDF" ]]; then
  log "ERROR: PDF generation failed or produced empty file: $OUTPUT_PDF"
  exit 5
fi

log "SUCCESS: Generated sale-ready PDF: $OUTPUT_PDF"
log "Metadata: title='$TITLE', author='$AUTHOR', date='$DOC_DATE'"

echo "$OUTPUT_PDF"
