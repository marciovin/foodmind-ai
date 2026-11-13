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


def recomendar_pratos(orcamento):
    pratos = carregar_pratos()

    recomendados = []

    # Filtragem pelo orçamento
    for prato in pratos:
        if prato["preco"] <= orcamento:
            recomendados.append(prato)

    if not recomendados:
        return []

    # Encontrar os valores de referência
    max_proteina, min_calorias = obter_referencias(recomendados)

    # Calcular pontuação de cada prato
    for prato in recomendados:
        prato["score"] = calcular_score(
            prato,
            max_proteina,
            min_calorias
        )

    # Ordenar da maior para a menor pontuação
    recomendados.sort(
        key=lambda prato: prato["score"],
        reverse=True
    )

    return recomendados


def calcular_score(prato, max_proteinas, min_calorias):
    proteina = prato["proteina_g"]
    calorias = float(prato["calorias"])

    pontos_proteinas = (proteina / max_proteinas) * 10

    pontos_calorias = (min_calorias / calorias) * 10

    score = (pontos_proteinas * 0.7) + (pontos_calorias * 0.3)

    return score

def obter_referencias(pratos):
    max_proteina = max(
        prato["proteina_g"] for prato in pratos
    )

    min_calorias = min(
        float(prato["calorias"]) for prato in pratos
    )

    return max_proteina, min_calorias