#!/usr/bin/env bash
mkdir logs
chmod 777 logs

python -m rasa_core.train \
  --online -o models/dialogue \
  -d models/dialogue/domain.yml -s stories \
  --endpoints config/endpoints.yaml

  read