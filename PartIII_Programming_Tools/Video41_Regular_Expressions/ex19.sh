import re


t = "__one__ __two__ __three__"


results = re.findall("__.*?__", t)


for match in results:
    print(match)
