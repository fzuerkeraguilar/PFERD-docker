from mmap import PROT_READ
from crontab import CronTab, CronSlices
import os

WORKING_DIR: str = "/pferd/working-dir"
CONFIG_FILE: str = "/pferd/pferd.cfg"

def setup():
    cron_schedule: str = os.getenv("CRON_SCHEDULE")
    if not CronSlices.is_valid(cron_schedule):
        print("Could not parse PFERD cron job")
        return False
    if not os.path.exists(CONFIG_FILE):
        print("Could not find PFERD config file")
        return False
    if not os.path.exists(WORKING_DIR):
        os.mkdir(WORKING_DIR)
    cron = CronTab(user=True)
    job = cron.new(command=f"pferd -c {CONFIG_FILE} --working-dir {WORKING_DIR} 1>> /proc/1/fd/1")
    job.setall(cron_schedule)
    cron.write()
    job.run()
    return True

def sleep():
    import time
    while True:
        time.sleep(100)

if __name__ == "__main__":
    if setup():
        sleep()