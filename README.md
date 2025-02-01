## Problem
Some WAFs/Applications block user access based on IP geolocation

## Solution
Given a target host + a list of country proxies -> check if access is possible from any of the proxy countries

## Usage

```
python3 check.py https://icanhazip.com proxies.json

[+] Checking access to https://icanhazip.com

Host reachable from Brazil
Host reachable from Germany
Host reachable from France
Host reachable from Finland
Host reachable from Italy
Host reachable from USA
Host reachable from UK
Host reachable from India
Host reachable from China
Host reachable from Australia
```
