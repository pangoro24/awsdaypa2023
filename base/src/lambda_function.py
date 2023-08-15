import json
import logging
import datetime
import base64
import gzip

logging.basicConfig(
    format="%(asctime)s %(name)/12s %(levelname)/8s %(message)s",
    datefmt= "%Y-%m-%d %H:%M:%S",
    level=logging.INFO
)
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

def lambda_handler(event,context):
    output_records = []
    LOGGER.info(event)
    for r in event["records"]:
        payload = gzip.decompress(base64.b64decode(r["data"]))
        raw_log = json.loads(payload.decode("utf-8"))
        LOGGER.info(raw_log)
        LOGGER.info("Log group:".format(raw_log["logGroup"]))
        data_tranf = {
            "logstream":raw_log["logGroup"],
            "msg":raw_log["logEvents"][0]["message"]
        }
        r_tranf ={
            "recordId": r["recordId"],
            "result": "Ok",
            "data": base64.b64encode(json.dumps(data_tranf).encode("utf-8")).decode("utf-8")
        }
        output_records.append(r_tranf)
        response = {
            "records": output_records
        }
    return response
