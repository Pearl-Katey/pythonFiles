import requests

google = requests.get("https://www.google.com")

if google.status_code != 200:
    print("Error encountered, please restart your code")