#-*- coding: utf-8 -*-
#Linguagem Hebreu, contém as strings que serão lidas para aparecerem no jogo

#Emojis
from emojis import *

#palavras
palavras = [
['פירות', 'Açai Berries', 'Apple', 'Apricot', 'Avocado', 'Banana', 'Bilberry', 'Blackberry', 'Blackcurrant', 'Blueberry', 'Boysenberry', 'Cantaloupe',
'Currant', 'Cherry', 'Cherimoya', 'Cloudberry', 'Coconut', 'Cranberry', 'Damson','Dragonfruit', 'Durian', 'Elderberry', 'Feijoa', 'Fig', 'Goji berry', 'Gooseberry', 'Grape', 'Raisin', 'Grapefruit', 'Guava',
'Huckleberry','Jabouticaba','Jackfruit','Jambul','Jujube','Juniper berry','Kiwi fruit','Kiwano','Kumquat','Lemon','Lime','Loquat','Lychee','Mango','Marion berry','Melon','Cantaloupe','Honeydew','Watermelon','Miracle fruit','Mulberry',
'Nectarine','Olive','Orange','Blood Orange','Clementine','Mandarine','Tangerine','Papaya','Passionfruit','Peach','Pear','Persimmon','Physalis','Pineapple','Pumpkin','Pomegranate','Pomelo','Purple Mangosteen','Quince','Raspberry','Salmon berry',
'Black raspberry','Rambutan','Redcurrant','Salal berry','Satsuma','Star fruit','Strawberry','Squash','Tamarillo','Tomato','Ugli fruit'],
['ארצות', 'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan',
'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burundi',
'Cambodia', 'Cameroon', 'Canada', 'Chile', 'China', 'Colombia', 'Republic of the Congo', 'Costa Rica', 'Croatia', 'Cuba', 'CzechRepublic',
'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Guatemala', 'Guinea', 'Guyana',
'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Portugal', 'Paraguay', 'New Zealand', 'Mexico', 'Madagascar', 'Peru', 'Russia', 'Serbia', 'Spain', 'Sudan', 'Sweden'],
['מקצועות', 'Accountant', 'Actor', 'Architect', 'Astronomer', 'Author', 'Baker', 'Bricklayer', 'Butcher', 'Carpenter', 'Cook', 'Cleaner', 'Dentist', 'Designer', 'Doctor', 'Electrician', 'Engineer', 'Farmer', 'Fireman', 'Fisherman', 'Florist', 'Gardener', 'Hairdresser', 'Journalist', 'Judge', 'Lawyer', 'Lecturer', 'Librarian', 'Lifeguard', 'Mechanic', 'Model', 'Newsreader', 'Nurse', 'Optician', 'Painter', 'Pharmacist', 'Photographer', 'Pilot', 'Plumber', 'Politician', 'Policeman',
 'Postman', 'Receptionist', 'Scientist', 'Secretary', 'Shopassistant', 'Soldier', 'Tailor', 'Taxidriver', 'Teacher', 'Translator', 'Travelagent', 'Veterinary', 'Waiter'],
['גיבור או נבל בעולם של דיסי או של מארוול','batman','flash','wonder women','penguin','super man','grenn lantern','grenn goblin','spider man','thor','hulk','iron man','ant man','human torch','the thing','black widow','green arrow','groot','rocket raccoon','magneto','wolverine','storm'],
['משחק מחשב או קונסולה','the legend of zelda','super mario','counter strike','nintendo wii','super nintendo','playstation','steam','defense of the ancients','league of legends','final fantasy','donkey kong','angry birds','fallout','bioshock','tetris','the elders scroll','minecraft','call of duty','battlefield','bomberman','sonic the hedgehog','just dance','nintendo','sony','sega','dreamcast'],
['אנשים חשובים (לדוגמא: מדענים, ראשי ממשלה...)','albert einstein','barack obama','abraham lincoln','nikola tesla','carl sagan','larry page','steves jobs','mark zuckerberg','tim cook','charles chaplin','platao','aristoteles','dilma rousseff','luiz inacio lula da silva','fernando herinque cardoso','george washington','george walker bush','adolf hitler','shigeru miyamoto','Neil deGrasse Tyson'],
['כותרי קולנוע או שמות שחקנים ודמויות שקשורים לקולנוע', 'breaking bad', 'how i met your mother','sense8', 'american beauty','donnie Darko','home alone','the sixth sense','the shinning','titanic','everybody hates chris','the mad hatter','alice in the wonderland','harry potter','adventure time','spongebob','Narcos','pineapple express','Pokémon','Yugioh','Hermione','Lord voldemort','Draco Malfoy','Katniss everdeen','hunger games','Mockingjay','cathing fire','exorcist','limitless','the hangover','Matrix','the lord of rings','The hobbit','Frodo Baggins','Sauron','Legolas','Gandalf','Albus Dumbledore','Star wars','Luke Skywalker','Chewbacca', 'Yoda'],
['פוקימון דור ראשון','Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard', 'Squirtle', 'Wartortle', 'Blastoise', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill', 'Pidgey', 'Pidgeotto', 'Pidgeot', 'Rattata', 'Raticate', 'Spearow', 'Fearow', 'Ekans', 'Arbok', 'Pikachu', 'Raichu', 'Sandshrew', 'Sandslash', 'Nidoran', 'Nidorina', 'Nidoqueen', 'Nidorino', 'Nidoking', 'Clefairy', 'Clefable', 'Vulpix', 'Ninetales', 'Jigglypuff', 'Wigglytuff', 'Zubat', 'Golbat', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 'Venonat', 'Venomoth', 'Diglett', 'Dugtrio', 'Meowth', 'Persian', 'Psyduck', 'Golduck', 'Mankey', 'Primeape', 'Growlithe', 'Arcanine', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Abra', 'Kadabra', 'Alakazam', 'Machop', 'Machoke', 'Machamp', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Tentacool', 'Tentacruel', 'Geodude', 'Graveler', 'Golem', 'Ponyta', 'Rapidash', 'Slowpoke', 'Slowbro', 'Magnemite', 'Magneton', 'Doduo', 'Dodrio', 'Seel', 'Dewgong', 'Grimer', 'Muk', 'Shellder', 'Cloyster', 'Gastly', 'Haunter', 'Gengar', 'Onix', 'Drowzee', 'Hypno', 'Krabby', 'Kingler', 'Voltorb', 'Electrode', 'Exeggcute', 'Exeggutor', 'Cubone', 'Marowak', 'Hitmonlee', 'Hitmonchan', 'Lickitung', 'Koffing', 'Weezing', 'Rhyhorn', 'Rhydon', 'Chansey', 'Tangela', 'Kangaskhan', 'Horsea', 'Seadra', 'Goldeen', 'Seaking', 'Staryu', 'Starmie', 'Mr.', 'Mime', 'Scyther', 'Jynx', 'Electabuzz', 'Magmar', 'Pinsir', 'Tauros', 'Magikarp', 'Gyarados', 'Lapras', 'Ditto', 'Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Porygon', 'Omanyte', 'Omastar', 'Kabuto', 'Kabutops', 'Aerodactyl', 'Snorlax', 'Articuno', 'Zapdos', 'Moltres', 'Dratini', 'Dragonair', 'Dragonite', 'Mewtwo', 'Mew']
        ]

categorias = ''
for i in range(len(palavras)):
    categorias = categorias+palavras[i][0]+'\n'

#Keyaboar padrão
att_kb = 'שלח מקלדת'

#Botões dos Keyboards
novojogo = 'משחק חדש' + emoji_joystick
ajuda = 'עזרה' + emoji_light
rank = 'ניקוד' + emoji_trofeu
ligar = 'התחל' + emoji_foguete
desligar = 'עצור' + emoji_x
config = 'הגדרות' + emoji_ferramenta
voltar = 'חזור' + emoji_back
cancelar = 'ביטול' + emoji_x
comandos = 'פקודות' + emoji_light
entrar = 'הצטרף' + emoji_foguete
sair = 'יציאה' + emoji_x
fechar_jogo = 'התחל משחק' + emoji_foguete
cancelar_jogo = 'בטל משחק' + emoji_x
arriscar = 'נחש!' + emoji_gritar
esta_fora = 'יצאת מהמשחק' + emoji_proibido
sobre = 'אודות' + emoji_livro

#Respostas iniciais
linguas = emoji_planeta + 'בחר שפה:'
iniciar_msg = 'טוען...'
mudar_lingua = 'שינוי בוצע בהצלחה!' + emoji_thumbsUp
start_msg = 'היי! אני האיש התלוי, ואני נמצא בידיכם! תפקידי הוא לארגן ולשחק את משחקי האיש התלוי אתכם ועם חבריכם ולוודא שכולנו נהנה!\n לחץ על "משחק חדש" ונתחיל!' + emoji_sorriso
is_enabled = 'אני מוכן!'
stop_msg = 'מבצע כיבוי...'
about_msg = 'אני פרויקט בקוד פתוח שנוצר על ידי המשתמש @bcesarg6 והמשתמש @cristoferoswald! אני מתפתח באופן מתמיד ואתם מוזמנים לעזור לי לגדול על ידי תכנות באתר github.com/bcesarg6/PlayHangmanBot\n' +categorias+'גר 1.5:\n\t- תוקנו שגיאות באנגלית, הוספה השפה העברית (תודה מיוחדת ל@Shushishtok)\n\nעדכונים עתידיים:\n\t- קטגוריות ומילים של המשחקים League of Legends וDota2\n\t- מערכת בעיטת משתמשים\n\t- בחירת קטגוריית מילים\n\t- ניקוד גלובלי\n\n תרגישו חופשיים להצטרף לקבוצה!' + emoji_sorriso
start_help_msg = 'נכון לעכשיו אין משחקים פעילים. לחץ על כפתור "משחק חדש" כדי להתחיל משחק או לחץ על "ניקוד" כדי לצפות בניקוד הנוכחי.\n בנוסף, באפשרותך לשנות את ההגדרות ' +emoji_sorriso + '\nזכרו, אם בשלב כלשהו תזדקקו למקלדת שלחו את הפקודה /kb'
config_help_msg = 'בחר את השפה הרצויה. המילים החבויות במשחק משתנות בהתאם לשפה שנבחרה.\nבמקרה שלא מצאתם את השפה שלכם, תוכלו לעזור לפיתוח הפרויקט וליצור את התרגומים שלכם! לחצו על כפתור "אודות" למידע נוסף.\nזכרו, אם בשלב כלשהו תזדקקו למקלדת שלחו את הפקודה /kb'
voltar_msg = 'תפריט ראשי'
cantdo_msg = 'אתה לא יכול לעשות את זה'
comandos_msg = 'פקודות'
ocupado_msg = 'אני עסוק כרגע, מצטער' + emoji_triste + ' בבקשה, בחרו את השפה שלכם. כדי לצפות במקלדת שלחו את הפקודה /kb'
teclado_msg = 'מקלדת'
ranking_msg = emoji_coroa + ' ניקוד ' + emoji_coroa
error_msg = 'שגיאה התרחשה. נא צרו קשר עם @cristoferoswald או עם @bcesarg6 ודווחו עליה.' + emoji_triste
sorry_msg = 'מצטער, מה אמרת?'

#respostas PreGame
def inicialMsg(u_name):
    return 'מתחילים משחק חדש! \n'+u_name+' יהיה מנהל המשחק.' + emoji_oculos

inicial_msg = 'בואו נחליט מי משחק, מי שרוצה להיכנס שילחץ על אנטר!' + emoji_sorriso
close_game_msg = 'המשחק יחל בקרוב! בתורך לחץ על אות כדי לנחש אותה או לחץ על "נחש!" אם אתה חושב שגילית את המילה הסודית. שימו לב, ברגע שתנחשו, אין דרך חזרה!' + emoji_zoando + '\nאנחנו נשחק בסדר הבא:'
palavra_msg = 'המילה הסודית היא: '
categoria_msg = 'קטגוריה: '
esta_dentro_msg = 'אתה כבר במשחק!'
sem_jogador_msg = 'כל השחקנים יצאו, המשחק יתבטל. ' + emoji_surpreso
cancelar_jogo_msg = 'המשחק בוטל על ידי מנהל המשחק.'
is_out_msg = 'אתה לא במשחק' + emoji_lua
vidas_msg = 'חיים: '
pre_game_help_msg = 'אני ממתין לאנשים להצטרף למשחק, הקש אנטר כדי להצטרף!\nמנהל: לחץ "התחל משחק" כדי להתחיל את המשחק עם השחקנים הנוכחיים!'

def novoAdmMsg(u_name):
    return 'מנהל חדש נבחר! '+u_name+' הוא המנהל החדש.' + emoji_oculos

def playerQuitMsg(u_name):
    return 'השחקן '+u_name+' יצא.' + emoji_triste

def entrarMsg(u_name):
    return 'מצוין '+u_name+', אתה משחק איתנו!' + emoji_blink

#repostas InGame
in_game_help_msg = 'לחץ על האות כדי לנחש אותה או לחץ על נ"יחש!" אם אתה חושב שאתה כבר יודע את המילה הסודית!\nזכור, אם תזדקקו למקלדת שלחו את הפקודה /kb'
arriscar_msg = 'אז נדמה לך שאתה יודע מה המילה הסודית?' + emoji_zoando + 'שלח לי את המילה, אבל שים לב, אם היא שגויה אתה עף מהמשחק!' + emoji_lua
round_errado_msg = 'עוד לא תורך לשחק! חכה שהתור שלך יגיע!' + emoji_lua
acertou_letra_msg = 'אות נכונה!' + emoji_claps
errou_letra_msg = 'אות לא נכונה' + emoji_triste + emoji_heartb
jachutada_msg = 'כבר ניחשו את האות הזאת!' + emoji_surpreso
umavida_msg = 'ניסיון אחרון! מצאו את המילה הסודית או התמודדו עם התבוסה!' + emoji_lua
gameover_msg = emoji_poop + ' המשחק נגמר, לוזרים! ' + emoji_poop
fora_msg = 'אתה לא במשחק, חכה שהמשחק ייגמר כדי להיכנס!'


def googleMsg(palavra):
    palavras = palavra.split(' ')
    palavra = ''
    for i in range(len(palavras)):
        palavra = palavra + palavras[i] +'%20'
    return (('המילה').decode('utf-8')+': https://google.com/#q=' + palavra).encode('utf-8')

def perdeu(u_name):
    return 'השחקן ' + u_name + ' סיכן את הכל והפסיד! השחקן יצא מהמשחק! ' + emoji_lua

def nextPlayer(u_name):
    return 'תור ' + u_name + emoji_point

def venceu(u_name):
    return emoji_confetti + ' כל הכבוד! ' + u_name + ' מצאתם את המילה הסודית וניצחתם! ' + emoji_confetti + '\n הנקודות חושבו ועודכנו בלוח הניקוד ' + emoji_sorriso
