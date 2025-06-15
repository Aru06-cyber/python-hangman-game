import init_db as fc


def bst_sc(id, sc):
    ins = "INSERT INTO p_scores VALUES (%s, %s)"
    fc.mycur.execute(ins, (id, sc))
    fc.mydb.commit()

    fc.mycur.execute("SELECT MAX(score) FROM p_scores WHERE p_id = %s", (id,))
    result = fc.mycur.fetchone()
    if result and result[0]:
        print("Best score:", result[0])
    else:
        print("No best scores yet :(")


def st(score, user_id):
    import random
    score = 0
    play = 0

    hangman1 = [
        """
             |

             |

             |

             |

             |

               """,
        """
            _
           | |
           O 
             |

             |""",
        """
            _  
           | |
           O 
          /| | 

             |""",
        """
            _  
           | |
           O |
          /|\|""",
        """
            _  
           | |
           O |
          /|\|
           | |
          /  |""",
        """
            _  
           | |
           O |
          /|\|
           | |
          / \|"""
    ]

    animals = [
        'rabbit', 'duckling', 'giraffe', 'dolphin', 'rooster', 'horse', 'zebra', 'llamas',
        'ostrich', 'camel', 'racoon', 'deer', 'turkey', 'dove', 'sheep', 'gorilla', 'geese',
        'oxen', 'reindeer', 'cat', 'dog', 'penguin', 'pigeon', 'rat', 'panda', 'tiger', 'lion',
        'elephant', 'ant', 'antelope', 'crocodile', 'monkey', 'bear', 'hare', 'bat', 'seahorse',
        'fish', 'prawn', 'catfish', 'bufallo', 'porcupine', 'shark', 'whale', 'unicorn', 'tortoise',
        'turtle', 'peacock', 'butterfly', 'fly', 'parrot', 'bee', 'cow', 'chameleon', 'dianosaur',
        'eagle', 'eel', 'hen', 'flemmingo', 'goat', 'hamster', 'hedgehog', 'kwala', 'kangaroo',
        'earthworm', 'jaguar', 'jackal'
    ]

    word = random.choice(animals).lower()
    guessed_correctly = []
    guessed_incorrectly = []
    tries = 6
    hangman_count = -1

    while tries > 0:
        output = ''
        for letter in word:
            output += letter if letter in guessed_correctly else "_ "
        if output.replace(" ", "") == word:
            break

        print("Guess the word: ", output)
        print(tries, "Chances left")
        guess = input().lower()

        if guess in guessed_correctly or guess in guessed_incorrectly:
            print("Already guessed", guess)
        elif len(guess) != 1:
            new_correct = []
            wrong_guess = False

            for char in guess:
                if char in word:
                    if char not in guessed_correctly:
                        guessed_correctly.append(char)
                        new_correct.append(char)
                else:
                    wrong_guess = True
                    if char not in guessed_incorrectly:
                        guessed_incorrectly.append(char)
                    score -= 1
                    tries -= 1
                    hangman_count += 1
                    if hangman_count < len(hangman1):
                        print(hangman1[hangman_count])
                    print("-1 score:", score)

            # Now decide how much to add
            if new_correct:
                if wrong_guess:
                    score += 3 * len(new_correct)
                    print(f"+{3 * len(new_correct)} (partial guess bonus) score:", score)
                else:
                    score += 5 * len(new_correct)
                    print(f"+{5 * len(new_correct)} score:", score)
            else:
                print("+0 score:", score)

        else:
            if guess in word:
                print("Awesome Job! You guessed a correct letter!")
                guessed_correctly.append(guess)
                score += 5
                print("+5 score:", score)
            else:
                guessed_incorrectly.append(guess)
                hangman_count += 1
                print("Oops! Incorrect letter")
                if hangman_count < len(hangman1):
                    print(hangman1[hangman_count])
                score -= 1
                print("-1 score:", score)
                tries -= 1

    if tries > 0:
        print(word)
        print("You guessed the word.")
        print("YOU WON!!!")
        print("Your Score:", score)
    else:
        print("_GAME OVER_")
        print("You lost!")
        print("The word was", word)
        print("Your Score:", score)

    bst_sc(user_id, score)
