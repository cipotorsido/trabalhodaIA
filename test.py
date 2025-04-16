import spacy

modelo_treinado = spacy.load("modelo_games")

texto = (
    "O mundo dos videogames é vasto, criativo e recheado de experiências inesquecíveis. "
    "Desde os tempos de Tetris, que conquistou gerações com sua simplicidade viciante, até a complexidade sombria de Elden Ring, "
    "eleito o melhor jogo de 2022, os games têm evoluído de formas surpreendentes."
    "Quem nunca se divertiu com a leveza de Super Mario Bros ou acelerou nas pistas caóticas de Mario Kart 8 Deluxe? "
    "Para os fãs de aventuras mais intensas, The Witcher 3: Wild Hunt e Red Dead Redemption 2 oferecem histórias profundas e mundos ricos em detalhes. "
    "E por falar em mundos abertos, não podemos esquecer de The Elder Scrolls V: Skyrim, Cyberpunk 2077 e Horizon Zero Dawn, "
    "que redefiniram o conceito de exploração virtual."
)

doc = modelo_treinado(texto)

# Imprime todas as entidades
for entidade in doc.ents:
    print(entidade.text, entidade.label_)

# Coleta só os jogos reconhecidos
jogos_identificados = [
    entidade.text for entidade in doc.ents if entidade.label_ == "VIDEO_GAME"
]

# Lista esperada
jogos_esperados = [
    "Tetris",
    "Elden Ring",
    "Super Mario Bros",
    "Mario Kart 8 Deluxe",
    "The Witcher 3: Wild Hunt",
    "Red Dead Redemption 2",
    "The Elder Scrolls V: Skyrim",
    "Cyberpunk 2077",
    "Horizon Zero Dawn"
]

# Calcula porcentagem
def calcular_porcentagem_acerto(jogos_esperados, jogos_identificados):
    acertos = 0
    for jogo in jogos_identificados:
        if jogo in jogos_esperados:
            acertos += 1

    total_identificados = len(jogos_identificados)
    if total_identificados == 0:
        return 0.0  # Evita divisão por zero

    porcentagem = (acertos / total_identificados) * 100
    return round(porcentagem, 2)

porcentagem = calcular_porcentagem_acerto(jogos_esperados, jogos_identificados)
print(f"Porcentagem de acerto: {porcentagem}%")

