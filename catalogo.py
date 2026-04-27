import json
import datetime as time
import os

ARQUIVOS_DADOS = "meus_filmes.json"

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def carregar_dados():
    try:
        with open(ARQUIVOS_DADOS,"r", encoding="uft-8") as arquivo:
                return json.load(arquivo)
    except:
         print("arquivo não existe criando lista vazia")
         return[]    

def salvar_dados(dados):
     with open(ARQUIVOS_DADOS,"w",encoding="uft-8") as arquivo:
          json.dump(dados,arquivo,indent=4,ensure_ascii=False)   

def obter_ano_valido():
     while True:
          try:
               ano = int(input("ano de lançamento: "))

               if ano < 1888 or ano > time.date().year:
                    print("por favor digite um ano valido")
                    continue
               return ano
          except ValueError:
               print("ERRO: digite apenas numeros inteiros para o ano") 
def obter_nota_valida():
    while True:
        try:
            nota = float(input("Nota (0.0 a 5.0): "))
            
            if nota < 0.0 or nota > 5.0:
                print("A nota deve estar entre 0 e 5.")
                continue
            
            return nota
        except ValueError:
            print("Erro: Digite um valor numérico (use ponto para decimais).")

def adicionar_filme(catalogo):
    limpar_tela()
    print("--- 🎬 REGISTRAR NOVO FILME ---")
    titulo = input("Titulo: ").strip()

    for filme in catalogo:
        if filme["titulo"].lower() == titulo.lower():
            print(f"\n ⚠️ Atenção: O filme '{filme['titulo']}' já está cadastrado no seu catalogo!")
            return
    
    genero = input("Gênero (ex: Ação, Comédia, Drama): ").strip()
    ano = obter_ano_valido()
    nota = obter_nota_valida()
    critica = input("Breve critica: ").strip()

    filme = {
        "titulo": titulo,
        "genero": genero,
        "ano": ano,
        "nota": nota,
        "critica": critica
    }

    catalogo.append(filme)
    salvar_dados(catalogo)
    print(f"✅ '{titulo}' adicionado com sucesso ao seu catálogo!")


def listar_filmes(catalogo):
    limpar_tela()
    print("=" * 40)
    print("         🎞️ MINHA COLEÇÃO")
    print("=" * 40)

    if not catalogo:
        print("O seu catálogo está vazio. Adicione um filme primeiro!")
        print("=" * 40)
        return
    
    for filme in catalogo:
        estrelas = "⭐" * int(filme["nota"])
        genero = filme.get("genero", "Desconhecido")

        print(f"[{filme['ano']}] {filme['titulo'].upper()} ({genero}) | Nota: {filme['nota']:.1f} {estrelas}")
        print("-" * 40)


def pesquisar_por_titulo(catalogo):
    limpar_tela()
    termo = input("Digite parte do titulo para pesquisar: ").strip().lower()

    resultados = []
    for filme in catalogo:
        if termo in filme["titulo"].lower():
            resultados.append(filme)
    
    _exibir_resultados_pesquisa(resultados)


def pesquisar_por_genero(catalogo):
    limpar_tela()
    termo = input("Digite o gênero para pesquisar (ex: Ação): ").strip().lower()

    resultados = []
    for filme in catalogo:
        if termo in filme.get("genero", "").lower():
            resultados.append(filme)
    
    _exibir_resultados_pesquisa(resultados)


def pesquisar_por_ano(catalogo):
    limpar_tela()
    try:
        ano_pesquisa = int(input("Digite o ano de lançamento exato para pesquisar: "))
    except ValueError:
        print("Erro: Digite um ano válido (número inteiro).")
        return

    resultados = []

    for filme in catalogo:
        if filme["ano"] == ano_pesquisa:
            resultados.append(filme)
        
    _exibir_resultados_pesquisa(resultados)


def _exibir_resultados_pesquisa(resultados):
    if resultados:
        print(f"\n🔍 Encontrados {len(resultados)} resultado(s):")

        for filme in resultados:
            genero = filme.get("genero", "Desconhecido")
            print(f"> {filme['titulo']} ({filme['ano']}) - {genero} - Nota: {filme['nota']}")
    
    else:
        print("\n❌ Nenhum filme encontrado com esses critérios.")


if __name__ == "__main__":
    lista_filmes = carregar_dados()
    pesquisar_por_ano(lista_filmes)                       