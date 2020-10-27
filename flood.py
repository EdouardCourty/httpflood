import sys
import requests as http
import threading
import time as t
from truncate import truncate as tru

argv = sys.argv[1:len(sys.argv)]

req = 1000
to_start = 1

if len(argv) == 0:
    print('python3 flood.py <host> <requests> <threads>')
    exit()

h = argv[0]

if len(argv) == 2:
    req = int(argv[1])
elif len(argv) > 2:
    req = int(argv[1])
    to_start = int(argv[2])

print(f"Starting with the following parameters:\n > h: {h}\n > Requests: {req}\n > Threads: {to_start}")
is_correct = str.lower(input("Are these values correct ? (Y/N) "))

if not is_correct == "y":
    exit()

sent = 0


def send(n):
    global sent
    while sent < (n - to_start + 1):
        http.get(h)
        sent += 1
        print(f"Sent {sent} requests on {n} requested. ({(sent/n)*100} %)")


threads = []
st = t.time()

for i in range(to_start):
    thread = threading.Thread(target=send, args=(int(req),))
    thread.start()
    threads.append(thread)


for thread in threads:
    thread.join()

tn = (t.time() - st)
print(f'Done ! Finished in {tru(tn, 4)} seconds. (~ {tru(req / tn, 2)} requests per second.)')
