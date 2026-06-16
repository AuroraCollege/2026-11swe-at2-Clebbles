from flask import Flask, render_template, request
import random
from spelling import Spelling
s = Spelling()

from wumpus import HuntTheWumpus
wumpus_game = HuntTheWumpus()

app = Flask(__name__)


@app.route("/submit", methods = ["POST"])
def submit():
    score = 0
    guesses = request.form.getlist("guesses[]")
    for guess_pointer in range(10):
        if s.correct_words[guess_pointer] == guesses[guess_pointer]:
            score += 1
            s.results[guess_pointer] = "Correct!"
        else:
            s.results[guess_pointer] = "Incorrect!"

    '''Sends the results to results page'''
    return render_template(
        "results.html", 
        misspelled_words = s.misspelled_words ,
        guesses = guesses ,
        correct_words = s.correct_words ,
        results = s.results ,
        score = score
    )

@app.route("/spelling_tester", methods=['POST', 'GET'])
def spelling_tester():

    '''Picks 10 random numbers that refers to words from words list and ensures no duplicates'''
    for word_num in range (10):
        num_used_already = True
        while num_used_already:
            num_used_already = False
            random_word_num = random.randint(0,len(s.words)-1)
            for search_num in reversed(range(word_num)):
                if random_word_num == s.spelling_list[search_num]:
                    num_used_already = True
        s.spelling_list[word_num] = random_word_num
    '''Splits the words list into 2 different lists with correct and incorrect spelling'''
    for word_num in range(10):
        s.misspelled_words[word_num] = s.words[s.spelling_list[word_num]][s.MISSPELLED]
        s.correct_words[word_num] = s.words[s.spelling_list[word_num]][s.CORRECT]

    '''Sends misspelled words to webpage to be displayed'''
    return render_template("spelling_tester.html" , misspelled_words = s.misspelled_words)

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


if __name__ == "__main__":
    app.run()

