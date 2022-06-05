# Second part of generate.py
# These need to be combined
with open('ipList.txt') as f:
    lines = f.readlines()
f.close()

payload = open("payload.txt", "a")
header = "X-Forwarded-For: "
for ip in lines:
    complete = (header+ip)
    payload.write(complete)
payload.close()
