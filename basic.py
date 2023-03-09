import requests

# if we want to change any info, we can insert a header line here:
# head = {"User-Agent": "Mozilla/5.0 (Windows NT1 0.0; Win64; x64)"}
# This is a way to hide the actual identification of your equipment.
# It is more commonly used to pretend ourselves as a normal browser rather than a crawler.
response = requests.get("http://book.toescape.com/")  # add a parameter after this URL, headers = head
if 200 <= response.status_code < 400:  # if response.ok == true:
    print(response.text)
elif 400 <= response.status_code < 500:
    print("Requests failed, client's error")
elif response.status_code >= 500:
    print("Requests failed, server's error")
