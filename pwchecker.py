def pwcheck(password):
    lower = True in [True if x.islower() else False for x in password]
    upper = True in [True if x.isupper() else False for x in password]
    number = True in [True if x.isdigit() else False for x in password]
    return lower and upper and number

def pwcheck(password):
    lower = True in [True if x.islower() else False for x in password]
    upper = True in [True if x.isupper() else False for x in password]
    number = True in [True if x.isdigit() else False for x in password]
    special = True in [True if x in "()$&@?!,<>~+*^%#" else False for x in password]
    score = 0
    if lower:
        score += 1
    if upper:
        score += 2
    if number:
        score += 3
    if special:
        score += 4
    return score
