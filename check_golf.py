import requests

URL = "https://www.kscgolf.org.hk/eng/golf/golf-bookings/reservation-status/?d=2026-11-29"

headers = {
    "User-Agent": "Mozilla/5.0"
}

resp = requests.get(
    URL,
    headers=headers,
    timeout=30
)

print("Status Code:", resp.status_code)
print("Final URL:", resp.url)

print(resp.text[:1000])
