from flask import Flask, render_template, request
import random
from wumpus import HuntTheWumpus
wumpus_game = HuntTheWumpus()

app = Flask(__name__)

'''Constants used to refer to elements of words list'''
MISSPELLED = 1
CORRECT = 0

'''Accesses the words.txt file and enters the contents into the words list'''
with open("words.txt", "r", encoding="utf-8") as file:
    words = [line.split() for line in file if line.strip()]

'''Initialising lists'''
spelling_list = [0] * 10
misspelled_words = [0] * 10
correct_words = [0] * 10
results = [0] * 10
@app.route("/spelling_tester", methods=['POST', 'GET'])
def spelling_tester():

    '''Picks 10 random numbers that refers to words from words list and ensures no duplicates'''
    for word_num in range (10):
        num_used_already = True
        while num_used_already:
            num_used_already = False
            random_word_num = random.randint(0,len(words)-1)
            for search_num in reversed(range(word_num)):
                if random_word_num == spelling_list[search_num]:
                    num_used_already = True
        spelling_list[word_num] = random_word_num
    '''Splits the words list into 2 different lists with correct and incorrect spelling'''
    for word_num in range(10):
        misspelled_words[word_num] = words[spelling_list[word_num]][MISSPELLED]
        correct_words[word_num] = words[spelling_list[word_num]][CORRECT]

    '''Sends misspelled words to webpage to be displayed'''
    return render_template("spelling_tester.html" , misspelled_words = misspelled_words)

    '''Processes the users guesses'''
@app.route("/submit", methods = ["POST"])
def submit():
    score = 0
    guesses = request.form.getlist("guesses[]")
    for guess_pointer in range(10):
        if correct_words[guess_pointer] == guesses[guess_pointer]:
            score += 1
            results[guess_pointer] = "Correct!"
        else:
            results[guess_pointer] = "Incorrect!"

    '''Sends the results to results page'''
    return render_template(
        "results.html", 
        misspelled_words = misspelled_words ,
        guesses = guesses ,
        correct_words = correct_words ,
        results = results ,
        score = score
    )



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

