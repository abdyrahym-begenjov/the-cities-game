# the-cities-game
# The Cities Game (Игра в города) 🏙️
## English 
The Cities Game is an interactive, fully featured terminal-based word puzzle game built in Python. Inspired by the traditional geography game, it challenges players to take turns naming cities where each subsequent entry must begin with the last letter of the previously named city.
With full bilingual localization supporting both English and Russian, automated city database filtering, active score tracking, and immersive multiplayer mechanics, this game brings a classic pastime directly to your command line.
### 🎮 Core Game Mechanics
#### Letter Trimming Rule
If a chosen city name ends with a non-vocalic modifier or specific letters such as 'ъ', 'ы', or 'ь', the game automatically drops that last letter and utilizes the preceding character as the target letter for the next turn.
#### Absolute Uniqueness
Every city name can only be used once per match. The game automatically keeps a live ledger of all entered cities to prevent duplicate responses.
#### Automatic Case Correction
Players can type freely in lowercase or mixed case. The game automatically strips trailing spaces and converts words to Title Case to cross-verify submissions seamlessly against the database.
### 🕹️ Game Modes
#### Infinity Mode (Single Player)
Test your personal geographical stamina in an ultimate challenge against the database.
 * The game pulls a random starting city from your global list to kickoff.
 * You begin with 3 Hearts.
 * Providing an invalid city, a city starting with the incorrect letter, or a repeating city deducts 1 Heart.
 * Submitting an empty field displays a friendly reminder without docking your score or lives.
 * The game concludes when your health drops to 0, or if you manage to exhaust the entire database to be crowned an Absolute Champion.
 * Performance star tiers are awarded based on how many correct cities you can recall in a single run.
#### Party Mode (2 - 4 Players Multiplayer)
Compete locally with your friends in a tactical, turn-based showdown.
 * Turn order is determined dynamically at the start by rolling a virtual six-sided die for each participant.
 * Match difficulty lengths dictate the target points required to win: Easy requires 10 points, Normal requires 20 points, and Hard requires 30 points.
 * Each player manages their own pool of 3 Hearts. Failing to answer correctly or pass validation docks a heart. Losing all hearts instantly eliminates a player from the loop.
 * To maintain competitive stakes, the player who is eliminated first (taking the absolute last place) walks away with 0 points for that match.
### ⚡ Special Abilities (Party Mode)
Every participant enters Party Mode armed with three powerful, single-use utility triggers. Instead of submitting a city name on their turn, a player can type the capability name in English or Russian to shift the tide of battle:
 * Blaster: Targets and immediately subtracts 1 Heart from any chosen active opponent. Self-targeting or attacking previously eliminated players is prohibited.
 * Game Pass: Safely skips the current player's turn altogether without penalty or health deductions.
 * Replacement: Discards the current active city and swaps it with a brand new, randomly chosen city from the database that retains the exact same required starting letter.
