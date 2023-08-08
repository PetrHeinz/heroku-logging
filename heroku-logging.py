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
    logger.info("A1" * 2500 + "B1" * 5000 + "C1" * 5000 + "D1" * 5000 + "E1" * 5000 + "F1" * 5000 + "G1" * 5000 + "H1" * 5000 + "I1" * 5000 + "J1" * 5000 + "K1" * 5000 + "L1" * 5000 + "M1" * 5000 + "N1" * 5000 + "O1" * 5000 + "P1" * 5000 + "Q1" * 5000 + "R1" * 5000 + "S1" * 5000 + "T1" * 5000 + "U1" * 5000 + "V1" * 5000 + "W1" * 5000 + "X1" * 5000 + "Y1" * 5000 + "Z1" * 5000)
    logger.info("A2" * 2500 + "B2" * 5000 + "C2" * 5000 + "D2" * 5000 + "E2" * 5000 + "F2" * 5000 + "G2" * 5000 + "H2" * 5000 + "I2" * 5000 + "J2" * 5000 + "K2" * 5000 + "L2" * 5000 + "M2" * 5000 + "N2" * 5000 + "O2" * 5000 + "P2" * 5000 + "Q2" * 5000 + "R2" * 5000 + "S2" * 5000 + "T2" * 5000 + "U2" * 5000 + "V2" * 5000 + "W2" * 5000 + "X2" * 5000 + "Y2" * 5000 + "Z2" * 5000)
    logger.info("A3" * 2500 + "B3" * 5000 + "C3" * 5000 + "D3" * 5000 + "E3" * 5000 + "F3" * 5000 + "G3" * 5000 + "H3" * 5000 + "I3" * 5000 + "J3" * 5000 + "K3" * 5000 + "L3" * 5000 + "M3" * 5000 + "N3" * 5000 + "O3" * 5000 + "P3" * 5000 + "Q3" * 5000 + "R3" * 5000 + "S3" * 5000 + "T3" * 5000 + "U3" * 5000 + "V3" * 5000 + "W3" * 5000 + "X3" * 5000 + "Y3" * 5000 + "Z3" * 5000)
    time.sleep(1)

