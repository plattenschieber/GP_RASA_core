#!/usr/bin/env bash
mkdir logs
chmod 777 logs

python src/train_dialog.py && python src/start_core.py -E "config/endpoints.docker.yaml"

read

