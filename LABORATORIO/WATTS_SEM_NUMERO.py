
# WhatsApp sem salvar o número
from urllib.parse import quote

base = "https://wa.me/"
contatos = {
    "Ana": "5511900000001",
    "João": "5541900000002",
}

for nome, fone in contatos.items():
    msg = f"Olá, {nome}! Pedido pronto."
    link = f"{base}{fone}?text="
    print(link + quote(msg))