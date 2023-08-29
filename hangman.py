import random

print("Capital Cities Hangman.")
print("By Anthony Nkyi.")
user_input = input("Type 'exit' to stop the program, or anything else to start. ")

while (user_input.lower()) != "exit":
  def get_guess():
    dashes = "-" * len(secret_word) #Word is hidden
    guesses_left = 12
    while guesses_left > -1 and not dashes == secret_word:
      print(dashes)
      print("You have "+ str(guesses_left)+ " guesses left.\n")
      guess = input("Guess: ")
      if len(guess) != 1:
        print ("Your guess must have  ONE letter.")
        guesses_left -= 1
      elif (guess.upper()) in secret_word:
        print ("Great guess, that letter's in the word.")
        dashes = update_dashes(secret_word, dashes, (guess.upper()))
      else:
        print ("That letter is not in the word.")
        guesses_left -= 1
      
    if guesses_left < 0:
      print ("You lose. The word was " + str(secret_word) + ".")
    else:
      print ("Congrats! You win. The word was " + str(secret_word))

  def update_dashes(secret, cur_dash, rec_guess):
    result = ""
    for i in range(len(secret)):
      if secret[i] == rec_guess:
        result = result + rec_guess
      else:
        result = result + cur_dash[i]
    return result
      
  words = ["LONDON", "PARIS", "WASHINGTON", "MADRID", "ROME", "LISBON", "ATHENS", "BERLIN", "ACCRA", "CAIRO", "BEIJING", "CANBERRA", "BUENOSAIRES", "OTTAWA", "KABUL", "ALGIERS", "BAKU"
           "MEXICO", "HAVANA", "VIENNA", "MONACO", "AMSTERDAM", "COPENHAGEN", "STOCKHOLM", "OSLO", "HELSINKI", "JOHANNESBURG", "DELHI", "PRAGUE", "MOSCOW", "ABUJA", "MARRAKECH", "TOKYO",
           "SINGAPORE", "DUBAI", "DOHA", "BRASILIA", "MONTEVIDEO", "ANTANANARIVO", "WELLINGTON", "CARDIFF", "EDINBURGH", "BELFAST", "DUBLIN", "BRUSSELS", "KIEV", "LUXEMBOURG",
           "BERN", "BUDAPEST", "BUCHAREST", "ANKARA", "HAVANA", "JERUSALEM"]

  secret_word = random.choice(words)
  get_guess()

  user_input = input("Please type exit to quit, or any other key to play again. ")

print("Thank you for playing Hangman.")
exit()
