import random

def new_game(self):
    self.player = Player()
    self.wumpus = Wumpus(random.choice(list(self.rooms.keys())))
    
    self.game_on = True
    return "Correct the 10 misspelled words"



with open("words.txt", "r", encoding="utf-8") as file:
    words = [line.split() for line in file if line.strip()]


spelling_list = [0] * 10

for word_num in range (10):
    num_used_already = True
    while num_used_already:
        num_used_already = False
        random_word_num = random.randint(0,len(words)-1)
        for search_num in reversed(range(word_num)):
            if random_word_num == spelling_list[search_num]:
                num_used_already = True
    spelling_list[word_num] = random_word_num