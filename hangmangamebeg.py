#hangman game project 3
import random
import hangman_stages


print("let's play hangman game!!")
print("The Word is from a list of Programming Languages")
print("you have to guess the word in 6 attempts")
lives=6
words = ["SachinTendulkar", "SunilGavaskar", "RahulDravid", "KapilDev",
         "AnilKumble", "VirenderSehwag", "SouravGanguly", "HarbhajanSingh",
         "ZaheerKhan", "YuvrajSingh", "ViratKohli", "MSDhoni", "VVSLaxman",
         "GautamGambhir", "AjinkyaRahane", "RavichandranAshwin", "JavagalSrinath",
         "IshantSharma", "ShikharDhawan", "BhuvneshwarKumar", "RohitSharma",
         "CheteshwarPujara", "HardikPandya", "RishabhPant", "MohammedShami",
         "KLRahul", "JaspritBumrah", "MayankAgarwal", "PrithviShaw",
         "HanumaVihari", "ShreyasIyer", "WriddhimanSaha", "ShubmanGill",
         "RahulDravid", "VirenderSehwag", "SouravGanguly", "HarbhajanSingh",
         "ZaheerKhan", "YuvrajSingh", "BishanSinghBedi", "SunilGavaskar",
         "KapilDev", "MohammedAzharuddin"]

word=random.choice(words)
word=word.lower()
word_list=list(word)
guess_list=[]
for i in range(len(word)):
    guess_list.append("_")
print(guess_list)
game_over=False
while not game_over:
    print()
    guess_letter=input("Guess a letter : ")
    print()
    guess_letter=guess_letter.lower()
    for position in range(len(word_list)):
        letter=word_list[position]
        if letter == guess_letter:
            guess_list[position]=guess_letter
    print(guess_list)
    print()
    if guess_letter not in word_list:
        lives-=1
        print("you have",lives,"lives left")
        if lives==0:
            game_over=True
            print("you lose!")
    if "_" not in guess_list:
        game_over=True
        print("you win!")
    print()
    print(hangman_stages.stages[lives])
    print()