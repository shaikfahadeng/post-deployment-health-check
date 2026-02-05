import urllib.request
import sys

print("Post-deployment health check started")

url = "https://www.google.com"

try:
    urllib.request.urlopen(url, timeout=5)
    print("Application is healthy")
    sys.exit(0)   # SUCCESS → pipeline continues
except Exception as e:
    print("Application is unhealthy")
    sys.exit(1)   # FAILURE → pipeline stops 
