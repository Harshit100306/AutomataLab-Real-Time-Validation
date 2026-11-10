"""Finite-state validators for the AutomataLab demonstration."""
def validate_password(password: str) -> bool:
    if not isinstance(password, str) or not 8 <= len(password) <= 20:
        return False
    flags = [False, False, False, False]
    for ch in password:
        if "a" <= ch <= "z": flags[0] = True
        elif "A" <= ch <= "Z": flags[1] = True
        elif "0" <= ch <= "9": flags[2] = True
        elif ch in "!@#$%^&*": flags[3] = True
        else: return False
    return all(flags)

def validate_email(email: str) -> bool:
    if not isinstance(email, str) or not email or any(c.isspace() for c in email) or email.count("@") != 1:
        return False
    local, domain = email.split("@")
    allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._%+-"
    if not local or any(c not in allowed for c in local) or local[0] == "." or local[-1] == "." or ".." in local:
        return False
    labels = domain.split(".")
    if len(labels) < 2: return False
    for label in labels:
        if not label or not label[0].isalnum() or not label[-1].isalnum(): return False
        if any(not (c.isascii() and (c.isalnum() or c == "-")) for c in label): return False
    return len(labels[-1]) >= 2 and all(c.isascii() and c.isalpha() for c in labels[-1])

def validate_pin(pin: str) -> bool:
    return isinstance(pin, str) and len(pin) == 4 and all("0" <= c <= "9" for c in pin)
