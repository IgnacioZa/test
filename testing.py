#!/usr/bin/env python3
import time
import os
from datetime import datetime

def get_time():
    return datetime.today().strftime("%m/%d/%Y %H:%M:%S")

if __name__ == "__main__":
    actual_date = datetime.today()
    str_date = actual_date.strftime("%m/%d/%Y %H:%M:%S")
    print(get_time())
