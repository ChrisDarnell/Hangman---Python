import random
from hangman_words import word_list
from hangman_art import stages, logo

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(logo)

#Testing code
print(f'Since this is for demo, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}!")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
 
        if letter == guess:
            display[position] = letter

    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        print(f"{guess} is not in the word. Hang!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You hanged, man!")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win!")

    #Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])