import re
pattern = re.compile(r'((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)')
match = pattern.search('192.168.1.1')
if match:
    print(match.group(0))
