def defangIPaddr(address: str) -> str:
    return "[.]".join(address.split("."))


print(defangIPaddr("1.1.1.1"))

