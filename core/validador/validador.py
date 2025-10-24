import re

def validar_cpf(cpf):
    """
    Valida um CPF (com ou sem pontos e traço).
    Retorna True se for válido, False caso contrário.
    """
    # Remove caracteres que não são números
    cpf = re.sub(r'\D', '', cpf)

    if len(cpf) != 11:
        return False

    # Evita CPFs com todos os números iguais (ex: 11111111111)
    if cpf == cpf[0] * 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    dig1 = (soma * 10 % 11) % 10

    # Calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    dig2 = (soma * 10 % 11) % 10

    return dig1 == int(cpf[9]) and dig2 == int(cpf[10])


def validar_nome(nome):
    """
    Valida um nome, o nome deve ter no mínimo 3 caracteres.
    Retorna True se for válido, False caso contrário
    """
    return True if len(nome) > 2 and len(nome) < 255 else False


def validar_idade(idade):
    """
    Valida uma idade, a idade deve ser maior ou igual a 0 e menor que 125 anos.
    Retorna True se for válido, False caso contrário
    """
    return True if idade >= 0 and idade < 125 else False


def validar_dados(cpf, nome, idade):
    """
    Valida cpf, nome, idade
    Retorna Dicionário com a mensagem de erro
    """
    if not validar_cpf(cpf):
        return {"erro":"CPF inválido"}
    elif not validar_nome(nome):
        return {"erro":"Nome inválido"}
    elif not validar_idade(idade):
        return {"erro":"Idade inválida"}
    else:
        return True