#### The Perfect Victory Bonus
Players are heavily incentivized to rely purely on their memories. If a player manages to win a Party Mode match with all three of their abilities fully intact and unused, their final score for that entire match is doubled.
### 📊 Global Progression & Settings
#### Persistent Leaderboards
All points earned from both Infinity Mode survivals and competitive Party Mode matches are compiled and aggregated globally into a local highscore database. Players can visit the Highscores tab from the main menu at any time to review historical performance and see who holds the top spots.
#### Localization & Customization
Through the configuration menu, users can dynamically shift between English or Russian interfaces at will. Changing the language dynamically updates the target city database (cities.json or goroda.json), ensuring an authentic vocabulary challenge tailored specifically to the chosen language.
## Русский
Игра в Города — это интерактивная текстовая головоломка для терминала, разработанная на языке Python. Вдохновленная классической настольной игрой, она предлагает игрокам по очереди называть города, где каждая последующая запись должна начинаться на последнюю букву предыдущего города.
Благодаря полной двуязычной локализации (русский и английский языки), автоматической фильтрации базы данных, отслеживанию рекордов и захватывающим мультиплеерным механикам, эта игра переносит любимое развлечение прямо в вашу командную строку.
### 🎮 Основные механики игры
#### Правило обрезки букв
Если выбранное название города заканчивается на непроизносимые знаки или специфические буквы, такие как 'ъ', 'ы' или 'ь', игра автоматически отбрасывает эту букву и использует предыдущий символ в качестве целевой буквы для следующего хода.
#### Абсолютная уникальность
Каждое название города может быть использовано только один раз за матч. Игра автоматически ведет живую историю всех введенных городов, чтобы предотвратить повторные ответы.
#### Автоматическое исправление регистра
Игроки могут вводить текст в любом регистре. Игра самостоятельно удаляет лишние пробелы в начале и конце строки, а также преобразует слова так, чтобы они начинались с заглавной буквы, для беспрепятственной проверки по базе данных.
### 🕹️ Режимы игры
#### Режим «Бесконечность» (Одиночная игра)
Проверьте свою личную географическую выносливость в ультимативном противостоянии с базой данных.
 * Для старта игра выбирает случайный город из глобального списка.
 * Вы начинаете матч с 3 Сердцами.
 * Ввод неверного города, города с неподходящей буквы или уже использованного названия отнимает 1 Сердце.
 * Отправка пустого поля ввода вызовет лишь предупреждение, не уменьшая ваши очки или жизни.
 * Игра завершается, когда счетчик ваших сердец падает до 0, либо когда вы полностью исчерпаете всю базу данных и получите титул Абсолютного Чемпиона.
 * По результатам игры вам присваивается определенное количество звезд в зависимости от того, сколько городов вы смогли вспомнить за один раунд.
#### Режим «Вечеринка» (Мультиплеер от 2 до 4 игроков)
Соревнуйтесь локально со своими друзьями в тактическом пошаговом противостоянии.
 * Очередность ходов определяется динамически в самом начале путем броска виртуального шестигранного кубика для каждого участника.
 * Выбранная сложность матча задает количество очков, необходимое для победы: «Лёгкий» требует 10 очков, «Нормальный» — 20 очков, а «Сложный» — 30 очков.
 * Каждый игрок управляет собственным пулом из 3 Сердец. Ошибка при вводе или провал валидации отнимает сердце. Потеря всех сердец приводит к мгновенному выбыванию игрока из общего круга.
 * Чтобы сохранить дух соперничества и высокие ставки, игрок, который выбывает самым первым (занимает последнее место), завершает матч с 0 баллов на счету.
### ⚡ Специальные способности (Режим «Вечеринка»)
Каждый участник входит в режим «Вечеринка», имея на вооружении три мощные одноразовые способности. Вместо ввода названия города в свой ход игрок может напечатать имя способности на русском или английском языке, чтобы переломить ход битвы:
 * Бластер: Выбирает целью и мгновенно отнимает 1 Сердце у любого активного оппонента. Стрелять в себя или атаковать уже выбывших игроков запрещено.
 * Пропуск: Позволяет безопасно пропустить текущий ход без каких-либо штрафов или потери здоровья.
 * Замена: Сбрасывает текущий активный город и заменяет его на совершенно новый, случайно выбранный из базы данных город, который сохраняет точно такую же требуемую начальную букву.
#### Бонус идеальной победы
Игра активно мотивирует полагаться исключительно на свою память. Если игроку удается победить в режиме «Вечеринка», не использовав ни одной из трех своих способностей (Бластер, Пропуск и Замена остались нетронутыми), его финальные очки за весь этот матч удваиваются.
### 📊 Глобальный прогресс и настройки
#### Постоянная таблица лидеров
Все очки, заработанные как в выживании режима «Бесконечность», так и в соревновательных матчах режима «Вечеринка», суммируются и сохраняются в глобальной локальной базе данных рекордов. Игроки могут в любой момент перейти на вкладку «Рекорды» из главного меню, чтобы изучить историю результатов и узнать, кто занимает верхние строчки.
#### Локализация и кастомизация
Через меню настроек пользователи могут в любой момент переключить интерфейс между русским и английским языками. Смена языка динамически обновляет целевую базу данных городов (cities.json или goroda.json), гарантируя аутентичную языковую проверку, адаптированную под выбранный регион.
