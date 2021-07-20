# TasmotaLogger

A somewhat configurable Tasmota logger container.

## Installation

```bash
docker build -t tasmotalogger .
```

## Configuration

| Variable                          | Default        | Description.                                                                                                                                      |
| --------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| TZ                                |                | Timezone, e.g. Europe/Helsinki.                                                                                                                   |
| TASMOTA_DEVICES                   |                | Tasmota devices, IP addresses separated by a space. Addresses can be domains and can have nicknames. E. g. 'office:192.168.1.10 home:example.com' |
| TASMOTA_DB_USERNAME               |                | MongoDB username.                                                                                                                                 |
| TASMOTA_DB_PASSWORD               |                | MongoDB password.                                                                                                                                 |
| TASMOTA_DB_HOST                   |                | MongoDB host.                                                                                                                                     |
| TASMOTA_DB_PORT                   | 27017          | MongoDB port.                                                                                                                                     |
| TASMOTA_DB_DATABASE               |                | MongoDB database.                                                                                                                                 |
| TASMOTA_DB_AUTHENTICATIONDATABASE | admin          | Database against which authentication is checked. Mongodump's 'authenticationDatabase' argument.                                                  |
| TASMOTA_CRONRULE                  | 0 \* \* \* \*  | Crontab rule defining interval of backing up.                                                                                                     |
| TASMOTA_DEBUG_LOG                 | /tmp/debug.log | Path to debug log.                                                                                                                                |
