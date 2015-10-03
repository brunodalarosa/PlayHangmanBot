#-*- coding: utf-8 -*-
#Linguagem Inglês, contém as strings que serão lidas para aparecerem no jogo

#Emojis
from emojis import *

#palavras
palavras = [
['Fruits', 'Açai Berries', 'Apple', 'Apricot', 'Avocado', 'Banana', 'Bilberry', 'Blackberry', 'Blackcurrant', 'Blueberry', 'Boysenberry', 'Cantaloupe',
'Currant', 'Cherry', 'Cherimoya', 'Cloudberry', 'Coconut', 'Cranberry', 'Damson','Dragonfruit', 'Durian', 'Elderberry', 'Feijoa', 'Fig', 'Goji berry', 'Gooseberry', 'Grape', 'Raisin', 'Grapefruit', 'Guava',
'Huckleberry','Jabouticaba','Jackfruit','Jambul','Jujube','Juniper berry','Kiwi fruit','Kiwano','Kumquat','Lemon','Lime','Loquat','Lychee','Mango','Marion berry','Melon','Cantaloupe','Honeydew','Watermelon','Miracle fruit','Mulberry',
'Nectarine','Olive','Orange','Blood Orange','Clementine','Mandarine','Tangerine','Papaya','Passionfruit','Peach','Pear','Persimmon','Physalis','Pineapple','Pumpkin','Pomegranate','Pomelo','Purple Mangosteen','Quince','Raspberry','Salmon berry',
'Black raspberry','Rambutan','Redcurrant','Salal berry','Satsuma','Star fruit','Strawberry','Squash','Tamarillo','Tomato','Ugli fruit'],
['Countries', 'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan',
'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burundi',
'Cambodia', 'Cameroon', 'Canada', 'Chile', 'China', 'Colombia', 'Republic of the Congo', 'Costa Rica', 'Croatia', 'Cuba', 'CzechRepublic',
'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Guatemala', 'Guinea', 'Guyana',
'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Portugal', 'Paraguay', 'New Zealand', 'Mexico', 'Madagascar', 'Peru', 'Russia', 'Serbia', 'Spain', 'Sudan', 'Sweden'],
['Professions', 'Accountant', 'Actor', 'Architect', 'Astronomer', 'Author', 'Baker', 'Bricklayer', 'Butcher', 'Carpenter', 'Cook', 'Cleaner', 'Dentist', 'Designer', 'Doctor', 'Electrician', 'Engineer', 'Farmer', 'Fireman', 'Fisherman', 'Florist', 'Gardener', 'Hairdresser', 'Journalist', 'Judge', 'Lawyer', 'Lecturer', 'Librarian', 'Lifeguard', 'Mechanic', 'Model', 'Newsreader', 'Nurse', 'Optician', 'Painter', 'Pharmacist', 'Photographer', 'Pilot', 'Plumber', 'Politician', 'Policeman',
 'Postman', 'Receptionist', 'Scientist', 'Secretary', 'Shopassistant', 'Soldier', 'Tailor', 'Taxidriver', 'Teacher', 'Translator', 'Travelagent', 'Veterinary', 'Waiter'],
['Hero or villain of DC or Marvel','batman','flash','wonder women','penguin','super man','grenn lantern','grenn goblin','spider man','thor','hulk','iron man','ant man','human torch','the thing','black window','green arrow','groot','rocket raccoon','magneto','wolverine','storm'],
['Videogame or game','the legend of zelda','super mario','counter strike','nintendo wii','super nintendo','playstation','steam','defense of the ancients','league of legends','final fantasy','donkey kong','angry birds','fallout','bioshock','tetris','the elders scroll','minecraft','call of duty','battlefield','bomberman','sonic the hedgehog','just dance','nintendo','sony','sega','dreamcast'],
['Important people (ex: President ou scientist)','albert einstein','barack obama','abraham lincoln','nikola tesla','carl sagan','larry page','steves jobs','mark zuckerberg','tim cook','charles chaplin','platao','aristoteles','dilma rousseff','luiz inacio lula da silva','fernando herinque cardoso','george washington','george walker bush','adolf hitler','shigeru miyamoto','Neil deGrasse Tyson'],
['Titles or names (actor or character) relacioned to TV or cinema!', 'breaking bad', 'how i met your mother','sense8', 'american beauty','donnie Darko','home alone','the sixth sense','the shinning','titanic','everybody hates chris','the mad hatter','alice in the worderland','harry potter','adventure time','spongebob','Narcos','pineapple express','Pokémon','Yugioh','Hermione','Lord voldemort','Draco Malfoy','Katniss everdeen','hunger gamse','Mockingjay','cathing fire','exorcist','limitless','the hangover','Matrix','the lord of rings','The hobbit','Frodo Baggins','Sauron','Legolas','Gandalf','Albus Dumbledore','Star wars','Luke Skywalker','Chewbacca', 'Yoda'],
['Pokémon 1st Gen','Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard', 'Squirtle', 'Wartortle', 'Blastoise', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill', 'Pidgey', 'Pidgeotto', 'Pidgeot', 'Rattata', 'Raticate', 'Spearow', 'Fearow', 'Ekans', 'Arbok', 'Pikachu', 'Raichu', 'Sandshrew', 'Sandslash', 'Nidoran', 'Nidorina', 'Nidoqueen', 'Nidorino', 'Nidoking', 'Clefairy', 'Clefable', 'Vulpix', 'Ninetales', 'Jigglypuff', 'Wigglytuff', 'Zubat', 'Golbat', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 'Venonat', 'Venomoth', 'Diglett', 'Dugtrio', 'Meowth', 'Persian', 'Psyduck', 'Golduck', 'Mankey', 'Primeape', 'Growlithe', 'Arcanine', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Abra', 'Kadabra', 'Alakazam', 'Machop', 'Machoke', 'Machamp', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Tentacool', 'Tentacruel', 'Geodude', 'Graveler', 'Golem', 'Ponyta', 'Rapidash', 'Slowpoke', 'Slowbro', 'Magnemite', 'Magneton', 'Doduo', 'Dodrio', 'Seel', 'Dewgong', 'Grimer', 'Muk', 'Shellder', 'Cloyster', 'Gastly', 'Haunter', 'Gengar', 'Onix', 'Drowzee', 'Hypno', 'Krabby', 'Kingler', 'Voltorb', 'Electrode', 'Exeggcute', 'Exeggutor', 'Cubone', 'Marowak', 'Hitmonlee', 'Hitmonchan', 'Lickitung', 'Koffing', 'Weezing', 'Rhyhorn', 'Rhydon', 'Chansey', 'Tangela', 'Kangaskhan', 'Horsea', 'Seadra', 'Goldeen', 'Seaking', 'Staryu', 'Starmie', 'Mr.', 'Mime', 'Scyther', 'Jynx', 'Electabuzz', 'Magmar', 'Pinsir', 'Tauros', 'Magikarp', 'Gyarados', 'Lapras', 'Ditto', 'Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Porygon', 'Omanyte', 'Omastar', 'Kabuto', 'Kabutops', 'Aerodactyl', 'Snorlax', 'Articuno', 'Zapdos', 'Moltres', 'Dratini', 'Dragonair', 'Dragonite', 'Mewtwo', 'Mew']
        ]

categorias = ''
for i in range(len(palavras)):
    categorias = categorias+palavras[i][0]+'\n'

#Botões dos Keyboards
novojogo = 'New Game' + emoji_joystick
ajuda = 'Help' + emoji_light
rank = 'Rank' + emoji_trofeu
ligar = 'Start' + emoji_foguete
desligar = 'Stop' + emoji_x
config = 'Settings' + emoji_ferramenta
voltar = 'Back' + emoji_back
cancelar = 'Cancel' + emoji_x
comandos = 'Commands' + emoji_light
entrar = 'Join' + emoji_foguete
sair = 'Quit' + emoji_x
fechar_jogo = 'Start Game' + emoji_foguete
cancelar_jogo = 'Cancel game' + emoji_x
arriscar = 'Risk!' + emoji_gritar
esta_fora = 'You are out of this game' + emoji_proibido
sobre = 'About' + emoji_livro

#Respostas iniciais
linguas = emoji_planeta + 'Choose a language:'
iniciar_msg = 'Loading...'
mudar_lingua = 'Change successful' + emoji_thumbsUp
start_msg = 'Hi, i am the Hangman, master of Hangman games! My duty is to organize and play Hangman games with you and your friends and ensure that we will have fun!\n Press the "new game" button and we shall begin!' + emoji_sorriso
is_enabled = 'Im already ready!'
stop_msg = 'Turning off'
about_msg = 'I am a Open Source project created by @bcesarg6 and @cristoferoswald! Im in constant development and you can help me grown up coding at github.com/bcesarg6/PlayHangmanBot\n\nCategories:\n'+categorias+'\nVersion 1.0:\n\t- First oficial launching version\n\nFuture updates:\n\t- Category and words about the games League of legends and Dota2\n\t- Kick player system\n\t- Word category selection\n\t- Global ranking\n\nFeel free to join the team!' + emoji_sorriso
start_help_msg = 'There is no game happening right now, press the button "new game" to start one or press "Rank" to see the ranking.\n You can also change the settings if you want to' + emoji_sorriso + '\nRemember, if anytime you need a keyboard send me the command /kb'
config_help_msg = 'Choose the language you want. The secret words of the game depends on the selected language\nDid not find your language? You can help my development by making your own translations! Press the About button for more information.\nRemember, if anytime you need a keyboard send me the command /kb'
voltar_msg = 'Main menu'
cantdo_msg = 'You cant do this'
comandos_msg = 'Commands'
ocupado_msg = 'I am busy right now, sorry' + emoji_triste
teclado_msg = 'Keyboard'
ranking_msg = emoji_coroa + ' RANKING ' + emoji_coroa
error_msg = 'An error occurred please contact @cristoferoswald or @bcesarg6 and report it' + emoji_triste
sorry_msg = 'Sorry, what did you say?'

#respostas PreGame
def inicialMsg(u_name):
    return 'Starting a new game! \n'+u_name+' will the admin of this game.' + emoji_oculos

inicial_msg = 'Lets begin defining the players, who wants to enter press the "Enter" button!'+emoji_sorriso
close_game_msg = 'The game will begin! In your turn press a letter to guess it or press "Risk" if you think that already discovered the secret word, but be careful, there is no way back!'+emoji_zoando+'\n We will play in this order:'
palavra_msg = 'The secret word: '
categoria_msg = 'Category: '
esta_dentro_msg = 'You already in this game!'
sem_jogador_msg = 'All the players quited, the game will be canceled! ' + emoji_surpreso
cancelar_jogo_msg = 'Game canceled by the admin'
is_out_msg = 'You are not in this game' + emoji_lua
vidas_msg = 'Lifes: '
pre_game_help_msg = 'I am waiting for people to join the game, press "Enter" to join \nAdmin: Press "Start game" to begin the game with this players'

def novoAdmMsg(u_name):
    return 'A new admin was selected! '+u_name+' is the new admin.' + emoji_oculos

def playerQuitMsg(u_name):
    return 'The player '+u_name+' quited.' + emoji_triste

def entrarMsg(u_name):
    return 'Ok '+u_name+', you will play in this game' + emoji_blink

#repostas InGame
in_game_help_msg = 'Press the letter to guess them or press "Risk" if you think that already know the secret word!\nRemember, if anytime you need a keyboard send me the command /kb'
arriscar_msg = 'So you think that you know what is the secret word? ' + emoji_zoando + ' Send me the word, but think wisely, if you fail you will be eliminated!' + emoji_lua
round_errado_msg = 'It is not your time to play yet! Wait for your turn!' + emoji_lua
acertou_letra_msg = 'Right letter!' + emoji_claps
errou_letra_msg = 'Wrong letter' + emoji_triste + emoji_heartb
jachutada_msg = 'This letter has already been guessed' + emoji_surpreso
umavida_msg = 'One life left! Discover the secret word or face your DEFEAT!' + emoji_lua
gameover_msg = emoji_poop + ' GAME OVER LOSERS! ' + emoji_poop
fora_msg = 'You are not in this game, wait for this game end to enter in another one!'

def perdeu(u_name):
    return u_name + ' Risked it all and losed! The player was eliminated!' + emoji_lua

def nextPlayer(u_name):
    return 'Turn of ' + u_name + ' ' + emoji_point

def venceu(u_name):
    return emoji_confetti + ' Congratulations ' + u_name + ' you discovered the secret word and won the game! ' + emoji_confetti + '\n Score calculated and ranking updated! ' + emoji_sorriso
