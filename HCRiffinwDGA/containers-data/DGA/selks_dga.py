#!/usr/bin/python3

from getDomain import getDomains
from predictDGA import get_prediction
import config

from datetime import datetime
import pytz
import threading

id = None

def setInterval(func, sec):
    e = threading.Event()
    func()
    while not e.wait(sec):
        func()

def main():
    current_datetime = datetime.now()  # local date and time
    UTC = pytz.utc
    current_datetime = UTC.localize(current_datetime)
    VN_TZ = pytz.timezone('Asia/Ho_Chi_Minh')
    current_datetime = current_datetime.astimezone(VN_TZ)
    # current_date = current_date.replace(tzinfo=timezone.utc+7)
    # current_time = datetime.time(current_datetime)  # time only
    current_date = datetime.date(current_datetime)  # date only

    print("\n=====================================================================================")
    print("Current: ", current_datetime)
    print("=====================================================================================\n")

    url = f'http://{config.SELKS_IP}:{config.SELKS_PORT}/logstash-dns-{current_date.strftime("%Y.%m.%d")}/_search'
    domains = getDomains(url)

    get_prediction(domains, show=True)

if __name__ == "__main__":
    setInterval(main, config.INTERVAL)
