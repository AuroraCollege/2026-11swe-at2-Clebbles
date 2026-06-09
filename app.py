from flask import Flask, render_template, request
from wumpus import HuntTheWumpus
wumpus_game = HuntTheWumpus()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wumpus', methods=['POST', 'GET'])
def wumpus():
    if request.method == 'POST':
        message = wumpus_game.play(request.form)
    else:
        message = wumpus_game.new_game()
    return render_template('wumpus.html', message=message, game=wumpus_game)

@app.route('/spelling_tester', methods=['POST', 'GET'])
def spelling_tester():
    if request.method == 'POST':
        message = spelling_tester.play(request.form)
    else:
        message = spelling_tester.new_game()
    return render_template('spelling_tester.html', message=message, game=spelling_tester)

if __name__ == "__main__":
    app.run()