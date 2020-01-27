import re
def limpiadate(x):
    match = re.search(r"\d{4}",x)    
    if match:
        x = int(match.group()) -1
    else:
        x = 0
    return x


def asigna3(x):
    if x == "Y":
        x = 3
    else:
        x = "N"
    return x



level1 = ["(.*)?acera(.*)?", "(.*)?o inju(.*)?","(.*)?inor(.*)?","(.*)?o in(.*)?","(.*)?ruised(.*)?" ] 
level2 = ["(.*)?urvi(.*)?", "(.*)?on(.*)?", "(.*)?bras(.*)?","(.*)? (.*)?","(.*)?over(.*)?","(.*)?aule(.*)?"]
level3 = ["(.*)?FATAL(.*)?"]


def assingscore(x):
    import re
    nivel1 = "1"
    nivel2 = "2"
    nivel3 = "3"
    if type(x) != str:
        x = nivel2
        return x
    if x == None:
        x = nivel2
    for a in level1:
        if re.search (a,x) != None:
            x = nivel1
            return x
    for b in level2:
        if re.search (b,x) != None:
            x = nivel2
            return x
    for c in level3:
        if re.search (c,x) != None:
            x = nivel3
            return x


def casteascore(x):
    return int(x)