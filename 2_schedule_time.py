import schedule
import time

def task():
    print("hello world!")

job = schedule.every().tuesday.at("11:05").do(task)

while True:
    print("checking")
    schedule.run_pending()
    time.sleep(1)

schedule.every().tuesday.at("11:05").do(task)
