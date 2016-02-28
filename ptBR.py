#-*- coding: utf-8 -*-
#Linguagem Português, contém as strings que serão lidas para aparecerem no jogo

#Emojis
from emojis import *

#palavras
palavras = [
                ['Animais', 'macaco', 'elefante','zebra','papagaio','andorinha','golfinho','gorila','tubarao','lobo','ornitorrinco','cavalo','humano','lebre','coelho','periquito','pomba','dinossauro','macaco','borboleta','Baleia', 'Cachorro', 'Cobra', 'Crocodilo', 'Frango', 'Galinha', 'Gambá', 'Gato', 'Leão', 'Girafa', 'Ovelha', 'Polvo', 'Rinocerontes', 'Tartarugas', 'Touro', 'Ursos', 'Vaca','Lontra', 'Onça', 'Porco', 'Urubú', 'Camelo', 'Cascavel', 'Burro'],
                ['Frutas', 'Abacate', 'Amora', 'Ameixa', 'Acerola', 'Abacaxi', 'Açaí', 'Banana', 'Carambola', 'Caju', 'Cereja', 'Cacau', 'Caqui', 'Cupuaçu', 'Damasco', 'Figo', 'Framboesa', 'Graviola', 'Goiaba', 'Groselha', 'Guaraná', 'Jaca', 'Jabuticaba', 'Kiwi', 'Laranja', 'Limão', 'Melancia', 'Mamão', 'Melão', 'Maracujá', 'Manga', 'Maçã', 'Pera', 'Pêssego', 'Tangerina', 'Tomate', 'Tamarindo', 'Uva'],
                ['Comidas','Macarrão instantâneo','cachorro quente','lasanha','frango a passarinho','batata frita','ketchup','chocolate','strogonoff','arroz e feijão','batata doce','pizza','sushi','temaki','fondue de chocolate','bolo','kitkat','pirulito','algodão doce','Escondidinho de carne seca','Torta de limão','Panqueca','Feijoada'],
                ['Profissões', 'advogado', 'professor', 'zelador','prostituta','médico','marceneiro','designer','desenvolvedor de jogos','dublador','escritor','cozinheiro','pedreiro','vendedor','gerente','caminhoneiro','taxista','pintor','mecânico','auxiliar','estagiário','carteiro','cirurgião','oftalmologista','analista de sistemas','empresário','piloto','bancário','jardineiro','fotógrafo','escrivão','juiz','delegado','soldado','sargento','xerife','engenheiro','mestre de obras','tradutor','farmacêutico','veterinário','costureiro','recepcionista','cientista','político','encanador','eletricista','massoterapeuta','garçom'],
                ['Coisas de computador', 'programador','compilador','servidor','monitor','algoritmo','netflix','orkut','instagram','tumblr','twitter','rede neural','google','photoshop','wolfram alpha','python','java','framework','ruby','javascript','latex','android','stack overflow','wikipedia','debugging'],
                ['Pessoas importantes','Giordano Bruno','Leonardo da Vinci','Francis Bacon','John Locke','Jean Jacques Rousseau','Cristovão Colombo','Pedro Álvares Cabral','René Descartes','Isaac Newton','Galileu Galilei','Alan Turing','Mahatma Gandhi','martin luther king','Karl Marx','Friedrich Nietzsche','albert einstein','barack obama','abraham lincoln','nikola tesla','carl sagan','larry page','steves jobs','mark zuckerberg','tim cook','charles chaplin','platao','aristoteles','dilma rousseff','luiz inacio lula da silva','fernando herinque cardoso','george washington','george walker bush','adolf hitler','shigeru miyamoto','Neil deGrasse Tyson','carlos drummond de andrade','Machado de Assis','santos dumont','Sigmund Freud'],
                ['Cidades do mundo','brasília','curitiba','maringá','nova iorque','tokio','barcelona','amsterdã','paris','milão','pequim','berlim','são paulo','rio de janeiro','salvador','manaus','rio branco','orlando','los angeles','calgary','toronto','montreal','dallas','londres','cuiabá','macheral cândido rondon','campo mourão','toledo','Cascavel','Ouro preto'],
                ['Heróis ou vilões','batman','flash','mulher maravilha','pinguim','super Homem','lanterna verde','duende verde','homem aranha','thor','hulk','homem de ferro','homem formiga','tocha humana','o coisa','viuva negra','arqueiro verde','groot','rocket raccoon','magneto','wolverine','tempestade'],
                ['Videogames e jogos','the legend of zelda','super mario','counter strike','nintendo wii','super nintendo','playstation','steam','defense of the ancients','league of legends','final fantasy','donkey kong','angry birds','fallout','bioshock','tetris','the elders scroll','minecraft','call of duty','battlefield','bomberman','sonic','just dance','nintendo','sony','Farcry','sega','dreamcast'],
                ['Filmes e series', 'Breaking bad','how i met your mother','sense8','beleza americana','donnie Darko','esqueceram de mim','o sexto sentido','o iluminado','titanic','todo mundo odeia o cris','chapeleiro maluco','alice no país das maravilhas','harry potter','hora de aventura','bob esponja','Narcos','Segurando as pontas','Pokémon','Yugioh','Hermione','Lord voldemort','Draco Malfoy','Katniss everdeen','Jogos vorazes','A esperança','Em chamas','O exorcista','Sem limites','Se beber não case','Matrix','O Senhor dos anéis','O hobbit','Frodo Baggins','Sauron','Legolas','Gandalf','Albus Dumbledore','Star wars','Luke Skywalker','Chewbacca','Mestre Yoda'],
                ['Países', 'brasil', 'estados Unidos', 'alemanha', 'japão', 'coréia do sul', 'áfrica do sul', 'holanda', 'argentina', 'espanha', 'chile', 'equador', 'canadá', 'singapura', 'índia', 'emirados árabes', 'itália', 'inglaterra', 'áustria', 'grécia', 'república Checa','austrália','madagáscar','rússia','china','méxico','colômbia','etiópia','bolívia'],
                ['Pokemons 1a geração','Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard', 'Squirtle', 'Wartortle', 'Blastoise', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill', 'Pidgey', 'Pidgeotto', 'Pidgeot', 'Rattata', 'Raticate', 'Spearow', 'Fearow', 'Ekans', 'Arbok', 'Pikachu', 'Raichu', 'Sandshrew', 'Sandslash', 'Nidoran', 'Nidorina', 'Nidoqueen', 'Nidorino', 'Nidoking', 'Clefairy', 'Clefable', 'Vulpix', 'Ninetales', 'Jigglypuff', 'Wigglytuff', 'Zubat', 'Golbat', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 'Venonat', 'Venomoth', 'Diglett', 'Dugtrio', 'Meowth', 'Persian', 'Psyduck', 'Golduck', 'Mankey', 'Primeape', 'Growlithe', 'Arcanine', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Abra', 'Kadabra', 'Alakazam', 'Machop', 'Machoke', 'Machamp', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Tentacool', 'Tentacruel', 'Geodude', 'Graveler', 'Golem', 'Ponyta', 'Rapidash', 'Slowpoke', 'Slowbro', 'Magnemite', 'Magneton', 'Doduo', 'Dodrio', 'Seel', 'Dewgong', 'Grimer', 'Muk', 'Shellder', 'Cloyster', 'Gastly', 'Haunter', 'Gengar', 'Onix', 'Drowzee', 'Hypno', 'Krabby', 'Kingler', 'Voltorb', 'Electrode', 'Exeggcute', 'Exeggutor', 'Cubone', 'Marowak', 'Hitmonlee', 'Hitmonchan', 'Lickitung', 'Koffing', 'Weezing', 'Rhyhorn', 'Rhydon', 'Chansey', 'Tangela', 'Kangaskhan', 'Horsea', 'Seadra', 'Goldeen', 'Seaking', 'Staryu', 'Starmie', 'Mr.', 'Mime', 'Scyther', 'Jynx', 'Electabuzz', 'Magmar', 'Pinsir', 'Tauros', 'Magikarp', 'Gyarados', 'Lapras', 'Ditto', 'Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Porygon', 'Omanyte', 'Omastar', 'Kabuto', 'Kabutops', 'Aerodactyl', 'Snorlax', 'Articuno', 'Zapdos', 'Moltres', 'Dratini', 'Dragonair', 'Dragonite', 'Mewtwo', 'Mew'],
                ['Pokemons 2a geração','Chikorita', 'Bayleef', 'Meganium','Cyndaquil', 'Quilava', 'Typhlosion', 'Totodile', 'Croconaw', 'Feraligatr', 'Sentret', 'Furret', 'Hoothoot', 'Noctowl', 'Ledyba', 'Ledian', 'Spinarak', 'Ariados', 'Crobat', 'Chinchou', 'Lanturn', 'Pichu', 'Cleffa', 'Igglybuff', 'Togepi', 'Togetic', 'Natu', 'Xatu', 'Mareep', 'Flaaffy', 'Ampharos', 'Bellossom', 'Marill', 'Azumarill', 'Sudowoodo', 'Politoed', 'Hoppip', 'Skiploom', 'Jumpluff', 'Aipom', 'Sunkern', 'Sunflora', 'Yanma', 'Wooper', 'Quagsire', 'Espeon', 'Umbreon', 'Murkrow', 'Slowking', 'Misdreavus', 'Unown', 'Wobbuffet', 'Girafarig', 'Pineco', 'Forretress', 'Dunsparce', 'Gligar', 'Steelix', 'Snubbull', 'Granbull', 'Qwilfish', 'Scizor', 'Shuckle', 'Heracross', 'Sneasel', 'Teddiursa', 'Ursaring', 'Slugma', 'Magcargo', 'Swinub', 'Piloswine', 'Corsola', 'Remoraid', 'Octillery', 'Delibird', 'Mantine', 'Skarmory', 'Houndour', 'Houndoom', 'Kingdra', 'Phanpy','Donphan', 'Porygon2', 'Stantler', 'Smeargle', 'Tyrogue', 'Hitmontop', 'Smoochum', 'Elekid', 'Magby', 'Miltank', 'Blissey', 'Raikou','Entei', 'Suicune', 'Larvitar','Pupitar', 'Tyranitar','Lugia', 'Ho-oh', 'Celebi'],
                ['Pokemons 3a geração','Treecko', 'Grovyle', 'Sceptile', 'Torchic', 'Combusken', 'Blaziken', 'Mudkip', 'Marshtomp', 'Swampert', 'Poochyena', 'Mightyena', 'Zigzagoon', 'Linoone', 'Wurmple', 'Silcoon', 'Beautifly', 'Cascoon', 'Dustox', 'Lotad', 'Lombre', 'Ludicolo', 'Seedot', 'Nuzleaf', 'Shiftry', 'Taillow', 'Swellow', 'Wingull', 'Pelipper', 'Ralts', 'Kirlia', 'Gardevoir', 'Surskit', 'Masquerain', 'Shroomish', 'Breloom', 'Slakoth', 'Vigoroth', 'Slaking', 'Nincada', 'Ninjask', 'Shedinja', 'Whismur', 'Loudred', 'Exploud', 'Makuhita', 'Hariyama', 'Azurill', 'Nosepass', 'Skitty', 'Delcatty', 'Sableye', 'Mawile', 'Aron', 'Lairon', 'Aggron', 'Meditite', 'Medicham', 'Electrike', 'Manectric', 'Plusle', 'Minun', 'Volbeat', 'Illumise', 'Roselia', 'Gulpin', 'Swalot', 'Carvanha', 'Sharpedo', 'Wailmer', 'Wailord', 'Numel', 'Camerupt', 'Torkoal', 'Spoink', 'Grumpig', 'Spinda', 'Trapinch', 'Vibrava', 'Flygon', 'Cacnea', 'Cacturne', 'Swablu', 'Altaria', 'Zangoose', 'Seviper', 'Lunatone', 'Solrock', 'Barboach', 'Whiscash', 'Corphish', 'Crawdaunt', 'Baltoy', 'Claydol', 'Lileep', 'Cradily', 'Anorith', 'Armaldo', 'Feebas', 'Milotic', 'Castform', 'Kecleon', 'Shuppet', 'Banette', 'Duskull', 'Dusclops', 'Tropius', 'Chimecho', 'Absol', 'Wynaut', 'Snorunt', 'Glalie', 'Spheal', 'Sealeo', 'Walrein', 'Clamperl', 'Huntail', 'Gorebyss', 'Relicanth', 'Luvdisc', 'Bagon', 'Shelgon', 'Salamence', 'Beldum', 'Metang', 'Metagross', 'Regirock', 'Regice', 'Registeel', 'Latias', 'Latios', 'Kyogre', 'Groudon', 'Rayquaza', 'Jirachi', 'Deoxys'],
                ['Pokemons 4a geração','Turtwig', 'Grotle', 'Torterra', 'Chimchar', 'Monferno', 'Infernape', 'Piplup', 'Prinplup', 'Empoleon', 'Starly', 'Staravia', 'Staraptor', 'Bidoof', 'Bibarel', 'Kricketot', 'Kricketune', 'Shinx', 'Luxio', 'Luxray', 'Budew', 'Roserade', 'Cranidos', 'Rampardos', 'Shieldon', 'Bastiodon', 'Burmy', 'Wormadam', 'Mothim', 'Combee', 'Vespiquen', 'Pachirisu', 'Buizel', 'Floatzel', 'Cherubi', 'Cherrim', 'Shellos', 'Gastrodon', 'Ambipom', 'Drifloon', 'Drifblim', 'Buneary', 'Lopunny', 'Mismagius', 'Honchkrow', 'Glameow', 'Purugly', 'Chingling', 'Stunky', 'Skuntank', 'Bronzor', 'Bronzong', 'Bonsly', 'Mime Jr.', 'Happiny', 'Chatot', 'Spiritomb', 'Gible', 'Gabite', 'Garchomp', 'Munchlax', 'Riolu', 'Lucario', 'Hippopotas', 'Hippowdon', 'Skorupi', 'Drapion', 'Croagunk', 'Toxicroak', 'Carnivine', 'Finneon', 'Lumineon', 'Mantyke', 'Snover', 'Abomasnow', 'Weavile', 'Magnezone', 'Lickilicky', 'Rhyperior', 'Tangrowth', 'Electivire', 'Magmortar', 'Togekiss', 'Yanmega', 'Leafeon', 'Glaceon', 'Gliscor', 'Mamoswine', 'Porygon-Z', 'Gallade', 'Probopass', 'Dusknoir', 'Froslass', 'Rotom', 'Uxie', 'Mesprit', 'Azelf', 'Dialga', 'Palkia', 'Heatran', 'Regigigas', 'Giratina', 'Cresselia', 'Phione', 'Manaphy', 'Darkrai', 'Shaymin', 'Arceus'],
                ['Pokemons 5a geração','Victini', 'Snivy', 'Servine', 'Serperior', 'Tepig', 'Pignite', 'Emboar', 'Oshawott', 'Dewott', 'Samurott', 'Patrat', 'Watchog', 'Lillipup', 'Herdier', 'Stoutland', 'Purrloin', 'Liepard', 'Pansage', 'Simisage', 'Pansear', 'Simisear', 'Panpour', 'Simipour', 'Munna', 'Musharna', 'Pidove', 'Tranquill', 'Unfezant', 'Blitzle', 'Zebstrika', 'Roggenrola', 'Boldore', 'Gigalith', 'Woobat', 'Swoobat', 'Drilbur', 'Excadrill', 'Audino', 'Timburr', 'Gurdurr', 'Conkeldurr', 'Tympole', 'Palpitoad', 'Seismitoad', 'Throh', 'Sawk', 'Sewaddle', 'Swadloon', 'Leavanny', 'Venipede', 'Whirlipede', 'Scolipede', 'Cottonee', 'Whimsicott', 'Petilil', 'Lilligant', 'Basculin', 'Sandile', 'Krokorok', 'Krookodile', 'Darumaka', 'Darmanitan', 'Maractus', 'Dwebble', 'Crustle', 'Scraggy', 'Scrafty', 'Sigilyph', 'Yamask', 'Cofagrigus', 'Tirtouga', 'Carracosta', 'Archen', 'Archeops', 'Trubbish', 'Garbodor', 'Zorua', 'Zoroark', 'Minccino', 'Cinccino', 'Gothita', 'Gothorita', 'Gothitelle', 'Solosis', 'Duosion', 'Reuniclus', 'Ducklett', 'Swanna', 'Vanillite', 'Vanillish', 'Vanilluxe', 'Deerling', 'Sawsbuck', 'Emolga', 'Karrablast', 'Escavalier', 'Foongus', 'Amoonguss', 'Frillish', 'Jellicent', 'Alomomola', 'Joltik', 'Galvantula', 'Ferroseed', 'Ferrothorn', 'Klink', 'Klang', 'Klinklang', 'Tynamo', 'Eelektrik', 'Eelektross', 'Elgyem', 'Beheeyem', 'Litwick', 'Lampent', 'Chandelure', 'Axew', 'Fraxure', 'Haxorus', 'Cubchoo', 'Beartic', 'Cryogonal', 'Shelmet', 'Accelgor', 'Stunfisk', 'Mienfoo', 'Mienshao', 'Druddigon', 'Golett', 'Golurk', 'Pawniard', 'Bisharp', 'Bouffalant', 'Rufflet', 'Braviary', 'Vullaby', 'Mandibuzz', 'Heatmor', 'Durant', 'Deino', 'Zweilous', 'Hydreigon', 'Larvesta', 'Volcarona', 'Cobalion', 'Terrakion', 'Virizion', 'Tornadus', 'Thundurus', 'Reshiram', 'Zekrom', 'Landorus', 'Kyurem', 'Keldeo', 'Meloetta', 'Genesect'],
                ['Pokemons 6a geração','Chespin', 'Quilladin', 'Chesnaught', 'Fennekin', 'Braixen', 'Delphox', 'Froakie', 'Frogadier', 'Greninja', 'Bunnelby', 'Diggersby', 'Fletchling', 'Fletchinder', 'Talonflame', 'Scatterbug', 'Spewpa', 'Vivillon', 'Litleo', 'Pyroar', 'Flabébé', 'Floette', 'Florges', 'Skiddo', 'Gogoat', 'Pancham', 'Pangoro', 'Furfrou', 'Espurr', 'Meowstic', 'Honedge', 'Doublade', 'Aegislash', 'Spritzee', 'Aromatisse', 'Swirlix', 'Slurpuff', 'Inkay', 'Malamar', 'Binacle', 'Barbaracle', 'Skrelp', 'Dragalge', 'Clauncher', 'Clawitzer', 'Helioptile', 'Heliolisk', 'Tyrunt', 'Tyrantrum', 'Amaura', 'Aurorus', 'Sylveon', 'Hawlucha', 'Dedenne', 'Carbink', 'Goomy', 'Sliggoo', 'Goodra', 'Klefki', 'Phantump', 'Trevenant', 'Pumpkaboo', 'Gourgeist', 'Bergmite', 'Avalugg', 'Noibat', 'Noivern', 'Xerneas', 'Yveltal', 'Zygarde', 'Diancie', 'Hoopa', 'Volcanion'],
                ['Herois do Dota 2', 'Abaddon', 'Alchemist', 'Ancient Apparition', 'Anti Mage', 'Arc Warden', 'Axe', 'Bane', 'Batrider', 'Beastmaster', 'Bloodseeker', 'Bounty Hunter', 'Brewmaster', 'Bristleback', 'Broodmother', 'Centaur Warrunner', 'Chaos Knight', 'Chen', 'Clinkz', 'Clockwerk', 'Crystal Maiden', 'Dark Seer', 'Dazzle', ',Death Prophet', 'Disruptor', 'Doom', 'Dragon Knight', 'Drow Ranger', 'Earth Spirit', 'Earthshaker', 'Elder Titan', 'Ember Spirit', 'Enchantress', 'Enigma', 'Faceless Void', 'Gyrocopter', 'Huskar', 'Invoker', 'Io', 'Jakiro', 'Juggernaut', 'Keeper of the Light', 'Kunkka', 'Legion Commander', 'Leshrac', 'Lich', 'Lifestealer', 'Lina', 'Lion', 'Lone Druid', 'Luna', 'Lycan', 'Magnus', 'Medusa', 'Meepo', 'Mirana', 'Morphling', ',Naga Siren', 'Natures Prophet', 'Necrophos', 'Night Stalker', 'Nyx Assassin', 'Ogre Magi', 'Omniknight', 'Oracle', 'Outworld Devourer', 'Phantom Assassin', 'Phantom Lancer', 'Phoenix', 'Puck', 'Pudge', 'Pugna', 'Queen of Pain', 'Razor', 'Riki', 'Rubick', 'Sand King', 'Shadow Demon', 'Shadow Fiend', 'Shadow Shaman', 'Silencer', 'Skywrath Mage', 'Slardar', 'Slark', 'Sniper', 'Spectre', 'Spirit Breaker', 'Storm Spirit', 'Sven', 'Techies', 'Templar Assassin', 'Terrorblade', 'Tidehunter', 'Timbersaw', 'Tinker', 'Tiny', 'Treant Protector', 'Troll Warlord', 'Tusk', 'Undying', 'Ursa', 'VengefulSpirit', 'Venomancer', 'Viper', 'Visage', 'Warlock', 'Weaver', 'Windranger', 'Winter Wyvern','Witch Doctor', 'Wraith King','Zeus'],
                ['Campões de League of Legends','Aatrox', 'Ahri', 'Akali', 'Alistar','Amumu','Anivia', 'Annie', 'Ashe', 'Azir', 'Bardo', 'Blitzcrank','Brand', 'Braum', 'Caitlyn', 'Cassiopeia','Cho Gath','Corki', 'Darius', 'Diana', 'Draven', 'Dr Mundo', 'Elise','Evelynn', 'Ezreal', 'Fiddlesticks', 'Fiora', 'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnar', 'Gragas', 'Graves', 'Hecarim','Heimerdinger', 'Illaoi', 'Irelia', 'Janna', 'Jarvan IV', 'Jax', 'Jayce', 'Jhin','Jinx', 'Kalista', 'Karma', 'Karthus', 'Kassadin', 'Katarina', 'Kayle', 'Kennen', 'Kha Zix','Kog Maw', 'LeBlanc', 'Lee Sin', 'Leona', 'Lissandra', 'Lucian', 'Lulu', 'Lux', 'Malphite','Malzahar',  'Maokai', 'Master Yi', 'Miss Fortune', 'Mordekaiser', 'Morgana', 'Nami', 'Nasus', 'Nautilus','Nidalee', 'Nocturne', 'Nunu', 'Olaf', 'Orianna', 'Pantheon', 'Poppy', 'Quinn', 'Rammus',  'Rek Sai','Renekton', 'Rengar', 'Riven',  'Rumble', 'Ryze', 'Sejuani', 'Shaco','Shen', 'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner', 'Sona',  'Soraka', 'Swain', 'Syndra', 'Talon', 'Taric', 'Teemo', 'Thresh', 'Tristana', 'Trundle', 'Tryndamere', 'Twisted Fate', 'Tryndamere', 'Udyr', 'Urgot', 'Varus', 'Vayne', 'Veigar', 'Vel Koz', 'Vi','Viktor', 'Vladimir', 'Volibear', 'Warwick', 'Wukong', 'Xerath','Xin Zhao', 'Yasuo', 'Yorick', 'Zac', 'Zed', 'Ziggs', 'Zilean', 'Zyra'],

            ]
categorias = ''
for i in range(len(palavras)):
    categorias = categorias+palavras[i][0]+'\n'

#Keyboard padrão
att_kb = 'Enviar teclado'

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
sobre = 'Sobre' + emoji_livro
categorias_btn = 'Selecionar categorias' + emoji_ferramenta

#Respostas iniciais
linguas = emoji_planeta + 'Escolha a linguagem:'
iniciar_msg = 'Carregando...'
mudar_lingua = 'Mudança feita com sucesso' + emoji_thumbsUp
start_msg = 'Olá, eu sou o Hangman, mestre de jogos da forca! Meu dever é organizar e jogar jogos da forca e garantir que você se divirta!\nAperte no botão "novo jogo" para começarmos!' + emoji_sorriso
is_enabled = 'Já estou ligado!'
about_msg = 'Sou um projeto de código aberto criado pelo @bcesarg6 e @cristoferoswald! Estou em constante desenvolvimento e você pode me ajudar a crescer contribuindo em https://github.com/bcesarg6/PlayHangmanBot\n\nCategorias:\n'+categorias+'\nVersão 2.0 - KIWI:\n*AGORA COM MAIS DE MIL PALAVRAS!*\n\t- Adicionado tradução em hebreu (agradecimento especial para @Shushishtok)\n\t- Adicionado sistema de seleção de categorias!\n\t- Adicionado 5 novas categorias de Pokémon e categorias de Dota 2 e League of Legends\n\nAtualizações futuras:\n\t- Recurso remover jogador da partda\n\t- Novos modos de jogo\n\t- Ranking global\n\nSinta-se a vontade para se juntar a equipe!' + emoji_sorriso
stop_msg = 'Desligado'
start_help_msg = 'Não há nenhum jogo em andamento, clique no botão "novo jogo" para começar um jogo ou veja o ranking no botão "Rank".\nVocê também pode alterar as configurações se desejar' + emoji_sorriso + '\nLembre-se se você precisar do telcado envie /kb'
config_help_msg = 'Escolha a minha lingua. ATENÇÃO: As palavras do jogo dependem da língua escolhida\nNão encontrou sua lingua? Você pode ajudar no meu desenvolvimento adicionando uma tradução, clique em Sobre para mais informações\nLembre-se se você precisar do telcado envie /kb'
voltar_msg = 'Menu inicial'
cantdo_msg = 'Você não pode fazer isso'
comandos_msg = 'Comandos'
ocupado_msg = 'Estou ocupado agora, desculpe' + emoji_triste + ' Por favor, selecione sua linguagem primeiro, mande /kb para ver o teclado'
teclado_msg = 'Teclado'
ranking_msg = emoji_coroa + ' RANKING ' + emoji_coroa
error_msg = 'Um erro ocorreu, por favor entre em contato com @cristoferoswald ou @bcesarg6 e reporte o ocorrido' + emoji_triste
sorry_msg = 'Desculpe, o que você disse?'

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
pre_game_help_msg = 'Jogo em modo de entrada, clique em Entrar para participar\nADM: Clique em "Começar jogo" para começar com os participantes atuais\nLembre-se se você precisar do telcado envie /kb '

cat_msg = 'Selecione as categorias das palavras que você deseja em seu jogo, para selecionar basta digitar o(s) número(s) correspondente(s) das categorias separados por espaços!\n\nCATEGORIAS:\n'
for i in range(len(palavras)):
        cat_msg = cat_msg +'\t '+str(i+1)+' - '+palavras[i][0]+'\n'

cat_msg = cat_msg + 'Para jogar com todas as categorias digite apenas 0\nSua configuração ficará salva!\nExemplo: 1 3 5 8 13'

cat_erro_msg = 'Erro ao selecionar as categorias!' + emoji_heartb + '\nTenha certeza que não inseriu letras, palavras ou simbolos!\nExemplo: 1 3 5 8 13\nOu apenas 0 para o padrão (Selecionar todas)' + emoji_blink
categorias_msg = 'Feito! Bom jogo!' + emoji_sorriso

def novoAdmMsg(u_name):
    return 'Um novo administrador foi definido! '+u_name+' é o novo administrador.' + emoji_oculos

def playerQuitMsg(u_name):
    return 'O jogador '+u_name+' saiu da partida.' + emoji_triste

def entrarMsg(u_name):
    return 'Ok '+u_name+', você vai participar dessa rodada' + emoji_blink

#repostas InGame
in_game_help_msg = 'Clique nas letras para chuta-las ou em Arriscar se você acha que já descobriu a palavra secreta!' + '\nLembre-se se você precisar do telcado envie /kb'
arriscar_msg = 'Então você acha que já descobriu qual é a palavra? ' + emoji_zoando + ' Me mande a palavra, mas pense bem, se você errar será eliminado!' + emoji_lua
round_errado_msg = 'Não é a sua vez de jogar, espere a sua vez!' + emoji_lua
acertou_letra_msg = 'Você acertou!' + emoji_claps
errou_letra_msg = 'Errou' + emoji_triste + emoji_heartb
jachutada_msg = 'Essa letra já foi chutada' + emoji_surpreso
umavida_msg = 'Somente uma vida restante! Descubra a palavra ou aceite sua DERROTA!' + emoji_lua
gameover_msg = emoji_poop + ' PERDERAM, FIM DE JOGO ' + emoji_poop
fora_msg = 'Você não participa dessa rodada, espere ela acabar para participar de um novo'

def googleMsg(palavra):
    palavras = palavra.split(' ')
    palavra = ''
    for i in range(len(palavras)):
        palavra = palavra + palavras[i] +'%20'
    return ('Descubra: https://google.com/#q='+palavra).encode('utf-8')

def perdeu(u_name):
    return u_name + ' arriscou e errou! O jogador foi eliminado!' + emoji_lua

def nextPlayer(u_name):
    return 'Vez de ' + u_name + ' ' + emoji_point

def venceu(u_name):
    return emoji_confetti + ' Parabéns ' + u_name + ' você descobriu a palavra secreta e ganhou o jogo! ' + emoji_confetti + '\n Pontos calculados e ranking atualizado! ' + emoji_sorriso
