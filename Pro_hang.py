import random
word_list=["peace","camel","tiger"]
word=(random.choice(word_list))
print(word)

# your code above
placeholder = ""
for blank in range(0, len(word)):
    placeholder += "_"
print(placeholder)
Display = placeholder   # Set Display to initial placeholder

game_over = False

print(Display)          # Show the blanks at start

while not game_over:
    guess = input("guess a letter ")
    new_display = ""
    correct_letter=""
    for letter in word:
        if letter == guess:
            new_display += guess
            correct_letter.append(guess)
        elif letter in correct_letter:
            new_display+=letter
        else:
            new_display += "_"
    Display = new_display
    print(Display)
    if "_" not in Display:
        game_over = True
