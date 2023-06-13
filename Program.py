# Criando as listas

locais_brasil = [
    ("Fernando de Noronha", 10000),
    ("Rio de Janeiro", 2500),
    ("Bonito", 3500),
    ("Chapada Diamantina", 8000),
    ("Serras Gaúchas", 5500),
    ("Salvador", 4000),
    ("Natal", 3500),
    ("Amazônia", 8500),
    ("Búzios", 2800),
    ("Brasília", 4200),
]

locais_mundo = [
    ("Buenos Aires", 3000),
    ("Nova York", 15000),
    ("Paris", 8500),
    ("Tóquio", 12000),
    ("Cairo", 7000),
    ("Casablanca", 6800),
    ("Nova Deli", 8500),
    ("Ilha de Páscoa", 11000),
    ("Havaí", 8300),
    ("Quebec", 7000),
]

# Classificando-as em ordem de preço
locais_brasil.sort(key=lambda x: x[1], reverse=True)
locais_mundo.sort(key=lambda x: x[1], reverse=True)

# Imprimindo os cinco locais mais caros do Brasil
print ("Locais mais caros do Brasil:")
for i in range(5):
    print(f"{i+1}.{locais_brasil[i][0]} - R${locais_brasil[i][1]:.2f}")

#Imprimindo os cinco locais mais baratos do mundo
print ("Locais mais baratos do mundo:")
for i in range(5):
    print(f"{i+1}.{locais_mundo[-(i+1)][0]} - R${locais_mundo[-(i+1)][1]:.2f}")
