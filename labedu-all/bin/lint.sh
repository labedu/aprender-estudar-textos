#!/usr/bin/env bash
set -euo pipefail
#|
#| Analyzes source code to flag programming errors, bugs, stylistic errors, and suspicious constructs.
#|

#| Code style with flake8
echo "running flake8"
flake8 --count --max-line-length=119 --show-source --statistics --doctests clusters/ tests/

#| Typing check with mypy
echo "running mypy"
mypy --ignore-missing-imports formatacao