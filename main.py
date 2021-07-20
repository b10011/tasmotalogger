import click
import os
import requests
import time
from loguru import logger

import mongoengine as db
from mongoengine_arrow import ArrowDateTimeField


class LogItem(db.Document):
    timestamp = ArrowDateTimeField(required=True)
    name = db.StringField(max_length=1024, required=True)
    host = db.StringField(max_length=1024, required=True)
    total = db.FloatField(required=True)


def fetch_usage_data(name_hosts):
    result = []

    for name, host in name_hosts:
        try:
            data = requests.get(
                "http://{host}/cm?cmnd=Status%208".format(host=host)
            ).json()
            timestamp = time.time()
            total = data["StatusSNS"]["ENERGY"]["Total"]
            result.append((timestamp, name, host, total))
        except Exception:
            print('Couldn\'t connect to "{}" (IP {})'.format(name, host))
            timestamp = time.time()
            result.append((timestamp, name, host, "CONNECTION FAILURE"))

    return result


@click.command()
@click.argument("devices", nargs=-1)
@click.option("--database-host", envvar="TASMOTA_DB_HOST")
@click.option("--database-port", envvar="TASMOTA_DB_PORT", default=27017)
@click.option("--database-username", envvar="TASMOTA_DB_USERNAME")
@click.option("--database-password", envvar="TASMOTA_DB_PASSWORD")
@click.option("--database-database", envvar="TASMOTA_DB_DATABASE")
@click.option(
    "--database-authentication-source",
    envvar="TASMOTA_DB_AUTHENTICATIONDATABASE",
    default="admin",
)
@click.option(
    "--debug-log", envvar="TASMOTA_DEBUG_LOG", default="/tmp/debug.log"
)
def main(
    devices,
    database_host,
    database_port,
    database_username,
    database_password,
    database_database,
    database_authentication_source,
    debug_log,
):
    logger.add(debug_log)

    logger.info("Connecting to database")

    try:
        db.connect(
            host=database_host,
            port=database_port,
            username=database_username,
            password=database_password,
            db=database_database,
            authentication_source=database_authentication_source,
        )

        if len(devices) == 0:
            devices = os.environ["TASMOTA_DEVICES"].split()

        if len(devices) == 0:
            logger.warning("No devices defined")
            return

        name_hosts = []
        for device in devices:
            try:
                name, host = device.split(":")
            except Exception:
                name = device
                host = device

            name_hosts.append((name, host))

        results = fetch_usage_data(name_hosts)

        for timestamp, name, host, total in results:
            logitem = LogItem(
                timestamp=timestamp, name=name, host=host, total=total
            )
            logitem.save()

    except Exception as e:
        logger.exception("Failed to fetch or insert statistics", e)


if __name__ == "__main__":
    main()
