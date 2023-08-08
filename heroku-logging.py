import logging
from pythonjsonlogger import jsonlogger
from datetime import datetime
import time


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get("timestamp"):
            now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            log_record["timestamp"] = now
        if log_record.get("level"):
            log_record["level"] = log_record["level"].upper()
        else:
            log_record["level"] = record.levelname


logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

logHandler = logging.StreamHandler()
formatter = CustomJsonFormatter("%(timestamp)s %(level)s %(name)s %(message)s")
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

while True:
    logger.info("Short message about user.", extra={"username": "testuser"})
    time.sleep(1)
    logger.info("A1" * 250 + "B1" * 500 + "C1" * 500 + "D1" * 500 + "E1" * 500 + "F1" * 500 + "G1" * 500 + "H1" * 500 + "I1" * 500 + "J1" * 500 + "K1" * 500 + "L1" * 500 + "M1" * 500 + "N1" * 500 + "O1" * 500 + "P1" * 500 + "Q1" * 500 + "R1" * 500 + "S1" * 500 + "T1" * 500 + "U1" * 500 + "V1" * 500 + "W1" * 500 + "X1" * 500 + "Y1" * 500 + "Z1" * 500)
    logger.info("A2" * 250 + "B2" * 500 + "C2" * 500 + "D2" * 500 + "E2" * 500 + "F2" * 500 + "G2" * 500 + "H2" * 500 + "I2" * 500 + "J2" * 500 + "K2" * 500 + "L2" * 500 + "M2" * 500 + "N2" * 500 + "O2" * 500 + "P2" * 500 + "Q2" * 500 + "R2" * 500 + "S2" * 500 + "T2" * 500 + "U2" * 500 + "V2" * 500 + "W2" * 500 + "X2" * 500 + "Y2" * 500 + "Z2" * 500)
    logger.info("A3" * 250 + "B3" * 500 + "C3" * 500 + "D3" * 500 + "E3" * 500 + "F3" * 500 + "G3" * 500 + "H3" * 500 + "I3" * 500 + "J3" * 500 + "K3" * 500 + "L3" * 500 + "M3" * 500 + "N3" * 500 + "O3" * 500 + "P3" * 500 + "Q3" * 500 + "R3" * 500 + "S3" * 500 + "T3" * 500 + "U3" * 500 + "V3" * 500 + "W3" * 500 + "X3" * 500 + "Y3" * 500 + "Z3" * 500)
    time.sleep(1)

