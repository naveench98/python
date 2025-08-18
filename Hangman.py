import random
word_list=["peace","camel","tiger"]
word=(random.choice(word_list))
print(word)
placeholder=""

for blank in range(0,len(word)):
        placeholder+="_"
print(placeholder)       
Display=""

game_over=False

while not game_over:
    guess=input("guess a letter ")     
    for letter in word:
        if letter==guess:
            Display+=guess
        else:
         Display+="_"

    if "_"not in Display:
     game_over=True
    print(Display)       