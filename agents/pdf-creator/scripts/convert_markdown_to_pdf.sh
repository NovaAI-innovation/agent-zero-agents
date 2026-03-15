#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Backward-compatible wrapper.
"$SCRIPT_DIR/build_sale_ready_pdf.sh" "$@"
