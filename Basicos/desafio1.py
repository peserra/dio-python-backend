def main():
    entrada = input().strip()
    preco_str, codigo_promocao = entrada.split()

    # Conversão do preço para float
    preco = float(preco_str)

    # TODO: Se o produto estiver em promoção ("S"), aplique 10% de desconto ao preço.
    # Caso contrário, mantenha o preço original.
    # Dica: Use uma estrutura condicional para decidir qual valor atribuir à variável preco_final.

    preco_final = float(preco_str) * 0.9 if codigo_promocao == "S" else float(preco_str)

    # Exibe o valor final com duas casas decimais
    print(f"{preco_final:.2f}")
    pass
if __name__ == "__main__":
    main()