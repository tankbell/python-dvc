#!/usr/bin/env bash
set -euo pipefail

notebook_py="$1"

notebook_name=$(basename -- "$notebook_py")
notebook_name="${notebook_name%.*}"

notebook_out="reports/notebooks/$notebook_name.ipynb"

jupytext --to notebook --output - "$notebook_py" |
    papermill - "$notebook_out" --cwd "notebooks"
