#!/usr/bin/python
import psycopg2
import datetime
import json
import decimal
from corpscanada.config import config
from corpscanada.eventprocessor import EventProcessor


with EventProcessor() as event_processor:
    event_processor.process_corp_event_queue(True)


