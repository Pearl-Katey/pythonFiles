import requests

google = requests.get("https://www.google.com")

if google.status_code != 200:
    print("Error encountered, please restart your code")
else:
    print("Youu requested a webapage on " + google.headers["Date"])
    print("Your webpage will be downloaded shortly")
    page = google.text

    fil = open("index.html", "w")
    fil.write(page)
    fil.close()