def forditott(szo):
    if szo == "":
        return ""
    return forditott(szo[1:]) + szo[0]

print(forditott("szia"))