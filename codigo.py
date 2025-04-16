import spacy
import json
from spacy.training.example import Example
'''
nlp = spacy.load("pt_core_news_lg")

doc = nlp('As ações da Magazine Luiza S.A. são azuis, Franca, Brasil é amarelo, acumularam baixa de 70% ao ano.')

for entidade in doc.ents:
    print("Entidade: ", entidade.text, " Label: ", entidade.label_)

for token in doc:
  print(token.text)


print("Tokens:           ", [token.text for token in doc])
print("Stop word:        ", [token.is_stop for token in doc])
print("Alfanumérico:     ", [token.is_alpha for token in doc])
print("Maiúsculo:        ", [token.is_upper for token in doc])
print("Pontuação:        ", [token.is_punct for token in doc])
print("Número:           ", [token.like_num for token in doc])
print("Sentença Inicial: ", [token.is_sent_start for token in doc])



print("Tokens:  ", [token.text for token in doc])
print("Formato: ", [token.shape_ for token in doc])


#doc = nlp('As ações da Magazine Luiza S.A., Franca, Brasil, acumularam baixa de 70% ao ano.')

for entidade in doc.ents:
  print("Entidade: ", entidade.text, " Label: ", entidade.label_)
'''
# Carregue o modelo pré-treinado em português
nlp = spacy.blank('pt')

# Defina as classes de rótulo
LABELS = ["VIDEO_GAME"]

ner = nlp.add_pipe("ner")  # Adicionar componente NER
if not ner:
    ner = nlp.create_pipe("ner")
    nlp.add_pipe(ner, last=True)

for label in LABELS:
    ner.add_label(label)


