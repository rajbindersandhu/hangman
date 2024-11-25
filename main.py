import random

word_list = ["teacher", "apple", "luxury", "alpha", "hello"]

def get_word():
    return random.choices(word_list)[0]

def get_index_visible(word: str):
    word_len = len(word)
    index_lst = []
    while True:
        current_index = random.randint(0, word_len-1)
        if(current_index not in index_lst):
            index_lst.append(current_index)
        if(len(index_lst) >= 2):
            break      
    return index_lst

def format_word(word: str, index_lst: list):
    formated_word = ""
    for index in range(len(word)):
        if index in index_lst:
            formated_word += word[index]
        else:
            formated_word += "_"
    return formated_word

def guess_char():
    user_input = input("Enter missing charcter: ")
    if(len(user_input) > 1):
        print("Enter only one character")
        user_input = guess_char()
    return user_input

def found_char(word_rmn:str, char:str, new_word:str):
    index_lst =[]
    
    for i in range(len(word_rmn)):
        if char == word_rmn[i]:
            index_lst.append(i)
            word_rmn = word_rmn[:i] + "_" +word_rmn[i+1:]
    for index in index_lst:
        new_word = new_word[:index] + char + new_word[index+1:]
    return word_rmn, new_word


def start_game(word, formatted_word):
    print("Guess the word: ")
    print(formatted_word)
    print("You have 3 lifes to guess the word")
    remaining_word = word
    
    life_count = 3
    while True:
        user_guess = guess_char()
        if user_guess in remaining_word:
            remaining_word, formatted_word = found_char(remaining_word, user_guess, formatted_word)
            if "_" not in formatted_word:
                print(formatted_word)
                print("Congrats!!!!!\nYou won")
                break
        else:
            print("\nWrong guess")
            if life_count>0:
                print(f"Loosing one life\n{life_count-1} life left")
                life_count -= 1
            else:
                print("No life left\nYou loose")
                break
        print("\n",formatted_word)
        
        

    
    

random_word = get_word()
index_lst = get_index_visible(random_word)
formatted_word = format_word(random_word, index_lst)
start_game(random_word, formatted_word)