import requests
import sys

def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {'message': msg }
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code


if __name__ == "__main__":
  token = sys.argv[1]
  message = sys.argv[2]
  lineNotifyMessage(token, message)