TRAIN_DATA = {
    "classes":["VIDEO_GAME"],
    "annotations":[
        ["Elden Ring foi Aclamado o melhor jogo do ano de 2022.",{"entities":[[0, 10, "VIDEO_GAME"]]}],
        ["Super Mario Bros eu adoro jogar.", {"entities": [[0, 16, "VIDEO_GAME"]]}],
        ["Red Dead Redemption você já jogou esse jogo?", {"entities": [[0, 19, "VIDEO_GAME"]]}],
        ["Minecraft é um dos jogos mais vendidos.", {"entities": [[0,11, "VIDEO_GAME"]]}],
        ["FIFA 21 traz muitas melhorias para o modo carreira.", {"entities": [[0, 7, "VIDEO_GAME"]]}],
        ["The Witcher 3 tem uma narrativa incrível.", {"entities": [[0, 13, "VIDEO_GAME"]]}],
        ["Call of Duty é um jogo de tiro muito famoso.", {"entities": [[0, 12, "VIDEO_GAME"]]}],
        ["Valorant tem uma jogabilidade de tiro tático.", {"entities": [[0, 8, "VIDEO_GAME"]]}],
        ["League of Legends é um jogo de estratégia em tempo real.", {"entities": [[0, 17, "VIDEO_GAME"]]}],
        ["Cyberpunk 2077 tem um mundo aberto impressionante.", {"entities": [[0, 14, "VIDEO_GAME"]]}],
        ["Assassin's Creed Valhalla é sobre vikings.", {"entities": [[0, 25, "VIDEO_GAME"]]}],
        ["Dark Souls é conhecido pela sua dificuldade.", {"entities": [[0, 10, "VIDEO_GAME"]]}],
        ["Pokémon GO é um jogo de realidade aumentada.", {"entities": [[0, 10, "VIDEO_GAME"]]}],
        ["Horizon Zero Dawn é um dos melhores jogos de ação.", {"entities": [[0, 17, "VIDEO_GAME"]]}],
        ["Overwatch é um jogo de tiro com heróis.", {"entities": [[0, 9, "VIDEO_GAME"]]}],
        ["The Elder Scrolls V: Skyrim é um clássico dos RPGs.", {"entities": [[0, 27, "VIDEO_GAME"]]}],
        ["Animal Crossing: New Horizons foi um sucesso em 2020.", {"entities": [[0, 29, "VIDEO_GAME"]]}],
        ["Final Fantasy VII Remake é um jogo de RPG épico.", {"entities": [[0, 24, "VIDEO_GAME"]]}],
        ["Among Us se tornou um fenômeno no mundo dos jogos.", {"entities": [[0, 8, "VIDEO_GAME"]]}],
        ["Tetris é um dos jogos mais jogados da história.", {"entities": [[0, 6, "VIDEO_GAME"]]}],
        ["Doom Eternal é um jogo de ação e tiro em primeira pessoa.", {"entities": [[0, 12, "VIDEO_GAME"]]}],
        ["Gran Turismo Sport tem gráficos incríveis.", {"entities": [[0, 18, "VIDEO_GAME"]]}],
        ["GTA V é um dos jogos mais vendidos de todos os tempos.", {"entities": [[0, 5, "VIDEO_GAME"]]}],
        ["Sekiro: Shadows Die Twice ganhou o prêmio de Jogo do Ano de 2019.", {"entities": [[0,25, "VIDEO_GAME"]]}],
        ["No Minecraft, você pode construir e explorar mundos.", {"entities": [[3, 12, "VIDEO_GAME"]]}],
        ["Assassin's Creed Odyssey foi lançado em 2018.", {"entities": [[0, 24, "VIDEO_GAME"]]}],
        ["Doom Eternal é um jogo de ação frenética.", {"entities": [[0, 12, "VIDEO_GAME"]]}],
        ["Grand Theft Auto V tem um mapa vasto e detalhado.", {"entities": [[0, 18, "VIDEO_GAME"]]}],
        ["Overwatch 2 promete novos heróis e mapas.", {"entities": [[0, 9, "VIDEO_GAME"]]}],
        ["Tetris é um clássico que nunca sai de moda.", {"entities": [[0, 6, "VIDEO_GAME"]]}],
        ["A série Final Fantasy sempre impressiona os fãs.", {"entities": [[8, 21, "VIDEO_GAME"]]}],
        ["Stardew Valley é ótimo jogo para relaxar.", {"entities": [[0, 14, "VIDEO_GAME"]]}],
        ["Street Fighter V é famoso pelas suas batalhas intensas.", {"entities": [[0, 16, "VIDEO_GAME"]]}],
        ["Minecraft tem várias atualizações que adicionam novas funcionalidades.", {"entities": [[0, 9, "VIDEO_GAME"]]}],
        ["Call of Duty é uma série de jogo conhecida por seus modos multiplayer.", {"entities": [[0, 12, "VIDEO_GAME"]]}],
        ["FIFA 22 trouxe várias melhorias para o modo Ultimate Team.", {"entities": [[0, 7, "VIDEO_GAME"]]}],
        ["Valorant é um jogo de tiro tático que ganhou muitos fãs.", {"entities": [[0, 8, "VIDEO_GAME"]]}],
        ["The Witcher 3: Wild Hunt é um dos melhores RPGs de todos os tempos.", {"entities": [[0, 24, "VIDEO_GAME"]]}],
        ["Pokémon é uma franquia que sempre lança novos jogos todo ano.", {"entities": [[0, 7, "VIDEO_GAME"]]}],
        ["League of Legends é um dos jogos mais jogados do mundo.", {"entities": [[0, 17, "VIDEO_GAME"]]}],
        ["Red Dead Redemption 2 conta uma história emocionante.", {"entities": [[0, 21, "VIDEO_GAME"]]}],
        ["Cyberpunk 2077 teve muitos problemas no seu lançamento.", {"entities": [[0, 14, "VIDEO_GAME"]]}],
        ["Mario Kart 8 Deluxe é um dos melhores jogos de corrida.", {"entities": [[0, 19, "VIDEO_GAME"]]}],
        ["Horizon Zero Dawn tem um mundo aberto fascinante.", {"entities": [[0, 17, "VIDEO_GAME"]]}],
        ["Pokémon Sword and Shield introduziu novas mecânicas de jogo.", {"entities": [[0, 24, "VIDEO_GAME"]]}],
        ["Dragon Age: Inquisition é um RPG de fantasia épico.", {"entities": [[0, 23, "VIDEO_GAME"]]}],
        ["The Elder Scrolls V: Skyrim é um jogo de mundo aberto incrível.", {"entities": [[0, 27, "VIDEO_GAME"]]}],
        ["Fortnite é um dos jogos mais populares da atualidade.", {"entities": [[0, 8, "VIDEO_GAME"]]}],
        ["Resident Evil 2 Remake é um excelente jogo de survival horror.", {"entities": [[0, 22, "VIDEO_GAME"]]}],
        ["Persona 5 Royal é uma versão expandida do jogo original.", {"entities": [[0, 15, "VIDEO_GAME"]]}],
        ["Call of Duty: Warzone é um jogo Battle Royale muito jogado.", {"entities": [[0, 21, "VIDEO_GAME"]]}],
        ["Minecraft Dungeons é uma nova aventura no universo de Minecraft.", {"entities": [[0, 18, "VIDEO_GAME"]]}],
        ["Rocket League mistura futebol e carros.", {"entities": [[0, 13, "VIDEO_GAME"]]}],
        ["The Last of Us Part II foi um dos maiores lançamentos de 2020.", {"entities": [[4, 22, "VIDEO_GAME"]]}],
        ["Assassin's Creed Valhalla se passa na época dos vikings.", {"entities": [[0, 25, "VIDEO_GAME"]]}],
        ["Battlefield V teve um grande foco na Segunda Guerra Mundial.", {"entities": [[0, 13, "VIDEO_GAME"]]}],
        ["Uncharted 4: A Thief's End tem uma história empolgante.", {"entities": [[0, 26, "VIDEO_GAME"]]}],
        ["Dark Souls III é conhecido pela sua dificuldade.", {"entities": [[0, 14, "VIDEO_GAME"]]}],
        ["Halo Infinite promete revolucionar a série.", {"entities": [[0, 13, "VIDEO_GAME"]]}],
        ["Dead by Daylight é um jogo de terror multiplayer.", {"entities": [[0, 16, "VIDEO_GAME"]]}],
        ["Mortal Kombat 11 trouxe novos personagens e cenários.", {"entities": [[0, 16, "VIDEO_GAME"]]}],
        ["God of War é um dos maiores sucessos do PlayStation.", {"entities": [[0, 10, "VIDEO_GAME"]]}],
        ["Gears of War 5 tem uma campanha empolgante.", {"entities": [[0, 14, "VIDEO_GAME"]]}],
        ["Animal Crossing: New Horizons foi um grande sucesso em 2020.", {"entities": [[0, 29, "VIDEO_GAME"]]}],
        ["The Sims 4 tem diversas expansões e conteúdos adicionais.", {"entities": [[0, 10, "VIDEO_GAME"]]}],
        ["Splatoon 2 é um jogo divertido de tiro multiplayer.", {"entities": [[0, 10, "VIDEO_GAME"]]}],
        ["Nier: Automata tem uma história única e fascinante.", {"entities": [[0, 14, "VIDEO_GAME"]]}],
        ["Street Fighter IV foi um dos melhores jogos de luta da década.", {"entities": [[0, 17, "VIDEO_GAME"]]}],
        ["Final Fantasy XV tem um mundo aberto gigantesco.", {"entities": [[0, 16, "VIDEO_GAME"]]}],
        ["Dark Souls: Remastered trouxe a versão clássica para novas gerações.", {"entities": [[0, 22, "VIDEO_GAME"]]}],
        ["The Legend of Zelda: Ocarina of Time é um clássico do Nintendo 64.", {"entities": [[0, 36, "VIDEO_GAME"]]}],
        ["Kingdom Hearts III é a continuação de uma das sagas mais amadas.", {"entities": [[0, 18, "VIDEO_GAME"]]}],
        ["Bloodborne tem uma atmosfera sombria e envolvente.", {"entities": [[0, 10, "VIDEO_GAME"]]}],
        ["Shadow of the Tomb Raider é uma ótima adição à série.", {"entities": [[0, 25, "VIDEO_GAME"]]}],
        ["Celeste é um dos jogos de plataforma mais desafiadores.", {"entities": [[0, 7, "VIDEO_GAME"]]}],
        ["Bioshock Infinite tem uma narrativa impressionante.", {"entities": [[0, 17, "VIDEO_GAME"]]}],
        ["Portal 2 é um dos melhores jogos de quebra-cabeças.", {"entities": [[0, 8, "VIDEO_GAME"]]}],
        ["Minecraft: Education Edition é uma versão focada no aprendizado.", {"entities": [[0, 28, "VIDEO_GAME"]]}],
        ["Little Nightmares é um jogo de aventura e terror.", {"entities": [[0, 17, "VIDEO_GAME"]]}],
        ["Forza Horizon 4 é um excelente jogo de corrida.", {"entities": [[0, 15, "VIDEO_GAME"]]}],
        ["Sea of Thieves permite explorar um vasto mundo pirata.", {"entities": [[0, 14, "VIDEO_GAME"]]}],
        ["Sonic the Hedgehog é o mascote da SEGA.", {"entities": [[0, 18, "VIDEO_GAME"]]}],
        ["The Division 2 é um jogo de tiro com elementos de RPG.", {"entities": [[0, 14, "VIDEO_GAME"]]}],
        ["Watch Dogs: Legion permite jogar como qualquer NPC.", {"entities": [[0, 18, "VIDEO_GAME"]]}],
        ["Tava entre pegar Elden Ring ou sei lá, aquele da CD Projekt, o Cyberpunk.", {"entities": [[17, 27, "VIDEO_GAME"], [63, 73, "VIDEO_GAME"]]}],


    ]
}

# Converta os dados de treinamento em exemplos do spaCy
examples = []
for annotation in TRAIN_DATA.get('annotations', []):
    text = annotation[0]
    entities = annotation[1].get('entities', [])
    example = Example.from_dict(nlp.make_doc(text), {"entities": entities})
    examples.append(example)

# Inicialize e treine o modelo
optimizer = nlp.initialize()

losses = {}

for i in range(30):  # Executar iterações de treinamento
    nlp.update(examples, losses=losses)
    print(f"Iteração {i+1}, Perda: {losses}")



# Salve o modelo treinado
nlp.to_disk("modelo_games")

print("Treinamento concluído!")


