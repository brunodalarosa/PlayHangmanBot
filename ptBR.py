#-*- coding: utf-8 -*-
#Linguagem Português, contém as strings que serão lidas para aparecerem no jogo

#Emojis
from emojis import *

#palavras
palavras = [
                ['Animail ou espécie', 'macaco', 'elefante','zebra','papagaio','andorinha','golfinho','gorila','tubarao','lobo','ornitorrinco','cavalo','humano','lebre','coelho','periquito','pomba','dinossauro','macaco','borboleta','Baleia', 'Cachorro', 'Cobra', 'Crocodilo', 'Frango', 'Galinha', 'Gambá', 'Gato', 'Leão', 'Girafa', 'Ovelha', 'Polvo', 'Rinocerontes', 'Tartarugas', 'Touro', 'Ursos', 'Vaca','Lontra', 'Onça', 'Porco', 'Urubú', 'Camelo', 'Cascavel', 'Burro'],
                ['Fruta', 'Abacate', 'Amora', 'Ameixa', 'Acerola', 'Abacaxi', 'Açaí', 'Banana', 'Carambola', 'Caju', 'Cereja', 'Cacau', 'Caqui', 'Cupuaçu', 'Damasco', 'Figo', 'Framboesa', 'Graviola', 'Goiaba', 'Groselha', 'Guaraná', 'Jaca', 'Jabuticaba', 'Kiwi', 'Laranja', 'Limão', 'Melancia', 'Mamão', 'Melão', 'Maracujá', 'Manga', 'Maçã', 'Pera', 'Pêssego', 'Tangerina', 'Tomate', 'Tamarindo', 'Uva'],
                ['Comidas salgados ou doces','Macarrão instantâneo','cachorro quente','lasanha','frango a passarinho','batata frita','ketchup','chocolate','strogonoff','arroz e feijão','batata doce','pizza','sushi','temaki','fondue de chocolate','bolo','kitkat','pirulito','algodão doce','Escondidinho de carne seca','Torta de limão','Panqueca','Feijoada'],
                ['Profissão', 'advogado', 'professor', 'zelador','prostituta','médico','marceneiro','designer','desenvolvedor de jogos','dublador','escritor','cozinheiro','pedreiro','vendedor','gerente','caminhoneiro','taxista','pintor','mecânico','auxiliar','estagiário','carteiro','cirurgião','oftalmologista','analista de sistemas','empresário','piloto','bancário','jardineiro','fotógrafo','escrivão','juiz','delegado','soldado','sargento','xerife','engenheiro','mestre de obras','tradutor','farmacêutico','veterinário','costureiro','recepcionista','cientista','político','encanador','eletricista','massoterapeuta','garçom'],
                ['Relacionado a Computador/Internet/Programação', 'programador','compilador','servidor','monitor','algoritmo','netflix','orkut','instagram','tumblr','twitter','rede neural','google','photoshop','wolfram alpha','python','java','framework','ruby','javascript','latex','android','stack overflow','wikipedia','debugging'],
                ['Pessoa importante (ex: Presidente ou cientista)','albert einstein','barack obama','abraham lincoln','nikola tesla','carl sagan','larry page','steves jobs','mark zuckerberg','tim cook','charles chaplin','platao','aristoteles','dilma rousseff','luiz inacio lula da silva','fernando herinque cardoso','george washington','george walker bush','adolf hitler','shigeru miyamoto','Neil deGrasse Tyson'],
                ['Cidade do mundo','brasília','curitiba','maringá','nova iorque','tokio','barcelona','amsterdã','paris','milão','pequim','berlim','são paulo','rio de janeiro','salvador','manaus','rio branco','orlando','los angeles','calgary','toronto','montreal','dallas','londres','cuiabá','macheral cândido rondon','campo mourão','toledo','Cascavel','Ouro preto'],
                ['Herói ou vilão do mundo das HQ/cinema (DC e Marvel)','batman','flash','mulher maravilha','pinguim','super Homem','lanterna verde','duende verde','homem aranha','thor','hulk','homem de ferro','homem formiga','tocha humana','o coisa','viuva negra','arqueiro verde','groot','rocket raccoon','magneto','wolverine','tempestade'],
                ['Videogame ou game','the legend of zelda','super mario','counter strike','nintendo wii','super nintendo','playstation','steam','defense of the ancients','league of legends','final fantasy','donkey kong','angry birds','fallout','bioshock','tetris','the elders scroll','minecraft','call of duty','battlefield','bomberman','sonic','just dance','nintendo','sony','sega','dreamcast'],
                ['Título ou nome (Ator ou personagem) relacionado a TV e Cinema!', 'Breaking bad','how i met your mother','sense8','netflix','beleza americana','donnie Darko','esqueceram de mim','o sexto sentido','o iluminado','titanic','todo mundo odeia o cris','chapeleiro maluco','alice no país das maravilhas','harry potter','hora de aventura','bob esponja','Narcos','Segurando as pontas','Pokémon','Yugioh','Hermione','Lord voldemort','Draco Malfoy','Katniss everdeen','Jogos vorazes','A esperança','Em chamas','O exorcista','Sem limites','Se beber não case','Matrix','O Senhor dos anéis','O hobbit','Frodo Baggins','Sauron','Legolas','Gandalf','Albus Dumbledore','Star wars','Luke Skywalker','Chewbacca','Mestre Yoda'],
                ['País', 'brasil', 'estados Unidos', 'alemanha', 'japão', 'coréia do sul', 'áfrica do sul', 'holanda', 'argentina', 'espanha', 'chile', 'equador', 'canadá', 'singapura', 'índia', 'emirados árabes', 'itália', 'inglaterra', 'áustria', 'grécia', 'república Checa','austrália','madagáscar','rússia','china','méxico','colômbia','etiópia','bolívia'],
                ['Pokémon 1st Gen','Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard', 'Squirtle', 'Wartortle', 'Blastoise', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill', 'Pidgey', 'Pidgeotto', 'Pidgeot', 'Rattata', 'Raticate', 'Spearow', 'Fearow', 'Ekans', 'Arbok', 'Pikachu', 'Raichu', 'Sandshrew', 'Sandslash', 'Nidoran', 'Nidorina', 'Nidoqueen', 'Nidorino', 'Nidoking', 'Clefairy', 'Clefable', 'Vulpix', 'Ninetales', 'Jigglypuff', 'Wigglytuff', 'Zubat', 'Golbat', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 'Venonat', 'Venomoth', 'Diglett', 'Dugtrio', 'Meowth', 'Persian', 'Psyduck', 'Golduck', 'Mankey', 'Primeape', 'Growlithe', 'Arcanine', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Abra', 'Kadabra', 'Alakazam', 'Machop', 'Machoke', 'Machamp', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Tentacool', 'Tentacruel', 'Geodude', 'Graveler', 'Golem', 'Ponyta', 'Rapidash', 'Slowpoke', 'Slowbro', 'Magnemite', 'Magneton', 'Doduo', 'Dodrio', 'Seel', 'Dewgong', 'Grimer', 'Muk', 'Shellder', 'Cloyster', 'Gastly', 'Haunter', 'Gengar', 'Onix', 'Drowzee', 'Hypno', 'Krabby', 'Kingler', 'Voltorb', 'Electrode', 'Exeggcute', 'Exeggutor', 'Cubone', 'Marowak', 'Hitmonlee', 'Hitmonchan', 'Lickitung', 'Koffing', 'Weezing', 'Rhyhorn', 'Rhydon', 'Chansey', 'Tangela', 'Kangaskhan', 'Horsea', 'Seadra', 'Goldeen', 'Seaking', 'Staryu', 'Starmie', 'Mr.', 'Mime', 'Scyther', 'Jynx', 'Electabuzz', 'Magmar', 'Pinsir', 'Tauros', 'Magikarp', 'Gyarados', 'Lapras', 'Ditto', 'Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Porygon', 'Omanyte', 'Omastar', 'Kabuto', 'Kabutops', 'Aerodactyl', 'Snorlax', 'Articuno', 'Zapdos', 'Moltres', 'Dratini', 'Dragonair', 'Dragonite', 'Mewtwo', 'Mew'],
            ]

#Botões dos Keyboards
novojogo = 'Novo Jogo' + emoji_joystick
ajuda = 'Ajuda' + emoji_light
rank = 'Rank' + emoji_trofeu
ligar = 'Ligar' + emoji_foguete
desligar = 'Desligar' + emoji_x
config = 'Configurações' + emoji_ferramenta
voltar = 'Voltar' + emoji_back
cancelar = 'Cancelar' + emoji_x
comandos = 'Comandos' + emoji_light
entrar = 'Entrar' + emoji_foguete
sair = 'Sair' + emoji_x
fechar_jogo = 'Começar jogo' + emoji_foguete
cancelar_jogo = 'Cancelar jogo' + emoji_x
arriscar = 'Arriscar' + emoji_gritar
esta_fora = 'Você está fora desse jogo' + emoji_proibido

#Respostas iniciais
linguas = emoji_planeta + 'Escolha a linguagem:'
iniciar_msg = 'Carregando...'
mudar_lingua = 'Mudança feita com sucesso' + emoji_thumbsUp
start_msg = 'Olá, eu sou o Hangman, mestre de jogos da forca! Meu dever é organizar e jogar jogos da forca e garantir que você se divirta!\nAperte no botão "novo jogo" para começarmos!' + emoji_sorriso
is_enabled = 'Já estou ligado!'
about_msg = 'Sou um projeto de código aberto criado pelo @bcesarg6 e @cristoferoswald! Estou em constante desenvolvimento e você pode me ajudar a crescer contribuindo em github.com/bcesarg6/ccuem_bot'
stop_msg = 'Desligado'
start_help_msg = 'Não há nenhum jogo em andamento, clique no botão "novo jogo" para começar um jogo ou veja o ranking no botão "Rank".\nVocê também pode alterar as configurações se desejar' + emoji_sorriso + '\nLembre-se se você precisar do telcado envie /kb'
config_help_msg = 'Escolha a minha lingua. ATENÇÃO: As palavras do jogo dependem da língua escolhida\nNão encontrou sua lingua? Você pode ajudar no meu desenvolvimento adicionando uma tradução :)\nLembre-se se você precisar do telcado envie /kb'
voltar_msg = 'Menu inicial'
cantdo_msg = 'Você não pode fazer isso'
comandos_msg = 'Comandos'
ocupado_msg = 'Estou ocupado agora, desculpe' + emoji_triste
teclado_msg = 'Teclado'
ranking_msg = emoji_coroa + ' RANKING ' + emoji_coroa

#respostas PreGame
def inicialMsg(u_name):
    return 'Começando um novo jogo!\n'+u_name+' será o administrador dessa rodada.' + emoji_oculos

inicial_msg = 'Vamos começar definindo os jogadores, quem quiser participar clique em Entrar'+emoji_sorriso
close_game_msg = 'O jogo vai começar! Na sua vez, clique nas letras para chutar ou clique em arriscar e me mande a palavra completa se você acha que já a descobriu, mas cuidado, não tem volta!'+emoji_zoando+'\nVocês jogarão nesta ordem:'
palavra_msg = 'A palavra é: '
categoria_msg = 'Categoria: '
esta_dentro_msg = 'Você já participa desta partida'
sem_jogador_msg = 'Todos os jogadores sairam, o jogo será cancelado' + emoji_surpreso
cancelar_jogo_msg = 'Jogo cancelado pelo administrador'
is_out_msg = 'Você não participa desse jogo' + emoji_lua
vidas_msg = 'Vidas: '
pre_game_help_msg = 'Jogo em modo de entrada, clique em Entrar para participar\nADM: Clique em Fechar Jogo para começar o jogo com os participantes atuais'

def novoAdmMsg(u_name):
    return 'Um novo administrador foi definido! '+u_name+' é o novo administrador.' + emoji_oculos

def playerQuitMsg(u_name):
    return 'O jogador '+u_name+' saiu da partida.' + emoji_triste

def entrarMsg(u_name):
    return 'Ok '+u_name+', você vai participar dessa rodada' + emoji_blink

#repostas InGame
in_game_help_msg = 'Clique nas letras para chuta-las ou em Arriscar se você acha que já descobriu a palavra secreta! se quiser mais opções clique em Comandos' + '\nLembre-se se você precisar do telcado envie /kb'
arriscar_msg = 'Então você acha que já descobriu qual é a palavra? ' + emoji_zoando + ' Me mande a palavra, mas pense bem, se você errar será eliminado!' + emoji_lua
round_errado_msg = 'Não é a sua vez de jogar, espere a sua vez!' + emoji_lua
acertou_letra_msg = 'Você acertou!' + emoji_claps
errou_letra_msg = 'Errou' + emoji_triste + emoji_heartb
jachutada_msg = 'Essa letra já foi chutada' + emoji_surpreso
umavida_msg = 'Somente uma vida restante! Descubra a palavra ou aceite sua DERROTA!' + emoji_lua
gameover_msg = emoji_poop + ' PERDERAM, FIM DE JOGO ' + emoji_poop
fora_msg = 'Você não participa dessa rodada, espere ela acabar para participar de um novo'

def perdeu(u_name):
    return u_name + ' arriscou e errou! O jogador foi eliminado!' + emoji_lua

def nextPlayer(u_name):
    return 'Vez de ' + u_name + ' ' + emoji_point

def venceu(u_name):
    return emoji_confetti + ' Parabéns ' + u_name + ' você descobriu a palavra secreta e ganhou o jogo! ' + emoji_confetti + '\n Pontos calculados e ranking atualizado! ' + emoji_sorriso
