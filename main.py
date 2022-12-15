import re

data = open("data.html", 'r', encoding="UTF-8")
s = ''
for i in data:
    s += i
data.close()
match = re.findall(r"\b[A-Za-z0-9]+[-_.]*\w+@\w+\.?\w+\.\w+\b", s, re.ASCII)
print(match)
