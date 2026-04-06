<<<<<<< HEAD
import datetime

def log_activity(activity):
    with open("activity.log", "a") as f:
=======
import datetime

def log_activity(activity):
    with open("activity.log", "a") as f:
>>>>>>> 937145374ef1cb54abd7cc95f7939691e2e304be
        f.write(f"{datetime.datetime.now()} - {activity}\n")