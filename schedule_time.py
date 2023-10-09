import schedule
import time

def task():
    print("hello world!")

job = schedule.every().thursday.at("10:43").do(task)

while True:
    print("checking")
    schedule.run_pending()
    time.sleep(1)

schedule.every().thursday.at("10:43").do(task)
