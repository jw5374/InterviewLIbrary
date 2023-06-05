def decodeMessage(key: str, message: str) -> str:
    cipher = {}
    i = 0
    for c in key:
        if c == " " or c in cipher:
            continue
        cipher[c] = i
        i += 1
    return "".join([chr(cipher[c] + 97) if c != " " else " " for c in message])
