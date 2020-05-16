# Tournament Go Game Scraper

This script scrapes sgf files of [tournament Go games](https://online-go.com/tournaments), filtering for 9x9, 13x13, or 19x19 games (user input).

The overall process is:
1. Send requests to the API to gather tournament IDs
2. Using browser automation, go to each tournament page to scrape game IDs
3. Download sgf files by calling the API with the game IDs

Included is a simple script (chrome_ubuntu.sh) to setup Google Chrome and Chromedriver for browser automation on a Ubuntu server.
