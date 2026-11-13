from recommender import recomendar_pratos

print("🍔 FOODMIND AI")
print("----------------------")

orcamento = float(input("💰 Qual seu orçamento? R$ "))

print("\n🎯 Qual é seu objetivo?")
print("1 - Consumir mais proteína")
print("2 - Consumir menos calorias")

escolha = input("\nEscolha uma opção: ")

if escolha == "1":
    objetivo = "proteina"

elif escolha == "2":
    objetivo = "calorias"

else:
    print("Opção inválida!")
    exit()

recomendacoes = recomendar_pratos(orcamento, objetivo)

print("\n🍽️ Pratos recomendados:\n") 

if not recomendacoes:
    print("Nenhum prato encontrado nesse orçamento.")

for prato in recomendacoes:
    print(f"🍔 {prato['nome']}")
    print(f"💰 Preço: R$ {prato['preco']:.2f}")
    print(f"💪 Proteína: {prato['proteina_g']}g")
    print(f"🔥 Calorias: {prato['calorias']} kcal")
    print("----------------------")