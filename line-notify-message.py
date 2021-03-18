import requests
import os
from datetime import datetime

def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    payload = {'message': msg } # Ref: https://notify-bot.line.me/doc/en/
    
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code # status_code returns 200, 400, 401, etc.


if __name__ == "__main__":
    wd = datetime.today().isoweekday()
    if 1 <= wd and wd <= 5: # Means "if today is between Monday and Friday"
        # LINE_NOTIFY_TOKEN and LINE_NOTIFY_MESSAGE are both Heroku Config Vars
        token = os.environ['LINE_NOTIFY_TOKEN']
        message = os.environ['LINE_NOTIFY_MESSAGE']
        lineNotifyMessage(token, message)

