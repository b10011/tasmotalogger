#!/bin/bash

TASMOTA_DB_PORT=${TASMOTA_DB_PORT:-27017}
TASMOTA_DB_AUTHENTICATIONDATABASE=${TASMOTA_DB_AUTHENTICATIONDATABASE:-admin}
if [[ -z ${TASMOTA_DB_USERNAME} ]]; then exit 1; fi
if [[ -z ${TASMOTA_DB_PASSWORD} ]]; then exit 1; fi
if [[ -z ${TASMOTA_DB_HOST} ]]; then exit 1; fi
if [[ -z ${TASMOTA_DB_DATABASE} ]]; then exit 1; fi
if [[ -z ${TASMOTA_DEVICES} ]]; then exit 1; fi

/usr/local/bin/python3 /app/main.py |& tee -a /tmp/dockerlog.txt
