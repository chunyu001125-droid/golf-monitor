import os
import requests
from bs4 import BeautifulSoup

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

DATE = "2026-11-29"

URL = f"https://www.kscgolf.org.hk/eng/golf/golf-bookings/reservation-status/?d={DATE}"

resp = requests.get(URL, timeout=30)

if resp.status_code != 200:
    print("Website error")
    exit()

html = resp.text

# 臨時版本：
# 如果 South Course 區域內有 Available 就通知

if "status-a" in html:

    message = f"""
🏌️ KSC Golf Alert

Date: {DATE}
Course: South Course
Time: 11:00-11:30

Available slot detected!
"""

    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": message
        }
    )

    print("Notification sent")

else:
    print("No slot")
