import random

word_list = [
    "inception", "avatar", "titanic", "jumanji", "gladiator", "batman", "superman",
    "frozen", "up", "coco", "dangal", "raazi", "rocky", "joker", "shazam", "interstellar",
    "gravity", "tenet", "lucy", "fury", "moana", "encanto", "zootopia", "cars", "ratatouille",
    "thor", "avengers", "panther", "frozen", "aladdin", "elemental", "barbie", "oppenheimer",
    "hera", "rrr", "pathaan", "baahubali", "drishyam", "chakde", "sanju", "dhoom", "ghajini"
]

hangman_stages = [
    """
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      / \\
    |
    |___
    """,
    """
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      / 
    |
    |___
    """,
    """
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      
    |
    |___
    """,
    """
     _______
    |/      |
    |      (_)
    |      \\|
    |       |
    |      
    |
    |___
    """,
    """
     _______
    |/      |
    |      (_)
    |       |
    |       |
    |      
    |
    |___
    """,
    """
     _______
    |/      |
    |      (_)
    |      
    |       
    |      
    |
    |___
    """,
    """
     _______
    |/      |
    |      
    |      
    |       
    |      
    |
    |___
    """
]

chosen_word = random.choice(word_list)
lives = 6

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_ "
print("Word to guess:", placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"*****************************{lives}/6 LIVES LEFT*****************************")
    guess = input("What letter do you guess?: ").lower()

    if guess in correct_letters:
        print("You've already guessed this letter...")
        continue  

    correct_letters.append(guess)

    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter + " "
        else:
            display += "_ "

    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("*****************************YOU LOSE*****************************")
            print(f"The correct word was: {chosen_word}")

    if "_ " not in display:
        game_over = True
        print("*****************************YOU WIN*****************************")

    print(hangman_stages[lives])
