class Livro:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f"Nome: {self.nome}\nPreço: ${self.preco:.2f}\nQuantidade disponível: {self.quantidade}\n"

class ColecaoLivros:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, nome, preco, quantidade):
        # Verifica se já existe um livro com o mesmo nome na coleção
        if not any(livro.nome == nome for livro in self.livros):
            livro = Livro(nome, preco, quantidade)
            self.livros.append(livro)
            print(f'O livro "{nome}" foi adicionado.')
        else:
            print(f'Já existe um livro com o nome "{nome}" na lista.')

    def remover_livro(self, nome):
        self.livros = list(filter(lambda livro: livro.nome != nome, self.livros))

    def modificar_livro(self, nome, novo_nome, novo_preco, nova_quantidade):
        for livro in self.livros:
            if livro.nome == nome:
                livro.nome = novo_nome
                livro.preco = novo_preco
                livro.quantidade = nova_quantidade

    def ordenar_lista(self):
        self.livros.sort(key=lambda livro: livro.preco)

    def exibir_lista(self):
        for livro in self.livros:
            print(livro)

lista_livros = ColecaoLivros()

while True:
    print("\n--- Menu ---")
    print("1. Inserir")
    print("2. Remover")
    print("3. Modificar")
    print("4. Exibir Lista")
    print("5. Sair")

    escolha = input("Escolha uma opção (1-5): ")

    if escolha == '1':
        nome = input("Digite o nome do livro: ")
        preco = float(input("Digite o preço do livro: "))
        quantidade = int(input("Digite a quantidade disponível do livro: "))
        lista_livros.adicionar_livro(nome, preco, quantidade)

    elif escolha == '2':
        nome = input("Digite o nome do livro a ser removido: ")
        lista_livros.remover_livro(nome)

    elif escolha == '3':
        nome = input("Digite o nome do livro a ser modificado: ")
        novo_nome = input("Digite o novo nome do livro: ")
        novo_preco = float(input("Digite o novo preço do livro: "))
        nova_quantidade = int(input("Digite a nova quantidade disponível do livro: "))
        lista_livros.modificar_livro(nome, novo_nome, novo_preco, nova_quantidade)

    elif escolha == '4':
        lista_livros.exibir_lista()

    elif escolha == '5':
        break

    else:
        print("Opção inválida. Tente novamente.")
