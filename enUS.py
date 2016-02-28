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
['Heroes and villains','batman','flash','wonder women','penguin','super man','grenn lantern','grenn goblin','spider man','thor','hulk','iron man','ant man','human torch','the thing','black widow','green arrow','groot','rocket raccoon','magneto','wolverine','storm'],
['Videogame or game','the legend of zelda','super mario','counter strike','nintendo wii','super nintendo','playstation','steam','defense of the ancients','league of legends','final fantasy','donkey kong','angry birds','fallout','bioshock','tetris','the elders scroll','minecraft','call of duty','battlefield','bomberman','sonic the hedgehog','just dance','nintendo','sony','sega','dreamcast'],
['Important people','Francis Bacon','John Locke','Jean Jacques Rousseau','Christopher Columbus','Pedro Álvares Cabral','Nicolau Maquiavel','Giordano Bruno','Leonardo da Vinci','René Descartes','Isaac Newton','Galileo Galilei','Alan Turing','Mahatma Gandhi','martin luther king','Karl Marx','Friedrich Nietzsche','albert einstein','barack obama','abraham lincoln','nikola tesla','Sigmund Freud','carl sagan','larry page','steves jobs','mark zuckerberg','tim cook','charles chaplin','platao','aristoteles','dilma rousseff','luiz inacio lula da silva','fernando herinque cardoso','george washington','george walker bush','adolf hitler','shigeru miyamoto','Neil deGrasse Tyson'],
['Shows and movies', 'breaking bad', 'how i met your mother','sense8', 'american beauty','donnie Darko','home alone','the sixth sense','the shinning','titanic','everybody hates chris','the mad hatter','alice in the wonderland','harry potter','adventure time','spongebob','Narcos','pineapple express','Pokémon','Yugioh','Hermione','Lord voldemort','Draco Malfoy','Katniss everdeen','hunger games','Mockingjay','cathing fire','exorcist','limitless','the hangover','Matrix','the lord of rings','The hobbit','Frodo Baggins','Sauron','Legolas','Gandalf','Albus Dumbledore','Star wars','Luke Skywalker','Chewbacca', 'Yoda'],
['Pokemons 1st Gen','Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard', 'Squirtle', 'Wartortle', 'Blastoise', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill', 'Pidgey', 'Pidgeotto', 'Pidgeot', 'Rattata', 'Raticate', 'Spearow', 'Fearow', 'Ekans', 'Arbok', 'Pikachu', 'Raichu', 'Sandshrew', 'Sandslash', 'Nidoran', 'Nidorina', 'Nidoqueen', 'Nidorino', 'Nidoking', 'Clefairy', 'Clefable', 'Vulpix', 'Ninetales', 'Jigglypuff', 'Wigglytuff', 'Zubat', 'Golbat', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 'Venonat', 'Venomoth', 'Diglett', 'Dugtrio', 'Meowth', 'Persian', 'Psyduck', 'Golduck', 'Mankey', 'Primeape', 'Growlithe', 'Arcanine', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Abra', 'Kadabra', 'Alakazam', 'Machop', 'Machoke', 'Machamp', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Tentacool', 'Tentacruel', 'Geodude', 'Graveler', 'Golem', 'Ponyta', 'Rapidash', 'Slowpoke', 'Slowbro', 'Magnemite', 'Magneton', 'Doduo', 'Dodrio', 'Seel', 'Dewgong', 'Grimer', 'Muk', 'Shellder', 'Cloyster', 'Gastly', 'Haunter', 'Gengar', 'Onix', 'Drowzee', 'Hypno', 'Krabby', 'Kingler', 'Voltorb', 'Electrode', 'Exeggcute', 'Exeggutor', 'Cubone', 'Marowak', 'Hitmonlee', 'Hitmonchan', 'Lickitung', 'Koffing', 'Weezing', 'Rhyhorn', 'Rhydon', 'Chansey', 'Tangela', 'Kangaskhan', 'Horsea', 'Seadra', 'Goldeen', 'Seaking', 'Staryu', 'Starmie', 'Mr.', 'Mime', 'Scyther', 'Jynx', 'Electabuzz', 'Magmar', 'Pinsir', 'Tauros', 'Magikarp', 'Gyarados', 'Lapras', 'Ditto', 'Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Porygon', 'Omanyte', 'Omastar', 'Kabuto', 'Kabutops', 'Aerodactyl', 'Snorlax', 'Articuno', 'Zapdos', 'Moltres', 'Dratini', 'Dragonair', 'Dragonite', 'Mewtwo', 'Mew'],
['Pokemons 2nd Gen','Chikorita', 'Bayleef', 'Meganium', 'Cyndaquil', 'Quilava', 'Typhlosion', 'Totodile', 'Croconaw', 'Feraligatr', 'Sentret', 'Furret', 'Hoothoot', 'Noctowl', 'Ledyba', 'Ledian', 'Spinarak', 'Ariados', 'Crobat', 'Chinchou', 'Lanturn', 'Pichu', 'Cleffa', 'Igglybuff', 'Togepi', 'Togetic', 'Natu', 'Xatu', 'Mareep', 'Flaaffy', 'Ampharos', 'Bellossom', 'Marill', 'Azumarill', 'Sudowoodo', 'Politoed', 'Hoppip', 'Skiploom', 'Jumpluff', 'Aipom', 'Sunkern', 'Sunflora', 'Yanma', 'Wooper', 'Quagsire', 'Espeon', 'Umbreon', 'Murkrow', 'Slowking', 'Misdreavus', 'Unown', 'Wobbuffet', 'Girafarig', 'Pineco', 'Forretress', 'Dunsparce', 'Gligar', 'Steelix', 'Snubbull', 'Granbull', 'Qwilfish', 'Scizor', 'Shuckle', 'Heracross', 'Sneasel', 'Teddiursa', 'Ursaring', 'Slugma', 'Magcargo', 'Swinub', 'Piloswine', 'Corsola', 'Remoraid', 'Octillery', 'Delibird', 'Mantine', 'Skarmory', 'Houndour', 'Houndoom', 'Kingdra', 'Phanpy', 'Donphan', 'Porygon2', 'Stantler', 'Smeargle', 'Tyrogue', 'Hitmontop', 'Smoochum', 'Elekid', 'Magby', 'Miltank', 'Blissey', 'Raikou', 'Entei', 'Suicune', 'Larvitar', 'Pupitar', 'Tyranitar', 'Lugia', 'Ho oh', 'Celebi'],
['Pokemons 3rd Gen','Treecko', 'Grovyle', 'Sceptile', 'Torchic', 'Combusken', 'Blaziken', 'Mudkip', 'Marshtomp', 'Swampert', 'Poochyena', 'Mightyena', 'Zigzagoon', 'Linoone', 'Wurmple', 'Silcoon', 'Beautifly', 'Cascoon', 'Dustox', 'Lotad', 'Lombre', 'Ludicolo', 'Seedot', 'Nuzleaf', 'Shiftry', 'Taillow', 'Swellow', 'Wingull', 'Pelipper', 'Ralts', 'Kirlia', 'Gardevoir', 'Surskit', 'Masquerain', 'Shroomish', 'Breloom', 'Slakoth', 'Vigoroth', 'Slaking', 'Nincada', 'Ninjask', 'Shedinja', 'Whismur', 'Loudred', 'Exploud', 'Makuhita', 'Hariyama', 'Azurill', 'Nosepass', 'Skitty', 'Delcatty', 'Sableye', 'Mawile', 'Aron', 'Lairon', 'Aggron', 'Meditite', 'Medicham', 'Electrike', 'Manectric', 'Plusle', 'Minun', 'Volbeat', 'Illumise', 'Roselia', 'Gulpin', 'Swalot', 'Carvanha', 'Sharpedo', 'Wailmer', 'Wailord', 'Numel', 'Camerupt', 'Torkoal', 'Spoink', 'Grumpig', 'Spinda', 'Trapinch', 'Vibrava', 'Flygon', 'Cacnea', 'Cacturne', 'Swablu', 'Altaria', 'Zangoose', 'Seviper', 'Lunatone', 'Solrock', 'Barboach', 'Whiscash', 'Corphish', 'Crawdaunt', 'Baltoy', 'Claydol', 'Lileep', 'Cradily', 'Anorith', 'Armaldo', 'Feebas', 'Milotic', 'Castform', 'Kecleon', 'Shuppet', 'Banette', 'Duskull', 'Dusclops', 'Tropius', 'Chimecho', 'Absol', 'Wynaut', 'Snorunt', 'Glalie', 'Spheal', 'Sealeo', 'Walrein', 'Clamperl', 'Huntail', 'Gorebyss', 'Relicanth', 'Luvdisc', 'Bagon', 'Shelgon', 'Salamence', 'Beldum', 'Metang', 'Metagross', 'Regirock', 'Regice', 'Registeel', 'Latias', 'Latios', 'Kyogre', 'Groudon', 'Rayquaza', 'Jirachi', 'Deoxys'],
['Pokemons 4th Gen','Turtwig', 'Grotle', 'Torterra', 'Chimchar', 'Monferno', 'Infernape', 'Piplup', 'Prinplup', 'Empoleon', 'Starly', 'Staravia', 'Staraptor', 'Bidoof', 'Bibarel', 'Kricketot', 'Kricketune', 'Shinx', 'Luxio', 'Luxray', 'Budew', 'Roserade', 'Cranidos', 'Rampardos', 'Shieldon', 'Bastiodon', 'Burmy', 'Wormadam', 'Mothim', 'Combee', 'Vespiquen', 'Pachirisu', 'Buizel', 'Floatzel', 'Cherubi', 'Cherrim', 'Shellos', 'Gastrodon', 'Ambipom', 'Drifloon', 'Drifblim', 'Buneary', 'Lopunny', 'Mismagius', 'Honchkrow', 'Glameow', 'Purugly', 'Chingling', 'Stunky', 'Skuntank', 'Bronzor', 'Bronzong', 'Bonsly', 'Mime Jr.', 'Happiny', 'Chatot', 'Spiritomb', 'Gible', 'Gabite', 'Garchomp', 'Munchlax', 'Riolu', 'Lucario', 'Hippopotas', 'Hippowdon', 'Skorupi', 'Drapion', 'Croagunk', 'Toxicroak', 'Carnivine', 'Finneon', 'Lumineon', 'Mantyke', 'Snover', 'Abomasnow', 'Weavile', 'Magnezone', 'Lickilicky', 'Rhyperior', 'Tangrowth', 'Electivire', 'Magmortar', 'Togekiss', 'Yanmega', 'Leafeon', 'Glaceon', 'Gliscor', 'Mamoswine', 'Porygon-Z', 'Gallade', 'Probopass', 'Dusknoir', 'Froslass', 'Rotom', 'Uxie', 'Mesprit', 'Azelf', 'Dialga', 'Palkia', 'Heatran', 'Regigigas', 'Giratina', 'Cresselia', 'Phione', 'Manaphy', 'Darkrai', 'Shaymin', 'Arceus'],
['Pokemons 5th Gen','Victini', 'Snivy', 'Servine', 'Serperior', 'Tepig', 'Pignite', 'Emboar', 'Oshawott', 'Dewott', 'Samurott', 'Patrat', 'Watchog', 'Lillipup', 'Herdier', 'Stoutland', 'Purrloin', 'Liepard', 'Pansage', 'Simisage', 'Pansear', 'Simisear', 'Panpour', 'Simipour', 'Munna', 'Musharna', 'Pidove', 'Tranquill', 'Unfezant', 'Blitzle', 'Zebstrika', 'Roggenrola', 'Boldore', 'Gigalith', 'Woobat', 'Swoobat', 'Drilbur', 'Excadrill', 'Audino', 'Timburr', 'Gurdurr', 'Conkeldurr', 'Tympole', 'Palpitoad', 'Seismitoad', 'Throh', 'Sawk', 'Sewaddle', 'Swadloon', 'Leavanny', 'Venipede', 'Whirlipede', 'Scolipede', 'Cottonee', 'Whimsicott', 'Petilil', 'Lilligant', 'Basculin', 'Sandile', 'Krokorok', 'Krookodile', 'Darumaka', 'Darmanitan', 'Maractus', 'Dwebble', 'Crustle', 'Scraggy', 'Scrafty', 'Sigilyph', 'Yamask', 'Cofagrigus', 'Tirtouga', 'Carracosta', 'Archen', 'Archeops', 'Trubbish', 'Garbodor', 'Zorua', 'Zoroark', 'Minccino', 'Cinccino', 'Gothita', 'Gothorita', 'Gothitelle', 'Solosis', 'Duosion', 'Reuniclus', 'Ducklett', 'Swanna', 'Vanillite', 'Vanillish', 'Vanilluxe', 'Deerling', 'Sawsbuck', 'Emolga', 'Karrablast', 'Escavalier', 'Foongus', 'Amoonguss', 'Frillish', 'Jellicent', 'Alomomola', 'Joltik', 'Galvantula', 'Ferroseed', 'Ferrothorn', 'Klink', 'Klang', 'Klinklang', 'Tynamo', 'Eelektrik', 'Eelektross', 'Elgyem', 'Beheeyem', 'Litwick', 'Lampent', 'Chandelure', 'Axew', 'Fraxure', 'Haxorus', 'Cubchoo', 'Beartic', 'Cryogonal', 'Shelmet', 'Accelgor', 'Stunfisk', 'Mienfoo', 'Mienshao', 'Druddigon', 'Golett', 'Golurk', 'Pawniard', 'Bisharp', 'Bouffalant', 'Rufflet', 'Braviary', 'Vullaby', 'Mandibuzz', 'Heatmor', 'Durant', 'Deino', 'Zweilous', 'Hydreigon', 'Larvesta', 'Volcarona', 'Cobalion', 'Terrakion', 'Virizion', 'Tornadus', 'Thundurus', 'Reshiram', 'Zekrom', 'Landorus', 'Kyurem', 'Keldeo', 'Meloetta', 'Genesect'],
['Pokemons 6th Gen','Chespin', 'Quilladin', 'Chesnaught', 'Fennekin', 'Braixen', 'Delphox', 'Froakie', 'Frogadier', 'Greninja', 'Bunnelby', 'Diggersby', 'Fletchling', 'Fletchinder', 'Talonflame', 'Scatterbug', 'Spewpa', 'Vivillon', 'Litleo', 'Pyroar', 'Flabébé', 'Floette', 'Florges', 'Skiddo', 'Gogoat', 'Pancham', 'Pangoro', 'Furfrou', 'Espurr', 'Meowstic', 'Honedge', 'Doublade', 'Aegislash', 'Spritzee', 'Aromatisse', 'Swirlix', 'Slurpuff', 'Inkay', 'Malamar', 'Binacle', 'Barbaracle', 'Skrelp', 'Dragalge', 'Clauncher', 'Clawitzer', 'Helioptile', 'Heliolisk', 'Tyrunt', 'Tyrantrum', 'Amaura', 'Aurorus', 'Sylveon', 'Hawlucha', 'Dedenne', 'Carbink', 'Goomy', 'Sliggoo', 'Goodra', 'Klefki', 'Phantump', 'Trevenant', 'Pumpkaboo', 'Gourgeist', 'Bergmite', 'Avalugg', 'Noibat', 'Noivern', 'Xerneas', 'Yveltal', 'Zygarde', 'Diancie', 'Hoopa', 'Volcanion'],
['Dota 2 Heroes', 'Abaddon', 'Alchemist', 'Ancient Apparition', 'Anti Mage', 'Arc Warden', 'Axe', 'Bane', 'Batrider', 'Beastmaster', 'Bloodseeker', 'Bounty Hunter', 'Brewmaster', 'Bristleback', 'Broodmother', 'Centaur Warrunner', 'Chaos Knight', 'Chen', 'Clinkz', 'Clockwerk', 'Crystal Maiden', 'Dark Seer', 'Dazzle', ',Death Prophet', 'Disruptor', 'Doom', 'Dragon Knight', 'Drow Ranger', 'Earth Spirit', 'Earthshaker', 'Elder Titan', 'Ember Spirit', 'Enchantress', 'Enigma', 'Faceless Void', 'Gyrocopter', 'Huskar', 'Invoker', 'Io', 'Jakiro', 'Juggernaut', 'Keeper of the Light', 'Kunkka', 'Legion Commander', 'Leshrac', 'Lich', 'Lifestealer', 'Lina', 'Lion', 'Lone Druid', 'Luna', 'Lycan', 'Magnus', 'Medusa', 'Meepo', 'Mirana', 'Morphling', ',Naga Siren', 'Natures Prophet', 'Necrophos', 'Night Stalker', 'Nyx Assassin', 'Ogre Magi', 'Omniknight', 'Oracle', 'Outworld Devourer', 'Phantom Assassin', 'Phantom Lancer', 'Phoenix', 'Puck', 'Pudge', 'Pugna', 'Queen of Pain', 'Razor', 'Riki', 'Rubick', 'Sand King', 'Shadow Demon', 'Shadow Fiend', 'Shadow Shaman', 'Silencer', 'Skywrath Mage', 'Slardar', 'Slark', 'Sniper', 'Spectre', 'Spirit Breaker', 'Storm Spirit', 'Sven', 'Techies', 'Templar Assassin', 'Terrorblade', 'Tidehunter', 'Timbersaw', 'Tinker', 'Tiny', 'Treant Protector', 'Troll Warlord', 'Tusk', 'Undying', 'Ursa', 'VengefulSpirit', 'Venomancer', 'Viper', 'Visage', 'Warlock', 'Weaver', 'Windranger', 'Winter Wyvern','Witch Doctor', 'Wraith King','Zeus'],
['League of Legends Champions','Aatrox', 'Ahri', 'Akali', 'Alistar','Amumu','Anivia', 'Annie', 'Ashe', 'Azir', 'Bardo', 'Blitzcrank','Brand', 'Braum', 'Caitlyn', 'Cassiopeia','Cho Gath','Corki', 'Darius', 'Diana', 'Draven', 'Dr Mundo', 'Elise','Evelynn', 'Ezreal', 'Fiddlesticks', 'Fiora', 'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnar', 'Gragas', 'Graves', 'Hecarim','Heimerdinger', 'Illaoi', 'Irelia', 'Janna', 'Jarvan IV', 'Jax', 'Jayce', 'Jhin','Jinx', 'Kalista', 'Karma', 'Karthus', 'Kassadin', 'Katarina', 'Kayle', 'Kennen', 'Kha Zix','Kog Maw', 'LeBlanc', 'Lee Sin', 'Leona', 'Lissandra', 'Lucian', 'Lulu', 'Lux', 'Malphite','Malzahar',  'Maokai', 'Master Yi', 'Miss Fortune', 'Mordekaiser', 'Morgana', 'Nami', 'Nasus', 'Nautilus','Nidalee', 'Nocturne', 'Nunu', 'Olaf', 'Orianna', 'Pantheon', 'Poppy', 'Quinn', 'Rammus',  'Rek Sai','Renekton', 'Rengar', 'Riven',  'Rumble', 'Ryze', 'Sejuani', 'Shaco','Shen', 'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner', 'Sona',  'Soraka', 'Swain', 'Syndra', 'Talon', 'Taric', 'Teemo', 'Thresh', 'Tristana', 'Trundle', 'Tryndamere', 'Twisted Fate', 'Tryndamere', 'Udyr', 'Urgot', 'Varus', 'Vayne', 'Veigar', 'Vel Koz', 'Vi','Viktor', 'Vladimir', 'Volibear', 'Warwick', 'Wukong', 'Xerath','Xin Zhao', 'Yasuo', 'Yorick', 'Zac', 'Zed', 'Ziggs', 'Zilean', 'Zyra'],

    ]

