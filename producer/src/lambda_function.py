import json
import logging
import datetime

logging.basicConfig(
    format="%(asctime)s %(name)/12s %(levelname)/8s %(message)s",
    datefmt= "%Y-%m-%d %H:%M:%S",
    level=logging.INFO
)
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

def lambda_handler(event,context):
    msg = "Data of interest sent to Kinesis at " + str(datetime.datetime.now())
    LOGGER.info(msg)
    return{
        "statusCode":200,
        "body": json.dumps(msg)
    }

