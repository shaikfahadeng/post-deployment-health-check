import urllib.request
import sys

print("Post-deployment health check started")

url = "https://www.google.com"

try:
    urllib.request.urlopen(url, timeout=70)
    print("Application is healthy")
    sys.exit(0)   # success
except:
    print("Application is unhealthy")
    sys.exit(1)   # failure
