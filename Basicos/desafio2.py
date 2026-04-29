# Lê a linha de entrada e separa os produtos em uma lista
produtos = input().strip().split()

# TODO: Crie uma estrutura para contar quantas vezes cada produto aparece na lista

# Dica: Use um laço para percorrer a lista e atualizar a contagem de cada produto

# Inicialize variáveis para armazenar o produto mais frequente e sua contagem
mais_frequente = None
maior_contagem = -1

# Percorra a lista original para garantir o critério de desempate (primeira ocorrência)
for produto in produtos:
    # TODO: Obtenha a contagem do produto atual e atualize mais_frequente se necessário
    mais_frequente = produto if produtos.count(produto) > maior_contagem else mais_frequente
    maior_contagem = produtos.count(produto) if produtos.count(produto) > maior_contagem else maior_contagem

# Imprima o produto mais frequente
print(mais_frequente)