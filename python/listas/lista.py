# Listas vazias
lista_vazia: list = []
lista_vazia2: list = list()

# Listas com valores
numeros: list[int] = [1, 2, 3, 4, 5]
nomes: list[str] = ["fulano", "beltrano", "ciclano"]
mistos: list = [1, "texto", 3.14, True, None]

print("Numeros:", numeros)
print("Nomes:", nomes)
print("Valores mistos:", mistos)
print("Listas vazias:", lista_vazia, lista_vazia2)

pares: list[int] = list(range(0, 20, 2))
print("Numeros pares:", pares)

frutas: list[str] = ["maca", "banana", "carambola", "uva"]
print("Primeira fruta:", frutas[0])
print("Terceira fruta:", frutas[2])
print("Ultima fruta:", frutas[-1])
print("Penultima fruta:", frutas[-2])
print("Todas as frutas:", frutas)

