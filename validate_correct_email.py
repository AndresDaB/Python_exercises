def valid_email(usuarios):
    for usuario in usuarios:
        nombre = usuario.get("nombre", "desconocido")
        email = usuario.get("email", "")

        if "@" in email and email.strip() != "":
            print(f"Email válido para {nombre}: {email}")
        else:
            print(f"Email inválido para {nombre}")

usuarios = [
    {"nombre": "Ana", "email": "ana@example.com"},
    {"nombre": "Luis", "email": ""},
    {"nombre": "Carlos"},
    {"nombre": "Marta", "email": "marta@example.com"}
]

valid_email(usuarios)
