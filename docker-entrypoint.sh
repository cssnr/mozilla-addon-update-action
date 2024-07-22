#!/usr/bin/env sh

set -e

echo "Starting: Mozilla Addon Update ${0} - $(pwd)"

echo "python /src/update.py"

python /src/update.py
