import urllib.request
import sys

print("Post-deployment health check started")

url = "https://invalid-health-check-url.example"

try:
    urllib.request.urlopen(url, timeout=5)
    print("Application is healthy")
    sys.exit(0)
except Exception:
    print("Application is unhealthy")
    sys.exit(1)

