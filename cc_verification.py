import re

# Precompila padrões regex para diferentes bandeiras de cartões de crédito
CARD_BRANDS = {
    'Visa': re.compile(r'^4[0-9]{12}(?:[0-9]{3})?$'),
    'MasterCard': re.compile(r'^5[1-5][0-9]{14}$'),
    'American Express': re.compile(r'^3[47][0-9]{13}$'),
    'Diners Club': re.compile(r'^3(?:0[0-5]|[68][0-9])[0-9]{11}$'),
    'Discover': re.compile(r'^6(?:011|5[0-9]{2})[0-9]{12}$'),
    'JCB': re.compile(r'^(?:2131|1800|35\d{3})\d{11}$')
}

def validar_bandeira_cartao(numero_cartao):
    """
    Valida a bandeira do cartão de crédito com base no número do cartão.
    
    Parâmetros:
    numero_cartao (str): O número do cartão de crédito a ser validado.
    
    Retorna:
    str: O nome da bandeira do cartão de crédito ou "Bandeira desconhecida" se não for reconhecida.
    """
    for bandeira, pattern in CARD_BRANDS.items():
        if pattern.fullmatch(numero_cartao):
            return bandeira
    return "Bandeira desconhecida"

# Exemplo de uso
if __name__ == "__main__":
    numero_cartao = "4111111111111111"
    bandeira = validar_bandeira_cartao(numero_cartao)
    print(f"A bandeira do cartão é: {bandeira}")
