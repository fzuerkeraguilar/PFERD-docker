from crontab import CronTab, CronSlices
import os

def setup():
    cron_schedule = os.getenv("PFERD_CRON")
    if not CronSlices.is_valid(cron_schedule):
        print("Could not parse PFERD cron job")


if __name__ == "__main__":
    setup()