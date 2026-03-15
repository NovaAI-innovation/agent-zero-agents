#!/bin/bash
set -e
INPUT="$1"
OUTPUT="$2"
TITLE="${3:-Document}"
AUTHOR="${4:-Author}"
DATE="${5:-$(date +%Y-%m-%d)}"
PREAMBLE_OPT=""
if [ -f /a0/agents/pdf-creator/outputs/styles/default_preamble.tex ]; then
  PREAMBLE_OPT="-H /a0/agents/pdf-creator/outputs/styles/default_preamble.tex"
elif [ -f /a0/usr/workdir/default_preamble.tex ]; then
  PREAMBLE_OPT="-H /a0/usr/workdir/default_preamble.tex"
fi
pandoc "$INPUT" -o "$OUTPUT" $PREAMBLE_OPT --pdf-engine=xelatex --metadata title="$TITLE" --metadata author="$AUTHOR" --metadata date="$DATE" --toc
