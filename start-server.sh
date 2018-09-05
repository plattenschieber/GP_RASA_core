#!/usr/bin/env bash
python train_dialog.py && python -m rasa_core.run -d models/dialogue --enable_api --debug --endpoints endpoints.yaml -o out.log