# petulant-octo-dubstep
This program is to help parse 'Top PS3 Games' from http://www.metacritic.com/game/playstation-3 and provide that data back as API.

# How To Setup

## What to install
* python-virtualenv
`sudo aptitude install python-virtualenv -y`

## How to setup environment
```
mkdir ~/env/
cd ~/env/
virtualenv flask
source flask/bin/activate
flask/bin/pip install flask requests BeautifulSoup
wget https://raw.githubusercontent.com/bdflemin/petulant-octo-dubstep/master/app.py
chmod a+x ./app.py
./app.py
```

## What API requests can be made
1. GET /games

This will provide all the games gathered when looking for top ps3 games on metacritic
EXAMPLE - `curl -XGET http://localhost:5000/games`

2.GET /games/${GAME_TITLE}

This will grab game titel data only
EXAMPLE - `curl -XGET http://localhost:5000/games/The%20Last%20of%20Us:%20Left%20Behind`

All requests made will be in JSON format

## Screenshots
ALL GAMES
![](https://github.com/bdflemin/petulant-octo-dubstep/blob/master/images/all_games.png)

SINGLE GAME
![](https://github.com/bdflemin/petulant-octo-dubstep/blob/master/images/single_game.png)
