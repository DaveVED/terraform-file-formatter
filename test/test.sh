#!/bin/bash
set -e

# Easy files.
./tf/main.py sort -file test/files/input-files/easy1.tf --debug
./tf/main.py sort -file test/files/input-files/easy2.tf --debug
./tf/main.py sort -file test/files/input-files/easy3.tf --debug

# Medium files.
./tf/main.py sort -file test/files/input-files/medium1.tf --debug
./tf/main.py sort -file test/files/input-files/medium2.tf --debug
#cmp --silent test/input-files/easy1.tf test/correct-output-files/easy1.tf || echo "files are different"
