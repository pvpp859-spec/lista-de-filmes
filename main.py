import catalogo


def mostrar_menu():
    catalogo.limpar_tela()
    print("\n" + "=" * 40)
    print("             🍿 CineLog")
    print("="*40)
    print("1. Adicionar Filme/Série ➕")
    print("2. Ver o meu Catálogo 📓")
    print("3. Pesquisar por Título 🔍")
    print("4. Pesquisar por Gênero 🎭")
    print("5. Pesquisar por Ano 📅")
    print("6. Sair ❌")
    print("="*40)


def iniciar_app():
    meus_filmes = catalogo.carregar_dados()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                catalogo.adicionar_filme(meus_filmes)
                input("\n Pressione ENTER para voltar ao menu...")
            
            case "2":
                catalogo.listar_filmes(meus_filmes)
                input("\n Pressione ENTER para voltar ao menu...")
            
            case "3":
                catalogo.pesquisar_por_titulo(meus_filmes)
                input("\n Pressione ENTER para voltar ao menu...")

            case "4":
                catalogo.pesquisar_por_genero(meus_filmes)
                input("\n Pressione ENTER para voltar ao menu...")
            
            case "5":
                catalogo.pesquisar_por_ano(meus_filmes)
                input("\n Pressione ENTER para voltar ao menu...")
            
            case "6":
                catalogo.limpar_tela()
                catalogo.salvar_dados(meus_filmes)
                print("Salvando o catálogo... Até a próxima sessão de cinema! 🍿")
                break

            case _:
                print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    iniciar_app()