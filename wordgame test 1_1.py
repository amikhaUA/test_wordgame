import random
from wordfreq import top_n_list

def ordgissningsspel():
    print("Choose language:")
    print("1.Svenska")
    print("2.English")
    print("3.Українська")

    choice = input("Your choice 1-3:")

    language = {
        "1": "sv",
        "2": "en",
        "3": "uk"
    }

    if choice not in language:
        print("Wrong choice!")
        return

    #get common words
    word_list = top_n_list(language[choice], 5000)

    # Keep words 7-12 letters only
    word_list = [
        word for word in word_list
        if word.isalpha() and 7 <= len(word) <= 12
    ]
    
    secret_word = random.choice(word_list)
    gissade_bokstäver = []
    försök_kvar = 8
    
    while försök_kvar > 0:
        show_word = [bokstav if bokstav in gissade_bokstäver else '_' for bokstav in secret_word]
        print("Word: ", ' '.join(show_word))
        print(f"Attempts left: {försök_kvar}")
        
        guess = input("Guess a letter: ").lower()
        try:
            if len(guess) != 1 or not guess.isalpha():
                raise ValueError("⚠️Wrong format!")
        except ValueError as e:
            print(e)
            continue
        
        if guess in gissade_bokstäver:
            print("⚠️You have already guess this letter.")
        elif guess in secret_word:
            gissade_bokstäver.append(guess)
        else:
            försök_kvar = försök_kvar - 1
            print("❌Wrong letter!")
        
        if all(bokstav in gissade_bokstäver for bokstav in secret_word):
            print(f"✅Congrats! You guess the word '{secret_word}'!")
            break
    else:
        print(f"❌You have no attempts left. Word was'{secret_word}'.")

ordgissningsspel()
