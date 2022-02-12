import requests
import time
from datetime import datetime # https://docs.python.org/3/library/datetime.html
import math

# import secrets
import config

# returns time in local timezone
now = datetime.now()
nowposix = now.timestamp()

# returns next noon in local timezone
if now.hour < 12: # same day
    noon = datetime(now.year, now.month, now.day, 12, 00, 00)
else: # next day
    noon = datetime(now.year, now.month, now.day + 1, 12, 00, 00)
noonposix = math.floor(noon.timestamp())

# get percentage complete
startofyearposix = datetime(now.year, 1, 1).timestamp()
nextyearposix = datetime(now.year+1, 1, 1).timestamp()
percentage = (noonposix - startofyearposix) / (nextyearposix - startofyearposix)

# calculate the number of days left to next year
datenow = datetime(now.year, now.month, now.day).timestamp()
daysleft = (nextyearposix - datenow) / 86400
yearnext = now.year + 1

# webhook to post to Discord
# https://discord.com/developers/docs/reference#message-formatting
payload_start = {
    'content': f'It is now <t:{noonposix}:f>. {now.year} is {percentage*100}% complete. There are {daysleft:.0f} days left to {yearnext}.',
}

# wait until it is time to post
time.sleep(noonposix - nowposix)

r = requests.post(config.webhook_url, data=payload_start)

