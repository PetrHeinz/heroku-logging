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
    logger.info("A1   " * 1000 + "B1   "  * 2000 + "C1   "  * 2000 + "D1   "  * 2000 + "E1   "  * 2000 + "F1   "  * 2000 + "G1   "  * 2000 + "H1   "  * 2000 + "I1   "  * 2000 + "J1   "  * 2000 + "K1   "  * 2000 + "L1   "  * 2000 + "M1   "  * 2000 + "N1   "  * 2000 + "O1   "  * 2000 + "P1   "  * 2000 + "Q1   "  * 2000 + "R1   "  * 2000 + "S1   "  * 2000 + "T1   "  * 2000 + "U1   "  * 2000 + "V1   "  * 2000 + "W1   "  * 2000 + "X1   "  * 2000 + "Y1   "  * 2000 + "Z1   "  * 2000)
    logger.info("A2   " * 1000 + "B2   "  * 2000 + "C2   "  * 2000 + "D2   "  * 2000 + "E2   "  * 2000 + "F2   "  * 2000 + "G2   "  * 2000 + "H2   "  * 2000 + "I2   "  * 2000 + "J2   "  * 2000 + "K2   "  * 2000 + "L2   "  * 2000 + "M2   "  * 2000 + "N2   "  * 2000 + "O2   "  * 2000 + "P2   "  * 2000 + "Q2   "  * 2000 + "R2   "  * 2000 + "S2   "  * 2000 + "T2   "  * 2000 + "U2   "  * 2000 + "V2   "  * 2000 + "W2   "  * 2000 + "X2   "  * 2000 + "Y2   "  * 2000 + "Z2   "  * 2000)
    logger.info("A3   " * 1000 + "B3   "  * 2000 + "C3   "  * 2000 + "D3   "  * 2000 + "E3   "  * 2000 + "F3   "  * 2000 + "G3   "  * 2000 + "H3   "  * 2000 + "I3   "  * 2000 + "J3   "  * 2000 + "K3   "  * 2000 + "L3   "  * 2000 + "M3   "  * 2000 + "N3   "  * 2000 + "O3   "  * 2000 + "P3   "  * 2000 + "Q3   "  * 2000 + "R3   "  * 2000 + "S3   "  * 2000 + "T3   "  * 2000 + "U3   "  * 2000 + "V3   "  * 2000 + "W3   "  * 2000 + "X3   "  * 2000 + "Y3   "  * 2000 + "Z3   "  * 2000)
    logger.info("A4   " * 1000 + "B4   "  * 2000 + "C4   "  * 2000 + "D4   "  * 2000 + "E4   "  * 2000 + "F4   "  * 2000 + "G4   "  * 2000 + "H4   "  * 2000 + "I4   "  * 2000 + "J4   "  * 2000 + "K4   "  * 2000 + "L4   "  * 2000 + "M4   "  * 2000 + "N4   "  * 2000 + "O4   "  * 2000 + "P4   "  * 2000 + "Q4   "  * 2000 + "R4   "  * 2000 + "S4   "  * 2000 + "T4   "  * 2000 + "U4   "  * 2000 + "V4   "  * 2000 + "W4   "  * 2000 + "X4   "  * 2000 + "Y4   "  * 2000 + "Z4   "  * 2000)
    logger.info("A5   " * 1000 + "B5   "  * 2000 + "C5   "  * 2000 + "D5   "  * 2000 + "E5   "  * 2000 + "F5   "  * 2000 + "G5   "  * 2000 + "H5   "  * 2000 + "I5   "  * 2000 + "J5   "  * 2000 + "K5   "  * 2000 + "L5   "  * 2000 + "M5   "  * 2000 + "N5   "  * 2000 + "O5   "  * 2000 + "P5   "  * 2000 + "Q5   "  * 2000 + "R5   "  * 2000 + "S5   "  * 2000 + "T5   "  * 2000 + "U5   "  * 2000 + "V5   "  * 2000 + "W5   "  * 2000 + "X5   "  * 2000 + "Y5   "  * 2000 + "Z5   "  * 2000)
    logger.info("A6   " * 1000 + "B6   "  * 2000 + "C6   "  * 2000 + "D6   "  * 2000 + "E6   "  * 2000 + "F6   "  * 2000 + "G6   "  * 2000 + "H6   "  * 2000 + "I6   "  * 2000 + "J6   "  * 2000 + "K6   "  * 2000 + "L6   "  * 2000 + "M6   "  * 2000 + "N6   "  * 2000 + "O6   "  * 2000 + "P6   "  * 2000 + "Q6   "  * 2000 + "R6   "  * 2000 + "S6   "  * 2000 + "T6   "  * 2000 + "U6   "  * 2000 + "V6   "  * 2000 + "W6   "  * 2000 + "X6   "  * 2000 + "Y6   "  * 2000 + "Z6   "  * 2000)
    logger.info("A7   " * 1000 + "B7   "  * 2000 + "C7   "  * 2000 + "D7   "  * 2000 + "E7   "  * 2000 + "F7   "  * 2000 + "G7   "  * 2000 + "H7   "  * 2000 + "I7   "  * 2000 + "J7   "  * 2000 + "K7   "  * 2000 + "L7   "  * 2000 + "M7   "  * 2000 + "N7   "  * 2000 + "O7   "  * 2000 + "P7   "  * 2000 + "Q7   "  * 2000 + "R7   "  * 2000 + "S7   "  * 2000 + "T7   "  * 2000 + "U7   "  * 2000 + "V7   "  * 2000 + "W7   "  * 2000 + "X7   "  * 2000 + "Y7   "  * 2000 + "Z7   "  * 2000)
    logger.info("A8   " * 1000 + "B8   "  * 2000 + "C8   "  * 2000 + "D8   "  * 2000 + "E8   "  * 2000 + "F8   "  * 2000 + "G8   "  * 2000 + "H8   "  * 2000 + "I8   "  * 2000 + "J8   "  * 2000 + "K8   "  * 2000 + "L8   "  * 2000 + "M8   "  * 2000 + "N8   "  * 2000 + "O8   "  * 2000 + "P8   "  * 2000 + "Q8   "  * 2000 + "R8   "  * 2000 + "S8   "  * 2000 + "T8   "  * 2000 + "U8   "  * 2000 + "V8   "  * 2000 + "W8   "  * 2000 + "X8   "  * 2000 + "Y8   "  * 2000 + "Z8   "  * 2000)
    logger.info("A9   " * 1000 + "B9   "  * 2000 + "C9   "  * 2000 + "D9   "  * 2000 + "E9   "  * 2000 + "F9   "  * 2000 + "G9   "  * 2000 + "H9   "  * 2000 + "I9   "  * 2000 + "J9   "  * 2000 + "K9   "  * 2000 + "L9   "  * 2000 + "M9   "  * 2000 + "N9   "  * 2000 + "O9   "  * 2000 + "P9   "  * 2000 + "Q9   "  * 2000 + "R9   "  * 2000 + "S9   "  * 2000 + "T9   "  * 2000 + "U9   "  * 2000 + "V9   "  * 2000 + "W9   "  * 2000 + "X9   "  * 2000 + "Y9   "  * 2000 + "Z9   "  * 2000)
    time.sleep(1)
    logger.info("JSON message {\"test\":\"value\"}")
    logger.info("JSON message {\"test\":\"value\",\"more words test\":\"more words value\"}")
    logger.info("JSON message {\"test\":\"value\",\"special\":\"quote \\\"\"}")
    logger.info("JSON message {\"test\":\"value\",\"more words test\":\"more words value\",\"special\":\"quote \\\"\"}")
    logger.info("JSON message with extra {\"test\":\"value\"}", extra={"test": "value"})
    logger.info("JSON message with extra {\"test\":\"value\",\"more words test\":\"more words value\"}", extra={"test": "value", "more words test": "more words value"})
    logger.info("JSON message with extra {\"test\":\"value\",\"special\":\"quote \\\"\"}", extra={"test": "value", "special": "quote \""})
    logger.info("JSON message with extra {\"test\":\"value\",\"more words test\":\"more words value\",\"special\":\"quote \\\"\"}", extra={"test": "value", "more words test": "more words value", "special": "quote \""})
    time.sleep(1)

