#!/usr/bin/python3
import logging
import random
import time
logging.basicConfig(filename='http.log',  level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def log_something():
   flog = random.choice([logging.info, logging.info, logging.warn, logging.info, logging.error])
   time=random.random() * random.randint(20,400)
   traceid=random.randint(9999,9876543)
   flog(f'time={time} traceid={traceid}')


def spike():
   flog = random.choice([logging.info, logging.warn, logging.error])
   time=random.random() * random.randint(900,1900)
   traceid=random.randint(9999,9876543)
   flog(f'time={time} traceid={traceid}')


while True :
   sleeptime = 0.1 + random.random()
   log_something()
   if sleeptime > 0.96:
      for i in range(1,9):
         spike()
   time.sleep(sleeptime)

