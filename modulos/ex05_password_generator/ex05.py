def generate_password(length = 12):
    import secrets
    import string

    random = secrets.SystemRandom()
    especial_characters = "@$._-()![]{}\\/"
    characters = ''.join(string.ascii_letters + string.digits + especial_characters)

    return ''.join(random.sample(characters, k=length))

passwords = [ generate_password(64) for _ in range(1)]

print(*passwords, sep="\n")