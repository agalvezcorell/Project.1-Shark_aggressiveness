import re
def limpiadate(x):
    match = re.search("\d{4}",x)
    if match:
        x = int(match.group()) -1
    else:
        x = 0
    return x


