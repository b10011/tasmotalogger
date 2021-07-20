#!/bin/bash

TASMOTA_CRONRULE=${TASMOTA_CRONRULE:-0 * * * *}

printenv >> /etc/environment

echo "${TASMOTA_CRONRULE} /app/execute" > /etc/cron.d/tasmota_execute
crontab /etc/cron.d/tasmota_execute

cron -f
