
from recommender import recomendar_pratos

print("🍔 FOODMIND AI")
print("----------------------")

orcamento = float(input("💰 Qual seu orçamento? R$ "))

recomendacoes = recomendar_pratos(orcamento)

if not recomendacoes:
    print("Nenhum prato encontrado nesse orçamento.")
else:
    print("\n🏆 Ranking de recomendações:\n")

    for posicao, prato in enumerate(recomendacoes, start=1):
        print(f"#{posicao} - {prato['nome']}")
        print(f"💰 R$ {prato['preco']:.2f}")
        print(f"💪 {prato['proteina_g']}g de proteína")
        print(f"🔥 {prato['calorias']} kcal")
        print(f"⭐ Score: {prato['score']:.2f}/10")
        print("----------------------")
