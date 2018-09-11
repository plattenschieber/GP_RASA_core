#!/usr/bin/env bash

python src/train_dialog.py && python src/start_core.py -E "config/endpoints.docker.yaml"

read

