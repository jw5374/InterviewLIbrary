import sys


def strongPasswordCheckerII(password: str) -> bool:
    if len(password) < 8:
        return False
    hasUpper = False
    hasLower = False
    hasDigit = False
    hasSpecial = False
    hasConsecutive = False
    i = 0
    specials = {"!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+"}
    while i < len(password) and not (hasUpper and hasLower and hasDigit and hasSpecial and hasConsecutive):
        hasSpecial = hasSpecial or password[i] in specials
        hasConsecutive = hasConsecutive or (password[i] == password[i+1] if i != len(password) - 1 else False)
        hasDigit = hasDigit or password[i].isdigit()
        hasUpper = hasUpper or password[i].isupper()
        hasLower = hasLower or password[i].islower()
        i += 1
    return hasUpper and hasLower and hasDigit and hasSpecial and (not hasConsecutive)


print(strongPasswordCheckerII(sys.argv[1]))

