# the-cities-game
# The Cities Game (Игра в города) 🏙️
## English
Welcome to the exciting text-based game "Cities," written in Python! This classic intellectual game is adapted for modern consoles, with multilingual support, a save system, and leaderboards. Test your knowledge, compete with friends, and beat your own high scores!
### 🌟 Key Game Features
* **Bilingual Interface:** Full support for Russian and English. The game automatically adapts the rules, city database, and interface to the selected localization.
* **Smart Rules Checking:** The game strictly enforces the rules of classic "Cities." It takes into account the peculiarities of the Russian language (for example, if a city ends in a soft or hard sign, or the letter "Ы," the game will automatically suggest a city starting with the second-to-last letter).
* **Lives and Scoring System:** You have 3 lives. Each mistake or repeated city takes away one life. Score points for each correct answer to increase your rank.
 * **Mastery Levels:** After completing a game, an algorithm evaluates your performance and assigns a title—from "Loser" to "Absolute Champion"—with a unique star system.
* **Local Data Saving:** Your name, selected language, and accumulated progress are automatically saved in JSON files, so you don't have to reconfigure the game each time you launch.
* **Global Highscore:** A built-in leaderboard sorts players by score. Compete with family or colleagues on the same device!
* **Flexible Settings:** You can always access the settings menu directly from the game to change your username or switch the interface language.
* **Cross-platform Screen Clearing:** The game menu always looks tidy thanks to smart console clearing, which adapts to both Windows and Unix systems (Linux/macOS).  ### 📜 Game Rules
The basic rules are incredibly simple, but require good memory and concentration:
1. The game randomly selects the first city from an extensive database.
2. You must enter a city name that begins with the same letter as the previous city's ending.
3. City names cannot be repeated during a single game session.
4. If you make a mistake, enter an empty string, or repeat a city you've already used, you lose one life (there are 3 in total).
5. The game continues until you run out of lives.
### 🛠️ System Requirements and Dependencies
For the game to run correctly, your computer must have Python version 3.10 or higher installed (as the code uses modern match/case pattern matching constructs).
 The following project files are also required for a full run:
* Game session and settings database files (base.json, data.json)
* City lists for different localizations (goroda.json, cities.json)
* Text files with detailed rules (ru_rules.txt, en_rules.txt)
* Internal modules for working with data and translation (propython, translator)
### 👨‍💻 About the Author
* **Creator:** Abdyrahym Begenjov
* **GitHub:** abdyrahym-begenjov
If you like the project, don't forget to give this repository a **Star ⭐**! Enjoy the game!
## Русский
Добро пожаловать в увлекательную текстовую игру «Города», реализованную на языке Python! Это классическое интеллектуальное развлечение, адаптированное под современные консоли, с поддержкой нескольких языков, системой сохранений и таблицей лидеров. Испытайте свою эрудицию, соревнуйтесь с друзьями и побеждайте собственные рекорды!
### 🌟 Ключевые особенности игры
 * **Двуязычный интерфейс:** Полная поддержка русского и английского языков. Игра автоматически адаптирует правила, базу городов и интерфейс под выбранную локализацию.
 * **Умная проверка правил:** Игра строго следит за соблюдением правил классических «Городов». Она учитывает особенности русского языка (например, если город заканчивается на мягкий или твердый знак, или букву «Ы», игра автоматически предложит назвать город на предпоследнюю букву).
 * **Система жизней и подсчет очков:** У вас есть 3 жизни. Каждая ошибка или повтор города отнимает одну жизнь. Набирайте очки за каждый правильный ответ, чтобы повысить свой ранг.
 * **Уровни мастерства:** По окончании игры алгоритм оценивает ваши результаты и присваивает звание — от «Неудачника» до «Абсолютного Чемпиона» с уникальной звездной системой.
 * **Локальное сохранение данных:** Ваше имя, выбранный язык и накопленный прогресс автоматически сохраняются в файлы формата JSON, так что вам не придется настраивать игру заново при каждом запуске.
 * **Глобальная таблица рекордов:** Встроенный лидерборд сортирует игроков по количеству набранных очков. Соревнуйтесь с семьей или коллегами на одном устройстве!
 * **Гибкие настройки:** Вы всегда можете зайти в меню настроек прямо из игры, чтобы сменить имя пользователя или переключить язык интерфейса.
 * **Кроссплатформенная очистка экрана:** Меню игры всегда выглядит аккуратно благодаря умной очистке консоли, которая подстраивается как под Windows, так и под Unix-системы (Linux/macOS).
### 📜 Правила игры
Основные правила невероятно просты, но требуют хорошей памяти и концентрации:
 1. Игра случайным образом выбирает первый город из обширной базы данных.
 2. Вам необходимо ввести название города, которое начинается на ту букву, на которую закончился предыдущий город.
 3. Названия городов не должны повторяться в течение одной игровой сессии.
 4. Если вы ошибаетесь, вводите пустую строку или повторяете уже использованный город, вы теряете одну жизнь (всего их 3).
 5. Игра продолжается до тех пор, пока у вас не закончатся жизни.
### 🛠️ Системные требования и зависимости
Для корректной работы игры на вашем компьютере должен быть установлен Python версии 3.10 или выше (так как в коде используются современные конструкции сопоставления шаблонов match/case).
Также для полноценного запуска требуются следующие сопутствующие файлы проекта:
 * Файлы баз данных игровых сессий и настроек (base.json, data.json)
 * Списки городов для разных локализаций (goroda.json, cities.json)
 * Текстовые файлы с подробными правилами (ru_rules.txt, en_rules.txt)
 * Внутренние модули для работы с данными и переводом (propython, translator)
### 👨‍💻 Об авторе
 * **Создатель:** Абдырахим Бегенджов
 * **GitHub:** abdyrahym-begenjov
Если вам понравился проект, не забудьте поставить **Star ⭐** этому репозиторию! Приятной игры!

