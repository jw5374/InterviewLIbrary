def numUniqueEmails(emails: list[str]) -> int:
    uniqueEmails = set()
    for email in emails:
        uniqueEmails.add(normalizeEmail(email))
    return len(uniqueEmails)


def normalizeEmail(email: str) -> str:
    splitted = email.split("@")
    local = splitted[0].split("+")[0].replace(".", "")
    splitted[0] = local
    return "@".join(splitted)


print(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))

