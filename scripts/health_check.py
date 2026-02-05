import urllib.request

print("Post-deployment health check started")

url = "https://www.google.com"

try:
    urllib.request.urlopen(url, timeout=5)
    print("Application is healthy")
except:
    print("Application is unhealthy")
