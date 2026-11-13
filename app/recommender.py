import csv

def carregar_pratos():
    pratos = []

    with open("data/pratos.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for prato in leitor:
            prato["preco"] = float(prato["preco"])
            prato["proteina_g"] = float(prato["proteina_g"])

            pratos.append(prato)
        
        return pratos

def recomendar_pratos(orcamento, objetivo):
    pratos = carregar_pratos()

    recomendados = []

    for prato in pratos:
        if prato["preco"] <= orcamento:
            recomendados.append(prato)

    if objetivo == "proteina":
        recomendados.sort(
            key=lambda prato: prato["proteina_g"],
            reverse=True
        )

    elif objetivo == "calorias":
        recomendados.sort(
            key=lambda prato: int(prato["calorias"])
        )
    
    return recomendados