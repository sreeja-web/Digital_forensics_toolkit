import datetime

def log_activity(activity):
    with open("activity.log", "a") as f:
        f.write(f"{datetime.datetime.now()} - {activity}\n")