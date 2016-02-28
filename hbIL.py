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

['פוקימון דור ראשון','Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard', 'Squirtle', 'Wartortle', 'Blastoise', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill', 'Pidgey', 'Pidgeotto', 'Pidgeot', 'Rattata', 'Raticate', 'Spearow', 'Fearow', 'Ekans', 'Arbok', 'Pikachu', 'Raichu', 'Sandshrew', 'Sandslash', 'Nidoran', 'Nidorina', 'Nidoqueen', 'Nidorino', 'Nidoking', 'Clefairy', 'Clefable', 'Vulpix', 'Ninetales', 'Jigglypuff', 'Wigglytuff', 'Zubat', 'Golbat', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 'Venonat', 'Venomoth', 'Diglett', 'Dugtrio', 'Meowth', 'Persian', 'Psyduck', 'Golduck', 'Mankey', 'Primeape', 'Growlithe', 'Arcanine', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Abra', 'Kadabra', 'Alakazam', 'Machop', 'Machoke', 'Machamp', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Tentacool', 'Tentacruel', 'Geodude', 'Graveler', 'Golem', 'Ponyta', 'Rapidash', 'Slowpoke', 'Slowbro', 'Magnemite', 'Magneton', 'Doduo', 'Dodrio', 'Seel', 'Dewgong', 'Grimer', 'Muk', 'Shellder', 'Cloyster', 'Gastly', 'Haunter', 'Gengar', 'Onix', 'Drowzee', 'Hypno', 'Krabby', 'Kingler', 'Voltorb', 'Electrode', 'Exeggcute', 'Exeggutor', 'Cubone', 'Marowak', 'Hitmonlee', 'Hitmonchan', 'Lickitung', 'Koffing', 'Weezing', 'Rhyhorn', 'Rhydon', 'Chansey', 'Tangela', 'Kangaskhan', 'Horsea', 'Seadra', 'Goldeen', 'Seaking', 'Staryu', 'Starmie', 'Mr.', 'Mime', 'Scyther', 'Jynx', 'Electabuzz', 'Magmar', 'Pinsir', 'Tauros', 'Magikarp', 'Gyarados', 'Lapras', 'Ditto', 'Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Porygon', 'Omanyte', 'Omastar', 'Kabuto', 'Kabutops', 'Aerodactyl', 'Snorlax', 'Articuno', 'Zapdos', 'Moltres', 'Dratini', 'Dragonair', 'Dragonite', 'Mewtwo', 'Mew'],

['סרטים וסדרות טלוויזיה', 'breaking bad', 'how i met your mother','sense8', 'american beauty','donnie Darko','home alone','the sixth sense','the shinning','titanic','everybody hates chris','the mad hatter','alice in the wonderland','harry potter','adventure time','spongebob','Narcos','pineapple express','Pokémon','Yugioh','Hermione','Lord voldemort','Draco Malfoy','Katniss everdeen','hunger games','Mockingjay','cathing fire','exorcist','limitless','the hangover','Matrix','the lord of rings','The hobbit','Frodo Baggins','Sauron','Legolas','Gandalf','Albus Dumbledore','Star wars','Luke Skywalker','Chewbacca', 'Yoda'],

['פוקימון דור שני','Chikorita', 'Bayleef', 'Meganium', 'Cyndaquil', 'Quilava', 'Typhlosion', 'Totodile', 'Croconaw', 'Feraligatr', 'Sentret', 'Furret', 'Hoothoot', 'Noctowl', 'Ledyba', 'Ledian', 'Spinarak', 'Ariados', 'Crobat', 'Chinchou', 'Lanturn', 'Pichu', 'Cleffa', 'Igglybuff', 'Togepi', 'Togetic', 'Natu', 'Xatu', 'Mareep', 'Flaaffy', 'Ampharos', 'Bellossom', 'Marill', 'Azumarill', 'Sudowoodo', 'Politoed', 'Hoppip', 'Skiploom', 'Jumpluff', 'Aipom', 'Sunkern', 'Sunflora', 'Yanma', 'Wooper', 'Quagsire', 'Espeon', 'Umbreon', 'Murkrow', 'Slowking', 'Misdreavus', 'Unown', 'Wobbuffet', 'Girafarig', 'Pineco', 'Forretress', 'Dunsparce', 'Gligar', 'Steelix', 'Snubbull', 'Granbull', 'Qwilfish', 'Scizor', 'Shuckle', 'Heracross', 'Sneasel', 'Teddiursa', 'Ursaring', 'Slugma', 'Magcargo', 'Swinub', 'Piloswine', 'Corsola', 'Remoraid', 'Octillery', 'Delibird', 'Mantine', 'Skarmory', 'Houndour', 'Houndoom', 'Kingdra', 'Phanpy', 'Donphan', 'Porygon2', 'Stantler', 'Smeargle', 'Tyrogue', 'Hitmontop', 'Smoochum', 'Elekid', 'Magby', 'Miltank', 'Blissey', 'Raikou', 'Entei', 'Suicune', 'Larvitar', 'Pupitar', 'Tyranitar', 'Lugia', 'Ho oh', 'Celebi'],
['פוקימון דור שלישי','Treecko', 'Grovyle', 'Sceptile', 'Torchic', 'Combusken', 'Blaziken', 'Mudkip', 'Marshtomp', 'Swampert', 'Poochyena', 'Mightyena', 'Zigzagoon', 'Linoone', 'Wurmple', 'Silcoon', 'Beautifly', 'Cascoon', 'Dustox', 'Lotad', 'Lombre', 'Ludicolo', 'Seedot', 'Nuzleaf', 'Shiftry', 'Taillow', 'Swellow', 'Wingull', 'Pelipper', 'Ralts', 'Kirlia', 'Gardevoir', 'Surskit', 'Masquerain', 'Shroomish', 'Breloom', 'Slakoth', 'Vigoroth', 'Slaking', 'Nincada', 'Ninjask', 'Shedinja', 'Whismur', 'Loudred', 'Exploud', 'Makuhita', 'Hariyama', 'Azurill', 'Nosepass', 'Skitty', 'Delcatty', 'Sableye', 'Mawile', 'Aron', 'Lairon', 'Aggron', 'Meditite', 'Medicham', 'Electrike', 'Manectric', 'Plusle', 'Minun', 'Volbeat', 'Illumise', 'Roselia', 'Gulpin', 'Swalot', 'Carvanha', 'Sharpedo', 'Wailmer', 'Wailord', 'Numel', 'Camerupt', 'Torkoal', 'Spoink', 'Grumpig', 'Spinda', 'Trapinch', 'Vibrava', 'Flygon', 'Cacnea', 'Cacturne', 'Swablu', 'Altaria', 'Zangoose', 'Seviper', 'Lunatone', 'Solrock', 'Barboach', 'Whiscash', 'Corphish', 'Crawdaunt', 'Baltoy', 'Claydol', 'Lileep', 'Cradily', 'Anorith', 'Armaldo', 'Feebas', 'Milotic', 'Castform', 'Kecleon', 'Shuppet', 'Banette', 'Duskull', 'Dusclops', 'Tropius', 'Chimecho', 'Absol', 'Wynaut', 'Snorunt', 'Glalie', 'Spheal', 'Sealeo', 'Walrein', 'Clamperl', 'Huntail', 'Gorebyss', 'Relicanth', 'Luvdisc', 'Bagon', 'Shelgon', 'Salamence', 'Beldum', 'Metang', 'Metagross', 'Regirock', 'Regice', 'Registeel', 'Latias', 'Latios', 'Kyogre', 'Groudon', 'Rayquaza', 'Jirachi', 'Deoxys'],
['פוקימון דור רביעי','Turtwig', 'Grotle', 'Torterra', 'Chimchar', 'Monferno', 'Infernape', 'Piplup', 'Prinplup', 'Empoleon', 'Starly', 'Staravia', 'Staraptor', 'Bidoof', 'Bibarel', 'Kricketot', 'Kricketune', 'Shinx', 'Luxio', 'Luxray', 'Budew', 'Roserade', 'Cranidos', 'Rampardos', 'Shieldon', 'Bastiodon', 'Burmy', 'Wormadam', 'Mothim', 'Combee', 'Vespiquen', 'Pachirisu', 'Buizel', 'Floatzel', 'Cherubi', 'Cherrim', 'Shellos', 'Gastrodon', 'Ambipom', 'Drifloon', 'Drifblim', 'Buneary', 'Lopunny', 'Mismagius', 'Honchkrow', 'Glameow', 'Purugly', 'Chingling', 'Stunky', 'Skuntank', 'Bronzor', 'Bronzong', 'Bonsly', 'Mime Jr.', 'Happiny', 'Chatot', 'Spiritomb', 'Gible', 'Gabite', 'Garchomp', 'Munchlax', 'Riolu', 'Lucario', 'Hippopotas', 'Hippowdon', 'Skorupi', 'Drapion', 'Croagunk', 'Toxicroak', 'Carnivine', 'Finneon', 'Lumineon', 'Mantyke', 'Snover', 'Abomasnow', 'Weavile', 'Magnezone', 'Lickilicky', 'Rhyperior', 'Tangrowth', 'Electivire', 'Magmortar', 'Togekiss', 'Yanmega', 'Leafeon', 'Glaceon', 'Gliscor', 'Mamoswine', 'Porygon-Z', 'Gallade', 'Probopass', 'Dusknoir', 'Froslass', 'Rotom', 'Uxie', 'Mesprit', 'Azelf', 'Dialga', 'Palkia', 'Heatran', 'Regigigas', 'Giratina', 'Cresselia', 'Phione', 'Manaphy', 'Darkrai', 'Shaymin', 'Arceus'],
['פוקימון דור חמישי','Victini', 'Snivy', 'Servine', 'Serperior', 'Tepig', 'Pignite', 'Emboar', 'Oshawott', 'Dewott', 'Samurott', 'Patrat', 'Watchog', 'Lillipup', 'Herdier', 'Stoutland', 'Purrloin', 'Liepard', 'Pansage', 'Simisage', 'Pansear', 'Simisear', 'Panpour', 'Simipour', 'Munna', 'Musharna', 'Pidove', 'Tranquill', 'Unfezant', 'Blitzle', 'Zebstrika', 'Roggenrola', 'Boldore', 'Gigalith', 'Woobat', 'Swoobat', 'Drilbur', 'Excadrill', 'Audino', 'Timburr', 'Gurdurr', 'Conkeldurr', 'Tympole', 'Palpitoad', 'Seismitoad', 'Throh', 'Sawk', 'Sewaddle', 'Swadloon', 'Leavanny', 'Venipede', 'Whirlipede', 'Scolipede', 'Cottonee', 'Whimsicott', 'Petilil', 'Lilligant', 'Basculin', 'Sandile', 'Krokorok', 'Krookodile', 'Darumaka', 'Darmanitan', 'Maractus', 'Dwebble', 'Crustle', 'Scraggy', 'Scrafty', 'Sigilyph', 'Yamask', 'Cofagrigus', 'Tirtouga', 'Carracosta', 'Archen', 'Archeops', 'Trubbish', 'Garbodor', 'Zorua', 'Zoroark', 'Minccino', 'Cinccino', 'Gothita', 'Gothorita', 'Gothitelle', 'Solosis', 'Duosion', 'Reuniclus', 'Ducklett', 'Swanna', 'Vanillite', 'Vanillish', 'Vanilluxe', 'Deerling', 'Sawsbuck', 'Emolga', 'Karrablast', 'Escavalier', 'Foongus', 'Amoonguss', 'Frillish', 'Jellicent', 'Alomomola', 'Joltik', 'Galvantula', 'Ferroseed', 'Ferrothorn', 'Klink', 'Klang', 'Klinklang', 'Tynamo', 'Eelektrik', 'Eelektross', 'Elgyem', 'Beheeyem', 'Litwick', 'Lampent', 'Chandelure', 'Axew', 'Fraxure', 'Haxorus', 'Cubchoo', 'Beartic', 'Cryogonal', 'Shelmet', 'Accelgor', 'Stunfisk', 'Mienfoo', 'Mienshao', 'Druddigon', 'Golett', 'Golurk', 'Pawniard', 'Bisharp', 'Bouffalant', 'Rufflet', 'Braviary', 'Vullaby', 'Mandibuzz', 'Heatmor', 'Durant', 'Deino', 'Zweilous', 'Hydreigon', 'Larvesta', 'Volcarona', 'Cobalion', 'Terrakion', 'Virizion', 'Tornadus', 'Thundurus', 'Reshiram', 'Zekrom', 'Landorus', 'Kyurem', 'Keldeo', 'Meloetta', 'Genesect'],
['פוקימון דור שישי','Chespin', 'Quilladin', 'Chesnaught', 'Fennekin', 'Braixen', 'Delphox', 'Froakie', 'Frogadier', 'Greninja', 'Bunnelby', 'Diggersby', 'Fletchling', 'Fletchinder', 'Talonflame', 'Scatterbug', 'Spewpa', 'Vivillon', 'Litleo', 'Pyroar', 'Flabébé', 'Floette', 'Florges', 'Skiddo', 'Gogoat', 'Pancham', 'Pangoro', 'Furfrou', 'Espurr', 'Meowstic', 'Honedge', 'Doublade', 'Aegislash', 'Spritzee', 'Aromatisse', 'Swirlix', 'Slurpuff', 'Inkay', 'Malamar', 'Binacle', 'Barbaracle', 'Skrelp', 'Dragalge', 'Clauncher', 'Clawitzer', 'Helioptile', 'Heliolisk', 'Tyrunt', 'Tyrantrum', 'Amaura', 'Aurorus', 'Sylveon', 'Hawlucha', 'Dedenne', 'Carbink', 'Goomy', 'Sliggoo', 'Goodra', 'Klefki', 'Phantump', 'Trevenant', 'Pumpkaboo', 'Gourgeist', 'Bergmite', 'Avalugg', 'Noibat', 'Noivern', 'Xerneas', 'Yveltal', 'Zygarde', 'Diancie', 'Hoopa', 'Volcanion'],
['גיבורים מדוטא 2', 'Abaddon', 'Alchemist', 'Ancient Apparition', 'Anti Mage', 'Arc Warden', 'Axe', 'Bane', 'Batrider', 'Beastmaster', 'Bloodseeker', 'Bounty Hunter', 'Brewmaster', 'Bristleback', 'Broodmother', 'Centaur Warrunner', 'Chaos Knight', 'Chen', 'Clinkz', 'Clockwerk', 'Crystal Maiden', 'Dark Seer', 'Dazzle', ',Death Prophet', 'Disruptor', 'Doom', 'Dragon Knight', 'Drow Ranger', 'Earth Spirit', 'Earthshaker', 'Elder Titan', 'Ember Spirit', 'Enchantress', 'Enigma', 'Faceless Void', 'Gyrocopter', 'Huskar', 'Invoker', 'Io', 'Jakiro', 'Juggernaut', 'Keeper of the Light', 'Kunkka', 'Legion Commander', 'Leshrac', 'Lich', 'Lifestealer', 'Lina', 'Lion', 'Lone Druid', 'Luna', 'Lycan', 'Magnus', 'Medusa', 'Meepo', 'Mirana', 'Morphling', ',Naga Siren', 'Natures Prophet', 'Necrophos', 'Night Stalker', 'Nyx Assassin', 'Ogre Magi', 'Omniknight', 'Oracle', 'Outworld Devourer', 'Phantom Assassin', 'Phantom Lancer', 'Phoenix', 'Puck', 'Pudge', 'Pugna', 'Queen of Pain', 'Razor', 'Riki', 'Rubick', 'Sand King', 'Shadow Demon', 'Shadow Fiend', 'Shadow Shaman', 'Silencer', 'Skywrath Mage', 'Slardar', 'Slark', 'Sniper', 'Spectre', 'Spirit Breaker', 'Storm Spirit', 'Sven', 'Techies', 'Templar Assassin', 'Terrorblade', 'Tidehunter', 'Timbersaw', 'Tinker', 'Tiny', 'Treant Protector', 'Troll Warlord', 'Tusk', 'Undying', 'Ursa', 'VengefulSpirit', 'Venomancer', 'Viper', 'Visage', 'Warlock', 'Weaver', 'Windranger', 'Winter Wyvern','Witch Doctor', 'Wraith King','Zeus'],
['גיבורים מליג אוף לגנדס','Aatrox', 'Ahri', 'Akali', 'Alistar','Amumu','Anivia', 'Annie', 'Ashe', 'Azir', 'Bardo', 'Blitzcrank','Brand', 'Braum', 'Caitlyn', 'Cassiopeia','Cho Gath','Corki', 'Darius', 'Diana', 'Draven', 'Dr Mundo', 'Elise','Evelynn', 'Ezreal', 'Fiddlesticks', 'Fiora', 'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnar', 'Gragas', 'Graves', 'Hecarim','Heimerdinger', 'Illaoi', 'Irelia', 'Janna', 'Jarvan IV', 'Jax', 'Jayce', 'Jhin','Jinx', 'Kalista', 'Karma', 'Karthus', 'Kassadin', 'Katarina', 'Kayle', 'Kennen', 'Kha Zix','Kog Maw', 'LeBlanc', 'Lee Sin', 'Leona', 'Lissandra', 'Lucian', 'Lulu', 'Lux', 'Malphite','Malzahar',  'Maokai', 'Master Yi', 'Miss Fortune', 'Mordekaiser', 'Morgana', 'Nami', 'Nasus', 'Nautilus','Nidalee', 'Nocturne', 'Nunu', 'Olaf', 'Orianna', 'Pantheon', 'Poppy', 'Quinn', 'Rammus',  'Rek Sai','Renekton', 'Rengar', 'Riven',  'Rumble', 'Ryze', 'Sejuani', 'Shaco','Shen', 'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner', 'Sona',  'Soraka', 'Swain', 'Syndra', 'Talon', 'Taric', 'Teemo', 'Thresh', 'Tristana', 'Trundle', 'Tryndamere', 'Twisted Fate', 'Tryndamere', 'Udyr', 'Urgot', 'Varus', 'Vayne', 'Veigar', 'Vel Koz', 'Vi','Viktor', 'Vladimir', 'Volibear', 'Warwick', 'Wukong', 'Xerath','Xin Zhao', 'Yasuo', 'Yorick', 'Zac', 'Zed', 'Ziggs', 'Zilean', 'Zyra'],

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
categorias_btn = 'בחר קטגוריות' + emoji_ferramenta


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
error_msg = 'שגיאה התרחשה. נא צרו קשר עם @Shushishtok ודווחו עליה.' + emoji_triste
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

cat_msg = 'בחר את הקטגוריות שתרצה שיהיו במשחק. שלח לי את המספרים עם רווחים ביניהם כדי לבחור קטגוריה.\n\nקטגוריות אפשריות:'
for i in range(len(palavras)):
        cat_msg = cat_msg +'\t '+str(i+1)+' - '+palavras[i][0]+'\n'

cat_msg = cat_msg + 'כדי לשחק עם כל הקטגוריות, שלח לי את המספר 0.\n שים לב, הבחירה שלך נשמרת במערכת.\n לדוגמא: 1 3 5 8 13'

cat_erro_msg = 'שגיאה!' + emoji_heartb + '\nודא כי אין מילים או אותיות בטקסט!\n דוגמא תקינה: 1 3 5 8 13\n או שלח אליי את המספר 0 לכל הקטגוריות' + emoji_blink
categorias_msg = 'בוצע בהצלחה! קדימה למשחק!' + emoji_sorriso

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
