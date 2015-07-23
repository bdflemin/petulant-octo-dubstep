#!flask/bin/python
import requests
from BeautifulSoup import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)

def ps3_games():
	data = []
	headers = {'User-Agent':'Mozilla'}
	source = requests.get('http://www.metacritic.com/game/playstation-3', headers=headers)
	metacritic = BeautifulSoup(source.text)
	games = metacritic.findAll('ol', attrs={'class':'list_products list_product_summaries'})[0]
	for i in games.findAll('div', attrs={'class':'wrap product_wrap'}):
		score = str(i.find('span', {'class':'metascore_w medium game positive'}).text)
		title = str(i.find('a').text)
		data.append({'title': title, 'score': score})
	return data

@app.route('/games', methods=['GET'])
def get_games():
	games = ps3_games()
	return jsonify({'games': games})

@app.route('/games/<string:game>', methods=['GET'])
def get_game(game):
	game = game.replace('%20',' ')
	data = ps3_games()
	for d in data:
		if game == d['title']:
			return jsonify({'game': d})

if __name__ == '__main__':
    app.run(debug=True)