from data.loader import importarPokemons, importarLocais
from classes.jogador import Jogador
from classes.local import Local
import batalha
import menu
from menu import LOGO

def exibirCabecalhoLocal(local):
    (print("\033[33m═\033[0m" * 124))
    if local.titulo:
        for linha in local.titulo:
            print(f"\033[33m{linha:^124}\033[0m")
    else:
        print(f"\033[36m{'★  ' + local.nome.upper() + '  ★':^124}\033[0m")
    print("\033[33m═\033[0m" * 124)

def telaExploracao(jogador: Jogador, pokemons: dict):
    while True:
        local = jogador.localAtual

        if local.isCura:
            menu.limparTela()
            exibirCabecalhoLocal(local)
            print(f"\n  Sua equipe foi totalmente curada!")
            local.curarEquipe(jogador)
            input(f"\n  {menu.Y}Pressione Enter para continuar...{menu.RESET}")
        
        elif local.pokemon and local.pokemon.isVivo() and not local.visitado:
            resultado = batalha.iniciarBatalha(jogador, local.pokemon, local, pokemons)
            if resultado == "derrota":
                return "derrota"
            local.visitado = True
            continue

        if not local.caminhos:
            return "fim"
        
        menu.limparTela()
        exibirCabecalhoLocal(local)
        print(f"\n  Para onde você deseja ir?")
        print("─" * 124)
        
        for i, caminho in enumerate(local.caminhos, 1):
            print(f"\n  [{menu.Y}{i}{menu.RESET}] {caminho.nome}")
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

            resultado = telaExploracao(jogador, pokemons)
            if resultado == "fim":
                menu.limparTela()
                print(menu.LOGO)
                menu.digitar(f"  {menu.Y}Sua jornada chegou ao fim, Treinador.{menu.RESET}", delay=0.05)
                exit()

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