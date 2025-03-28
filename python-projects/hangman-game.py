#project - 8 :Hangman game in python

import random
words = ['enum' , 'python' , 'colab' , 'vscode' ,'game']

word= random.choice(words)
guessed_letters = []
attempts  = 6

print("Welcome to Hangman Game Project")
print("_" , len(word))

while attempts > 0: 
    guess = input("\n Guess the letters:").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Write one alphabat only!")
        continue
    
    if guess in guessed_letters:
        
        print("this letter is already guess choose another letter!")
        continue
    guessed_letters.append(guess)
    
    if guess in word:
        
        print("Correct Guess!")
    else:
        attempts -= 1
        print(f"Wrong {attempts} attempts")
        
    displayed_word = " ".join([letter if letter in guessed_letters else "_" for letter in word]) # type: ignore
    print(displayed_word)
    
    if "_" not in displayed_word:
        print(f"Congratulation! the correct :{word}")
        break
    else:
        print(f"Game  over! the correct word is {word}")
        
    