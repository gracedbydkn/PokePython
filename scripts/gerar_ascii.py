import json
import subprocess
import os

with open("data/pokemons.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

for p in dados ["pokemon"]:
    nome = p["nome"]

    resultado = subprocess.run(
        ["pokemon", "--pokemon", nome],
        capture_output=True,
        text=True
    )

    ascii_art = resultado.stdout
    p["ascii"] = ascii_art.splitlines()
    print(f"ASCII gerado: {nome}")

with open("data/pokemons.json", "w", encoding="utf-8") as f:
    json.dump(dados, f, ensure_ascii=False, indent=2)

print("ASCIIs gerados!")