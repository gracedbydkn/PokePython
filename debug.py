from data.loader import importarPokemons, importarLocais
from classes.jogador import Jogador
from classes.local import Local
import batalha
import menu

def telaExploracao(jogador: Jogador):
    while True:
        local = jogador.localAtual

        if local.isCura:
            menu.limparTela()
            print(f"\n  {menu.V}★ {local.nome} ★{menu.RESET}")
            print(f"\n  Sua equipe foi totalmente curada!")
            local.curarEquipe(jogador)
            input(f"\n  {menu.Y}Pressione Enter para continuar...{menu.RESET}")
        
        elif local.pokemon and local.pokemon.isVivo():
            resultado = batalha.iniciarBatalha(jogador, local.pokemon, local.nome)
            if resultado == "derrota":
                return "derrota"

        if not local.caminhos:
            return "fim"
        
        menu.limparTela()
        print(f"\n  {menu.Y}★  {local.nome}  ★{menu.RESET}")
        print(f"\n  Para onde você deseja ir?")
        print("─" * 124)

        for i, caminho in enumerate(local.caminhos, 1):
            temPokemon = f"  {menu.R}[!]{menu.RESET}" if caminho.pokemon and caminho.pokemon.isVivo() else f"  {menu.V}[✓]{menu.RESET}" if not caminho.isCura else f"  {menu.C}[+]{menu.RESET}"
            print(f"\n  [{menu.Y}{i}{menu.RESET}] {caminho.nome}{temPokemon}")
        
        print()
        print("─" * 124)

        while True:
            escolha = input(f"\n  {menu.Y}>{menu.RESET} ").strip()
            if escolha.isdigit() and 1 <= int(escolha) <= len(local.caminhos):
                jogador.mover(local.caminhos[int(escolha) - 1])
                break
            print("  Escolha inválida")

def main():
    pokemons = importarPokemons()
    locais = importarLocais(pokemons=pokemons)


    while True:
        menu.exibirMenu()
        escolha = input("\n  > ").strip()

        if escolha == "1":
            pokemonInicial = menu.escolherInicial(pokemons)

            jogador = Jogador(
                equipe = [pokemonInicial],
                localAtual = locais["Ovo"]
            )

            resultado = telaExploracao(jogador)
            if resultado == "fim":
                menu.limparTela()
                print(menu.LOGO)
                menu.digitar(f"  {menu.Y}Sua jornada chegou ao fim, Treinador.{menu.RESET}", delay=0.05)
                input(f"\n  {menu.Y}Pressione Enter para voltar ao menu...{menu.RESET}")

        elif escolha == "2":
            menu.limparTela()
            menu.printMENU()
            print(f"\033[33m═\033[0m" * 124)
            print("  ")
            exit()
        else:
            print("  Escolha inválida")

if __name__ == "__main__":
    main()