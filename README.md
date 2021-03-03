# Tournament Go Game Scraper

This script scrapes sgf files of [tournament Go games](https://online-go.com/tournaments), filtering for 9x9, 13x13, or 19x19 games (user input).

The overall process is:
1. Send requests to the API to gather tournament IDs
2. Using browser automation, go to each tournament page to scrape game IDs
3. Download sgf files by calling the API with the game IDs

This can be used to gather raw data on a specified type of tournament game for machine learning projects, e.g. if you were interested in win rates of different opennings at various levels of play or if you wanted to try building up an AI to learn to play.

Notes
- Included is a simple script (chrome_ubuntu.sh) to setup Google Chrome and Chromedriver for browser automation on a Ubuntu server.
- poetry.lock and pyproject.toml are just setup files from [repl.it](https://repl.it/@AndrewLien/9x9GoGamesScrape), an online IDE that can link to Github.
