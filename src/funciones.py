import re
def limpiadate(x):
    match = re.search("\d{4}",x)
    if match:
        x = int(match.group()) -1
    else:
        x = 0
    return x


def assignscore3(x):
    if x == "Y":
        x = 3
    else:
        x = "N"
    return x


def assingscore(x):
    nivel2 = "2"
    nivel1 = "1"
    nivel3 = "3"
    if type(x) != str:
        x = nivel2
    if re.search (r"(.*)?acera(.*)?", x) != None:
        x = nivel1
    if re.search (r"(.*)?o inju(.*)?", x) != None:
        x = nivel1
    if re.search (r"(.*)?inor(.*)?", x) != None:
        x = nivel1     
    if re.search (r"(.*)?o in(.*)?", x) != None:
        x = nivel1
    if re.search (r"(.*)?FATAL(.*)?", x) !=None:
        x= nivel3
    if re.search (r"(.*)? (.*)?", x) != None:
        x= nivel2
    if re.search (r"(.*)?urvi(.*)?", x) != None:
        x= nivel2
    if re.search (r"(.*)?on(.*)?", x) != None:
        x= nivel2
    if re.search (r"(.*)?bras(.*)?", x) != None:
        x= nivel2
    if re.search (r"(.*)?over(.*)?", x) != None:
        x= nivel2
    if re.search (r"(.*)?aule(.*)?", x) != None:
        x= nivel2
    return x