categorias = ''
for i in range(len(palavras)):
    categorias = categorias+palavras[i][0]+'\n'

#Keyaboar padrão
att_kb = 'Send Keyboard'

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
categorias_btn = 'Select categories' + emoji_ferramenta

#Respostas iniciais
linguas = emoji_planeta + 'Choose a language:'
iniciar_msg = 'Loading...'
mudar_lingua = 'Change successful' + emoji_thumbsUp
start_msg = 'Hi, I am the Hangman, master of Hangman games! My duty is to organize and play Hangman games with you and your friends and ensure that we will have fun!\n Press the "new game" button and we shall begin!' + emoji_sorriso
is_enabled = 'I am already ready!'
stop_msg = 'Turning off'
about_msg = 'I am an Open Source project created by @bcesarg6 and @cristoferoswald! I am in constant development and you can help me growing up coding at github.com/bcesarg6/PlayHangmanBot\n\nCategories:\n'+categorias+'\nVersion 2.0 - KIWI:\n*NOW WITH MORE THAN 1K WORDS!*\n\t- Added hebrew translation (special thanks to @Shushishtok)\n\t- Added the category selection system\n\t- 5 New Pokémon Gens, Dota 2 and League of legends categories added \n\nFuture updates:\n\t- Kick player system\n\t- Global ranking\n\t- New game modes!\n\nFeel free to join the team!' + emoji_sorriso
start_help_msg = 'There is no game ongoing right now, press the button "new game" to start one or press "Rank" to see the ranking.\n You can also change the settings if you want to' + emoji_sorriso + '\nRemember, if anytime you need a keyboard send me the command /kb'
config_help_msg = 'Choose the language you want. The secret words of the game depends on the selected language\nDid not find your language? You can help my development by making your own translations! Press the About button for more information.\nRemember, if anytime you need a keyboard send me the command /kb'
voltar_msg = 'Main menu'
cantdo_msg = 'You can not do this'
comandos_msg = 'Commands'
ocupado_msg = 'I am busy right now, sorry' + emoji_triste + ' Please, select your language first, send /kb to see the keyboard'
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
esta_dentro_msg = 'You are already in this game!'
sem_jogador_msg = 'All the players left, the game will be cancelled! ' + emoji_surpreso
cancelar_jogo_msg = 'Game canceled by the admin'
is_out_msg = 'You are not in this game' + emoji_lua
vidas_msg = 'Lives: '
pre_game_help_msg = 'I am waiting for people to join the game, press "Enter" to join \nAdmin: Press "Start game" to begin the game with this players'

