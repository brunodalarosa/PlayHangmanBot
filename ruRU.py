#-*- coding: utf-8 -*-
#Linguagem Inglês, contém as strings que serão lidas para aparecerem no jogo

#Emojis
from emojis import *

#palavras
palavras = [
["Плоды", "Ягоды асаи", "Яблоко", "Абрикос", "Авокадо", "Банана", "Черника", "Ежевика", "Черная смородина", "Черника", "Бойзенова ягода", "Канталупа",
"Смородина", "Вишня", "Черимойя", "Морошка", "Кокос", "Клюква", "Тернослива", "Питайя", "Дуриан", "Бузина", "Фейхоа", "Фига", "Ягоды годжи", "Крыжовник", "Виноград", "Изюм", "Грейпфрут", "Гуава",
"Хаклберри", "Жаботикаба", "Джекфрут", "Джамболан", "Зизифус", "Ягоды можжевельника", "Киви", "Кивано", "Кумкват", "Лимон", "Лайм", "Личи", "Манго", "Ежевика марион", "Дыня", "Канталупа", "Медовая дыня", "Арбуз", "Путерия", "Шелковица",
"Нектарин", "Олива", "Апельсин", "Красный апельсин", "Клементина", "Мандарин", "Танжерин", "Папайя", "Страстоцвет", "Персик", "Груша", "Хурма", "Физалис", "Ананас", "Тыква", "Гранат", "Помело", "Мангостан", "Айва", "Малина", "Малина великолепная",
"Малина западная", "Рамбутан", "Красная смородина", "Гаультерия шаллон", "Мандарин уншиу", "Звёздчатое яблоко", "Карамбола", "Клубника", "Сквош", "Тамарилло", "Томат", "Агли"],
['Страны', 'Афганистан', 'Албания', 'Алжир', 'Андорра', 'Ангола', 'Аргентина', "Армения", "Аруба", "Австралия", "Австрия", "Азербайджан", "Бахрейн",
"Бангладеш", "Барбадос", "Беларусь", "Бельгия", "Белиз", "Бенин", "Бутан", "Боливия", "Босния и Герцеговина", "Ботсвана", "Бразилия", "Бруней", "Болгария", "Бурунди", "Буркина-Фасо", "Бирма", "Бурунди",
"Камбоджа", "Камерун", "Канада", "Чад", "Чили", "Китай", "Колумбия", "Республика Конго", "Коста-Рика", "Хорватия", "Куба", "Кипр" ,'Чешская Республика',
"Дания", "Джибути", "Доминика", "Доминиканская Республика", "Эквадор", "Египет", "Сальвадор", "Экваториальная Гвинея", "Эстония", "Эфиопия", "Фиджи", "Франция", "Грузия", "Германия", "Гана", "Греция", "Гватемала", "Гвинея", "Гайана",
"Исландия", "Индия", "Индонезия", "Иран", "Ирак", "Ирландия", "Израиль", "Италия", "Португалия", "Парагвай", "Филиппины", "Новая Зеландия", "Мексика ","Мадагаскар", "Перу", "Россия", "Сербия", "Испания", "Судан", "Швеция"]
["Профессии", "Бухгалтер", "Актер", "Секретарь", "Археолог", "Архитектор", "Астроном", "Аудитор", "Автор", "Пекарь", "Бариста", "Бухгалтер", "Ботаник" "Каменщик", "Мясник", "Кардиолог", "Столяр", "Химик", "Хиропрактик", "Консьерж", "Повар", "Чистильщик", "Стоматолог", "Дизайнер", "Доктор", "Электрик", "Инженер", "Фермер", "Пожарный", "Рыбак", "Флорист", "Садовник", "Парикмахер", "Журналист", "Судья", "Адвокат", "Лектор", "Библиотекарь", "Озранник", "Механик", "Модель", "Диктор", "Медсестра", "Оптик", "Художник", "Фармацевт", "Фотограф", "Пилот", "Водопроводчик", "Политик", "Милиционер",
 "Почтальон", "Портье", "Ученый", "Министр", "Продавец", "Солдат", "Портной", "Таксист", "Учитель", "Переводчик", "Путешественник", "Ветеринар", "Официант", "Зоолог"],
['Герои и злодеи','Бэтмэн','Флэш','Чудо-женщина','Пингвин','Супермэн','Зеленый фонарь','Зеленый гоблин','Человек-паук','Тор','Халк','Железный человек','Человек-муравей','Человек-факел','Нечто','Черная вдова','Зеленая стрела','Грут','Ракета','Магнето','Логан','Шторм'],
# usually not translated into Russian
['Игры и видеоигры','The Legend of Zelda','Super Mario','Counter Strike','Nintendo Wii','Super Nintendo','Playstation','Steam','Defense of the Ancients','League of Legends','Final Fantasy','Donkey Kong','Angry Birds','Fallout','Bioshock','Тетрис','The Elder Scrolls','Minecraft','Call of Duty','Battlefield','Bomberman','Sonic the Hedgehog','Just Dance','Nintendo','Sony','Sega','Dreamcast'],
# In the left arm there's Sniker's, 
# In the right arm there's Mars
# My PR-manager...
['Великие люди','Фрэнсис Бэкон','Джон Локк','Жан Жак Руссо','Христофор Колумб','Педру Алвариш Кабрал','Никколо Макиавелли','Джордано Бруно','Леонардо Да Винчи','Рене Декарт','Исаан Ньютон','Галилео Галилей','Алан Тьюринг','Махатма Ганди','Мартин Лютер Кинг','Карл Маркс' ,'Фридрих Ницше','Альберт Энштейн','Барак Обама','Авраам Линкольн','Никола Тесла','Зигмунд Фрейд','Карл Саган','Ларри Пейдж','Стив Джобс','Марк Цукерберг','Тим Кук','Чарльз Чаплин','Платон','Аристотель','Дилма Русеф','Луис Инасиу Лула да Силва','Фернанду Энрики Кардозу','Джордж Вашингтон','Джордж Уокер Буш','Адольф Гитлер','Сигэру Миямото','Нил Деграсс Тайсон'],
['Фильмы и сериалы', 'Во все тяжкие', 'Как я встретил вашу маму','Восьмое чувство', 'Красота по-американски','Донни Дарко','Один дома','Шестое чувство','Сияние','Титаник','Все ненавидят Криса','Безумный шляпник','Алиса в Стране Чудес','Гарри Поттер','Время приключений','Губка Боб','Нарко','Ананасовый экспресс','Покемон','Yugioh','Гермиона','Волан-де-Морт','Драко Малфой','Китнисс Эвердин','Голодные игры', 'Сойка-пересмешница', 'И вспыхнет пламя', 'Экзорцист', 'Область тьмы', 'Мальчишник в Вегасе', 'Матрицы', 'Властелин колец', 'Хоббит','Фродо Бэггинс', 'Саурон', 'Леголас','Гэндальф', 'Альбус Дамблдор','Звездные войны','Люк Скайуокер','Чубакка', 'Йода'],
# If these pockemoon names are from Pockemon Go, then they shouldn't be translated
['Покемоны 1 поколения', 'Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard', 'Squirtle', 'Wartortle', 'Blastoise', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill', 'Pidgey', 'Pidgeotto', 'Pidgeot', 'Rattata', 'Raticate', 'Spearow', 'Fearow', 'Ekans', 'Arbok', 'Pikachu', 'Raichu', 'Sandshrew', 'Sandslash', 'Nidoran', 'Nidorina', 'Nidoqueen', 'Nidorino', 'Nidoking', 'Clefairy', 'Clefable', 'Vulpix', 'Ninetales', 'Jigglypuff', 'Wigglytuff', 'Zubat', 'Golbat', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 'Venonat', 'Venomoth', 'Diglett', 'Dugtrio', 'Meowth', 'Persian', 'Psyduck', 'Golduck', 'Mankey', 'Primeape', 'Growlithe', 'Arcanine', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Abra', 'Kadabra', 'Alakazam', 'Machop', 'Machoke', 'Machamp', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Tentacool', 'Tentacruel', 'Geodude', 'Graveler', 'Golem', 'Ponyta', 'Rapidash', 'Slowpoke', 'Slowbro', 'Magnemite', 'Magneton', 'Doduo', 'Dodrio', 'Seel', 'Dewgong', 'Grimer', 'Muk', 'Shellder', 'Cloyster', 'Gastly', 'Haunter', 'Gengar', 'Onix', 'Drowzee', 'Hypno', 'Krabby', 'Kingler', 'Voltorb', 'Electrode', 'Exeggcute', 'Exeggutor', 'Cubone', 'Marowak', 'Hitmonlee', 'Hitmonchan', 'Lickitung', 'Koffing', 'Weezing', 'Rhyhorn', 'Rhydon', 'Chansey', 'Tangela', 'Kangaskhan', 'Horsea', 'Seadra', 'Goldeen', 'Seaking', 'Staryu', 'Starmie', 'Mr.', 'Mime', 'Scyther', 'Jynx', 'Electabuzz', 'Magmar', 'Pinsir', 'Tauros', 'Magikarp', 'Gyarados', 'Lapras', 'Ditto', 'Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Porygon', 'Omanyte', 'Omastar', 'Kabuto', 'Kabutops', 'Aerodactyl', 'Snorlax', 'Articuno', 'Zapdos', 'Moltres', 'Dratini', 'Dragonair', 'Dragonite', 'Mewtwo', 'Mew'],
['Покемоны 2 поколения','Chikorita', 'Bayleef', 'Meganium', 'Cyndaquil', 'Quilava', 'Typhlosion', 'Totodile', 'Croconaw', 'Feraligatr', 'Sentret', 'Furret', 'Hoothoot', 'Noctowl', 'Ledyba', 'Ledian', 'Spinarak', 'Ariados', 'Crobat', 'Chinchou', 'Lanturn', 'Pichu', 'Cleffa', 'Igglybuff', 'Togepi', 'Togetic', 'Natu', 'Xatu', 'Mareep', 'Flaaffy', 'Ampharos', 'Bellossom', 'Marill', 'Azumarill', 'Sudowoodo', 'Politoed', 'Hoppip', 'Skiploom', 'Jumpluff', 'Aipom', 'Sunkern', 'Sunflora', 'Yanma', 'Wooper', 'Quagsire', 'Espeon', 'Umbreon', 'Murkrow', 'Slowking', 'Misdreavus', 'Unown', 'Wobbuffet', 'Girafarig', 'Pineco', 'Forretress', 'Dunsparce', 'Gligar', 'Steelix', 'Snubbull', 'Granbull', 'Qwilfish', 'Scizor', 'Shuckle', 'Heracross', 'Sneasel', 'Teddiursa', 'Ursaring', 'Slugma', 'Magcargo', 'Swinub', 'Piloswine', 'Corsola', 'Remoraid', 'Octillery', 'Delibird', 'Mantine', 'Skarmory', 'Houndour', 'Houndoom', 'Kingdra', 'Phanpy', 'Donphan', 'Porygon2', 'Stantler', 'Smeargle', 'Tyrogue', 'Hitmontop', 'Smoochum', 'Elekid', 'Magby', 'Miltank', 'Blissey', 'Raikou', 'Entei', 'Suicune', 'Larvitar', 'Pupitar', 'Tyranitar', 'Lugia', 'Ho oh', 'Celebi'],
['Покемоны 3 поколения','Treecko', 'Grovyle', 'Sceptile', 'Torchic', 'Combusken', 'Blaziken', 'Mudkip', 'Marshtomp', 'Swampert', 'Poochyena', 'Mightyena', 'Zigzagoon', 'Linoone', 'Wurmple', 'Silcoon', 'Beautifly', 'Cascoon', 'Dustox', 'Lotad', 'Lombre', 'Ludicolo', 'Seedot', 'Nuzleaf', 'Shiftry', 'Taillow', 'Swellow', 'Wingull', 'Pelipper', 'Ralts', 'Kirlia', 'Gardevoir', 'Surskit', 'Masquerain', 'Shroomish', 'Breloom', 'Slakoth', 'Vigoroth', 'Slaking', 'Nincada', 'Ninjask', 'Shedinja', 'Whismur', 'Loudred', 'Exploud', 'Makuhita', 'Hariyama', 'Azurill', 'Nosepass', 'Skitty', 'Delcatty', 'Sableye', 'Mawile', 'Aron', 'Lairon', 'Aggron', 'Meditite', 'Medicham', 'Electrike', 'Manectric', 'Plusle', 'Minun', 'Volbeat', 'Illumise', 'Roselia', 'Gulpin', 'Swalot', 'Carvanha', 'Sharpedo', 'Wailmer', 'Wailord', 'Numel', 'Camerupt', 'Torkoal', 'Spoink', 'Grumpig', 'Spinda', 'Trapinch', 'Vibrava', 'Flygon', 'Cacnea', 'Cacturne', 'Swablu', 'Altaria', 'Zangoose', 'Seviper', 'Lunatone', 'Solrock', 'Barboach', 'Whiscash', 'Corphish', 'Crawdaunt', 'Baltoy', 'Claydol', 'Lileep', 'Cradily', 'Anorith', 'Armaldo', 'Feebas', 'Milotic', 'Castform', 'Kecleon', 'Shuppet', 'Banette', 'Duskull', 'Dusclops', 'Tropius', 'Chimecho', 'Absol', 'Wynaut', 'Snorunt', 'Glalie', 'Spheal', 'Sealeo', 'Walrein', 'Clamperl', 'Huntail', 'Gorebyss', 'Relicanth', 'Luvdisc', 'Bagon', 'Shelgon', 'Salamence', 'Beldum', 'Metang', 'Metagross', 'Regirock', 'Regice', 'Registeel', 'Latias', 'Latios', 'Kyogre', 'Groudon', 'Rayquaza', 'Jirachi', 'Deoxys'],
['Покемоны 4 поколения','Turtwig', 'Grotle', 'Torterra', 'Chimchar', 'Monferno', 'Infernape', 'Piplup', 'Prinplup', 'Empoleon', 'Starly', 'Staravia', 'Staraptor', 'Bidoof', 'Bibarel', 'Kricketot', 'Kricketune', 'Shinx', 'Luxio', 'Luxray', 'Budew', 'Roserade', 'Cranidos', 'Rampardos', 'Shieldon', 'Bastiodon', 'Burmy', 'Wormadam', 'Mothim', 'Combee', 'Vespiquen', 'Pachirisu', 'Buizel', 'Floatzel', 'Cherubi', 'Cherrim', 'Shellos', 'Gastrodon', 'Ambipom', 'Drifloon', 'Drifblim', 'Buneary', 'Lopunny', 'Mismagius', 'Honchkrow', 'Glameow', 'Purugly', 'Chingling', 'Stunky', 'Skuntank', 'Bronzor', 'Bronzong', 'Bonsly', 'Mime Jr.', 'Happiny', 'Chatot', 'Spiritomb', 'Gible', 'Gabite', 'Garchomp', 'Munchlax', 'Riolu', 'Lucario', 'Hippopotas', 'Hippowdon', 'Skorupi', 'Drapion', 'Croagunk', 'Toxicroak', 'Carnivine', 'Finneon', 'Lumineon', 'Mantyke', 'Snover', 'Abomasnow', 'Weavile', 'Magnezone', 'Lickilicky', 'Rhyperior', 'Tangrowth', 'Electivire', 'Magmortar', 'Togekiss', 'Yanmega', 'Leafeon', 'Glaceon', 'Gliscor', 'Mamoswine', 'Porygon-Z', 'Gallade', 'Probopass', 'Dusknoir', 'Froslass', 'Rotom', 'Uxie', 'Mesprit', 'Azelf', 'Dialga', 'Palkia', 'Heatran', 'Regigigas', 'Giratina', 'Cresselia', 'Phione', 'Manaphy', 'Darkrai', 'Shaymin', 'Arceus'],
['Покемоны 5 поколения','Victini', 'Snivy', 'Servine', 'Serperior', 'Tepig', 'Pignite', 'Emboar', 'Oshawott', 'Dewott', 'Samurott', 'Patrat', 'Watchog', 'Lillipup', 'Herdier', 'Stoutland', 'Purrloin', 'Liepard', 'Pansage', 'Simisage', 'Pansear', 'Simisear', 'Panpour', 'Simipour', 'Munna', 'Musharna', 'Pidove', 'Tranquill', 'Unfezant', 'Blitzle', 'Zebstrika', 'Roggenrola', 'Boldore', 'Gigalith', 'Woobat', 'Swoobat', 'Drilbur', 'Excadrill', 'Audino', 'Timburr', 'Gurdurr', 'Conkeldurr', 'Tympole', 'Palpitoad', 'Seismitoad', 'Throh', 'Sawk', 'Sewaddle', 'Swadloon', 'Leavanny', 'Venipede', 'Whirlipede', 'Scolipede', 'Cottonee', 'Whimsicott', 'Petilil', 'Lilligant', 'Basculin', 'Sandile', 'Krokorok', 'Krookodile', 'Darumaka', 'Darmanitan', 'Maractus', 'Dwebble', 'Crustle', 'Scraggy', 'Scrafty', 'Sigilyph', 'Yamask', 'Cofagrigus', 'Tirtouga', 'Carracosta', 'Archen', 'Archeops', 'Trubbish', 'Garbodor', 'Zorua', 'Zoroark', 'Minccino', 'Cinccino', 'Gothita', 'Gothorita', 'Gothitelle', 'Solosis', 'Duosion', 'Reuniclus', 'Ducklett', 'Swanna', 'Vanillite', 'Vanillish', 'Vanilluxe', 'Deerling', 'Sawsbuck', 'Emolga', 'Karrablast', 'Escavalier', 'Foongus', 'Amoonguss', 'Frillish', 'Jellicent', 'Alomomola', 'Joltik', 'Galvantula', 'Ferroseed', 'Ferrothorn', 'Klink', 'Klang', 'Klinklang', 'Tynamo', 'Eelektrik', 'Eelektross', 'Elgyem', 'Beheeyem', 'Litwick', 'Lampent', 'Chandelure', 'Axew', 'Fraxure', 'Haxorus', 'Cubchoo', 'Beartic', 'Cryogonal', 'Shelmet', 'Accelgor', 'Stunfisk', 'Mienfoo', 'Mienshao', 'Druddigon', 'Golett', 'Golurk', 'Pawniard', 'Bisharp', 'Bouffalant', 'Rufflet', 'Braviary', 'Vullaby', 'Mandibuzz', 'Heatmor', 'Durant', 'Deino', 'Zweilous', 'Hydreigon', 'Larvesta', 'Volcarona', 'Cobalion', 'Terrakion', 'Virizion', 'Tornadus', 'Thundurus', 'Reshiram', 'Zekrom', 'Landorus', 'Kyurem', 'Keldeo', 'Meloetta', 'Genesect'],
['Покемоны 6 поколения','Chespin', 'Quilladin', 'Chesnaught', 'Fennekin', 'Braixen', 'Delphox', 'Froakie', 'Frogadier', 'Greninja', 'Bunnelby', 'Diggersby', 'Fletchling', 'Fletchinder', 'Talonflame', 'Scatterbug', 'Spewpa', 'Vivillon', 'Litleo', 'Pyroar', 'Flabébé', 'Floette', 'Florges', 'Skiddo', 'Gogoat', 'Pancham', 'Pangoro', 'Furfrou', 'Espurr', 'Meowstic', 'Honedge', 'Doublade', 'Aegislash', 'Spritzee', 'Aromatisse', 'Swirlix', 'Slurpuff', 'Inkay', 'Malamar', 'Binacle', 'Barbaracle', 'Skrelp', 'Dragalge', 'Clauncher', 'Clawitzer', 'Helioptile', 'Heliolisk', 'Tyrunt', 'Tyrantrum', 'Amaura', 'Aurorus', 'Sylveon', 'Hawlucha', 'Dedenne', 'Carbink', 'Goomy', 'Sliggoo', 'Goodra', 'Klefki', 'Phantump', 'Trevenant', 'Pumpkaboo', 'Gourgeist', 'Bergmite', 'Avalugg', 'Noibat', 'Noivern', 'Xerneas', 'Yveltal', 'Zygarde', 'Diancie', 'Hoopa', 'Volcanion'],
['Герои Dota 2', 'Abaddon', 'Alchemist', 'Ancient Apparition', 'Anti Mage', 'Arc Warden', 'Axe', 'Bane', 'Batrider', 'Beastmaster', 'Bloodseeker', 'Bounty Hunter', 'Brewmaster', 'Bristleback', 'Broodmother', 'Centaur Warrunner', 'Chaos Knight', 'Chen', 'Clinkz', 'Clockwerk', 'Crystal Maiden', 'Dark Seer', 'Dazzle', 'Death Prophet', 'Disruptor', 'Doom', 'Dragon Knight', 'Drow Ranger', 'Earth Spirit', 'Earthshaker', 'Elder Titan', 'Ember Spirit', 'Enchantress', 'Enigma', 'Faceless Void', 'Gyrocopter', 'Huskar', 'Invoker', 'Io', 'Jakiro', 'Juggernaut', 'Keeper of the Light', 'Kunkka', 'Legion Commander', 'Leshrac', 'Lich', 'Lifestealer', 'Lina', 'Lion', 'Lone Druid', 'Luna', 'Lycan', 'Magnus', 'Medusa', 'Meepo', 'Mirana', 'Morphling', 'Naga Siren', 'Natures Prophet', 'Necrophos', 'Night Stalker', 'Nyx Assassin', 'Ogre Magi', 'Omniknight', 'Oracle', 'Outworld Devourer', 'Phantom Assassin', 'Phantom Lancer', 'Phoenix', 'Puck', 'Pudge', 'Pugna', 'Queen of Pain', 'Razor', 'Riki', 'Rubick', 'Sand King', 'Shadow Demon', 'Shadow Fiend', 'Shadow Shaman', 'Silencer', 'Skywrath Mage', 'Slardar', 'Slark', 'Sniper', 'Spectre', 'Spirit Breaker', 'Storm Spirit', 'Sven', 'Techies', 'Templar Assassin', 'Terrorblade', 'Tidehunter', 'Timbersaw', 'Tinker', 'Tiny', 'Treant Protector', 'Troll Warlord', 'Tusk', 'Undying', 'Ursa', 'VengefulSpirit', 'Venomancer', 'Viper', 'Visage', 'Warlock', 'Weaver', 'Windranger', 'Winter Wyvern','Witch Doctor', 'Wraith King','Zeus'],
['League of Legends Champions','Aatrox', 'Ahri', 'Akali', 'Alistar','Amumu','Anivia', 'Annie', 'Ashe', 'Azir', 'Bardo', 'Blitzcrank','Brand', 'Braum', 'Caitlyn', 'Cassiopeia','Cho Gath','Corki', 'Darius', 'Diana', 'Draven', 'Dr Mundo', 'Elise','Evelynn', 'Ezreal', 'Fiddlesticks', 'Fiora', 'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnar', 'Gragas', 'Graves', 'Hecarim','Heimerdinger', 'Illaoi', 'Irelia', 'Janna', 'Jarvan IV', 'Jax', 'Jayce', 'Jhin','Jinx', 'Kalista', 'Karma', 'Karthus', 'Kassadin', 'Katarina', 'Kayle', 'Kennen', 'Kha Zix','Kog Maw', 'LeBlanc', 'Lee Sin', 'Leona', 'Lissandra', 'Lucian', 'Lulu', 'Lux', 'Malphite','Malzahar',  'Maokai', 'Master Yi', 'Miss Fortune', 'Mordekaiser', 'Morgana', 'Nami', 'Nasus', 'Nautilus','Nidalee', 'Nocturne', 'Nunu', 'Olaf', 'Orianna', 'Pantheon', 'Poppy', 'Quinn', 'Rammus',  'Rek Sai','Renekton', 'Rengar', 'Riven',  'Rumble', 'Ryze', 'Sejuani', 'Shaco','Shen', 'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner', 'Sona',  'Soraka', 'Swain', 'Syndra', 'Talon', 'Taric', 'Teemo', 'Thresh', 'Tristana', 'Trundle', 'Tryndamere', 'Twisted Fate', 'Tryndamere', 'Udyr', 'Urgot', 'Varus', 'Vayne', 'Veigar', 'Vel Koz', 'Vi','Viktor', 'Vladimir', 'Volibear', 'Warwick', 'Wukong', 'Xerath','Xin Zhao', 'Yasuo', 'Yorick', 'Zac', 'Zed', 'Ziggs', 'Zilean', 'Zyra'],

    ]

categorias = ''
for i in range(len(palavras)):
    categorias = categorias+palavras[i][0]+'\n'

#Keyaboar padrão
att_kb = 'Открыть клавиатуру'

#Botões dos Keyboards
novojogo = 'Новая игра' + emoji_joystick
ajuda = 'Помощь' + emoji_light
rank = 'Рейтинг' + emoji_trofeu
ligar = 'Старт' + emoji_foguete
desligar = 'Стоп' + emoji_x
config = 'Настройки' + emoji_ferramenta
voltar = 'Назад' + emoji_back
cancelar = 'Отменить' + emoji_x
comandos = 'Управление' + emoji_light
entrar = 'Присоединиться' + emoji_foguete
sair = 'Выйти' + emoji_x
fechar_jogo = 'Начать игру' + emoji_foguete
cancelar_jogo = 'Закончить игру' + emoji_x
arriscar = 'Слово!' + emoji_gritar
esta_fora = 'Вы вышли из игры' + emoji_proibido
sobre = 'Информация' + emoji_livro
categorias_btn = 'Выберите категории' + emoji_ferramenta

#Respostas iniciais
linguas = emoji_planeta + 'Выберите язык:'
iniciar_msg = 'Подождите...'
mudar_lingua = 'Язык успешно изменен' + emoji_thumbsUp
start_msg = 'Привет, меня зовут Hangman, я мастер игры в "Виселицу"! У меня есть много вариантов игры в "Виселицу" для тебя и твоих друзей! Будет весело!\n Нажми кнопку "новая игра", и мы начнем!' + emoji_sorriso
is_enabled = 'Я уже готов!'
stop_msg = 'Выключаю...'
about_msg = 'Я -- проект с открытым исходным кодом, созданный слвместно @bcesarg6 и @cristoferoswald! В данный момент я еще нахожусь в разработке и ты можешь помочь мне, мой код здесь: github.com/bcesarg6/PlayHangmanBot\n\nКатегории:\n'+categorias+'\nVersion 2.0 - KIWI:\n*УЖЕ БОЛЕЕ 1K СЛОВ!*\n\t- Добавлен язык иврит (отдельное спасибо @Shushishtok)\n\t-  Добавлена система выбора категорий\n\t- 5 Добавлены новые категории: Pokémon Gens, Dota 2 и League of legends \n\nБудущие обновления:\n\t- Система выбивания игроков\n\t- Глобальный рейтинг\n\t- Новые моды игры!\n\nВступай в нашу прекрасную команду разработчиков!' + emoji_sorriso
start_help_msg = 'В данный момент не начато ни одной игры, нажми на кнопку "Новая игра", чтобы начать, или нажми "Рейтинг", чтобы увидеть рейтинг.\n Также можно изменить настройки игры' + emoji_sorriso + '\nДля вызова клавиатуры нажми /kb'
config_help_msg = 'Нужно выбрать язык игры. Скрытые слова в игре зависят от выбранного языка.\nНе нашел свой язык? Ты можешь помочь добавить в игру свой язык! Гажми кнопку "Информация" для подробностей.\nДля вызова клавиатуры нажми /kb'
voltar_msg = 'Главное меню'
cantdo_msg = 'Этого сделать нельзя'
comandos_msg = 'Комманды'
ocupado_msg = 'Извини, я сейчас занят' + emoji_triste + ' Пожалуйста, выбери язык игры и нажми /kb для показа клавиатуры'
teclado_msg = 'Клавиатура'
ranking_msg = emoji_coroa + ' РЕЙТИНГ ' + emoji_coroa
error_msg = 'Возникла ошибка, пожалуйста, свяжись с @cristoferoswald или @bcesarg6, и мы ее исправим' + emoji_triste
sorry_msg = 'Извини, что ты сказал?'

#respostas PreGame
def inicialMsg(u_name):
    return 'Начинаем новую игру! \n'+u_name+' будет админом этой игре.' + emoji_oculos

inicial_msg = 'начнем собирать игроков, кто хочет грать, нажмите кнопку "Присоединиться"!'+emoji_sorriso
close_game_msg = 'Игра начинается! В свой ход нажми на букву, чтобы отгадать ее, или нажми клавишу "Слово!", если считаешь, что отгадал слово. Но будь осторожен, после этого пути назад нет!'+emoji_zoando+'\n Мы будем играть в следующем порядке:'
palavra_msg = 'Скрытое слово: '
categoria_msg = 'Категория: '
esta_dentro_msg = 'Ты уже присоединился к этой партии!'
sem_jogador_msg = 'В игре никого не осталось, придется отменить игру ' + emoji_surpreso
cancelar_jogo_msg = 'Игра закрыта админом'
is_out_msg = 'Ты не играешь в данной партии' + emoji_lua
vidas_msg = 'Жизни: '
pre_game_help_msg = 'Нам нужны люди для игры, нажимай "Присоединиться", чтобы играть с нами! \nАдмин: Нажми "Начать игру", чтобы начать партию с пришедшими игроками'

cat_msg = 'Теперь нужно выбрать категории для игры. Отправь мне номера выбранных категорий, разделенные пробелами\n\nCATEGORIES:\n'
for i in range(len(palavras)):
        cat_msg = cat_msg +'\t '+str(i+1)+' - '+palavras[i][0]+'\n'

cat_msg = cat_msg + 'Чтобы выбрать сразу все категории, просто отправь 0\nВыбор категорий на игру поменять нельзя!\n Пример: 1 3 5 8 13'

cat_erro_msg = 'Ошибка!' + emoji_heartb + '\nУбедись, что в сообщении нет ничего, кроме номеров категорий!\nпример: 1 3 5 8 13\nили только 0 для выбора всех категорий' + emoji_blink
categorias_msg = 'Блестящая игра!' + emoji_sorriso


def novoAdmMsg(u_name):
    return 'Выбран новый админ! '+u_name+' новый админ.' + emoji_oculos

def playerQuitMsg(u_name):
    return 'Игрок '+u_name+' вышел из игры.' + emoji_triste

def entrarMsg(u_name):
    return 'Хорошо, '+u_name+', ты будешь играть' + emoji_blink

#repostas InGame
in_game_help_msg = 'Нажми на букву, чтобы отгадать ее, или нажми клавишу "Слово!", если считаешь, что отгадал слово.\nДля вызова клавиатуры нажми /kb'
arriscar_msg = 'Ты думаешь, что отгадал скрытое слово? ' + emoji_zoando + ' Тогда отправь мне это слово, но хорошо перед этим подумай, если ты неправ, ты проиграешь!' + emoji_lua
round_errado_msg = 'Сейчас не Ваш ход!' + emoji_lua
acertou_letra_msg = 'Такая буква есть!' + emoji_claps
errou_letra_msg = 'Такой буквы нет' + emoji_triste + emoji_heartb
jachutada_msg = 'Эту букву уже называли' + emoji_surpreso
umavida_msg = 'Осталась одна жизнь! Отгадай скрытое слово или прими ПОРАЖЕНИЕ! (МУХАХА)' + emoji_lua
gameover_msg = emoji_poop + ' ИГРА ОКОНЧЕНА, НЕУДАЧНИКИ! ' + emoji_poop
fora_msg = 'Эта игра уже идет, дождись окончаня этой игры или начни новую!'


def googleMsg(palavra):
    palavras = palavra.split(' ')
    palavra = ''
    for i in range(len(palavras)):
        palavra = palavra + palavras[i] +'%20'
    return ('Информация о слове: https://google.com/#q=' + palavra).encode('utf-8')

def perdeu(u_name):
    return u_name + ' поставил все и проиграл! Игрок покидает игру!' + emoji_lua

def nextPlayer(u_name):
    return 'Ход игрока ' + u_name + emoji_point

def venceu(u_name):
    return emoji_confetti + ' Поздравляем, ' + u_name + ', ты отгадал скрытое слово и выиграл игру! ' + emoji_confetti + '\n Очки и рейтинг подсчитаны и обновлены! ' + emoji_sorriso
