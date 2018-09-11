#!/usr/bin/env bash
mkdir logs
chmod 777 logs

python src/train_dialog.py && python -m rasa_core.run -d models/dialogue --enable_api --endpoints config/endpoints.yaml -o ./logs/out.log

read