def checkPass(p):
    has_upper = any(c.isupper() for c in p)
    has_lower = any(c.islower() for c in p)
    has_digit = any(c.isdigit() for c in p)
    return len(p) >= 8 and has_upper and has_lower and has_digit