cat_msg = 'Select the categories of words that you want in your game, send me the numbers with spaces between them to choose the categories!\n\nCATEGORIES:\n'
for i in range(len(palavras)):
        cat_msg = cat_msg +'\t '+str(i+1)+' - '+palavras[i][0]+'\n'

cat_msg = cat_msg + 'To play with all categories just send me 0\nRemember, your selection will be saved!\n Example: 1 3 5 8 13'

cat_erro_msg = 'Error!' + emoji_heartb + '\nBe sure to no include words or letters within the text!\nExample: 1 3 5 8 13\nOr just 0 to default selection (All categories)' + emoji_blink
categorias_msg = 'Done! Good game!' + emoji_sorriso


def novoAdmMsg(u_name):
    return 'A new admin was selected! '+u_name+' is the new admin.' + emoji_oculos

def playerQuitMsg(u_name):
    return 'The player '+u_name+' left.' + emoji_triste

def entrarMsg(u_name):
    return 'Ok '+u_name+', you will play in this game' + emoji_blink

#repostas InGame
in_game_help_msg = 'Press the letter to guess it or press "Risk" if you think that already know the secret word!\nRemember, if anytime you need a keyboard send me the command /kb'
arriscar_msg = 'So you think that you know what is the secret word? ' + emoji_zoando + ' Send me the word, but think wisely, if you fail you will be eliminated!' + emoji_lua
round_errado_msg = 'It is not your time to play yet! Wait for your turn!' + emoji_lua
acertou_letra_msg = 'Right letter!' + emoji_claps
errou_letra_msg = 'Wrong letter' + emoji_triste + emoji_heartb
jachutada_msg = 'This letter has already been guessed' + emoji_surpreso
umavida_msg = 'One life left! Discover the secret word or face your DEFEAT!' + emoji_lua
gameover_msg = emoji_poop + ' GAME OVER LOSERS! ' + emoji_poop
fora_msg = 'You are not in this game, wait for this game end to enter in another one!'


def googleMsg(palavra):
    palavras = palavra.split(' ')
    palavra = ''
    for i in range(len(palavras)):
        palavra = palavra + palavras[i] +'%20'
    return ('Discover: https://google.com/#q=' + palavra).encode('utf-8')

def perdeu(u_name):
    return u_name + ' Risked it all and losed! The player was eliminated!' + emoji_lua

def nextPlayer(u_name):
    return u_name + '\'s turn ' + emoji_point

def venceu(u_name):
    return emoji_confetti + ' Congratulations ' + u_name + ' you discovered the secret word and won the game! ' + emoji_confetti + '\n Score calculated and ranking updated! ' + emoji_sorriso
