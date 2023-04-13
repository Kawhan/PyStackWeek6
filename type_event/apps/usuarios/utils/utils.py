import re


def verificar_senha_forte(senha):
    # Verifica se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        return False

    # Verifica se a senha contém pelo menos uma letra maiúscula
    if not re.search("[A-Z]", senha):
        return False

    # Verifica se a senha contém pelo menos uma letra minúscula
    if not re.search("[a-z]", senha):
        return False

    # Verifica se a senha contém pelo menos um número
    if not re.search("[0-9]", senha):
        return False

    # Verifica se a senha contém pelo menos um caractere especial
    if not re.search("[!@#$%^&*()_+-={};:'\"<>,.?/|\\]", senha):
        return False

    # Se a senha passar por todas as verificações, retorna True
    return True
