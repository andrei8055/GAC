import requests
import json
import urllib3
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


if len(sys.argv) != 3:
	print("Usage: python3 script.py <host> <proxy_file>")
	sys.exit(1)

target_host = sys.argv[1]
proxy_file = sys.argv[2]

print("[+] Checking access to " + target_host)
print("")
# Read the JSON file
with open("proxies.json", "r") as file:
    data = json.load(file)

# Iterate through the proxies and print them
for proxy_obj in data.get("proxies", []):
	proxy = {
		"http": "http://" + proxy_obj['ip'] + ":" + str(proxy_obj['port']),
		"https": "http://" + proxy_obj['ip'] + ":" + str(proxy_obj['port'])
	}

	try:
	    # Make the request through the proxy
	    response = requests.get(target_host, proxies=proxy, timeout=10, verify=False)
	    if response.status_code == 200:
	    	print("Host reachable from " + proxy_obj['country'])
	except requests.RequestException as e:
		pass
	except requests.Timeout as e:
		pass