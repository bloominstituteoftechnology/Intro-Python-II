secret_word = "Apu"
guess = ""
guess_count = 0
guess_limit = 3
out_of_luck = False

while guess != secret_word and not(out_of_luck):
    if guess_count < guess_limit:
        guess = input('Enter Guess: ')
        guess_count += 1
    else:
        out_of_luck = True

if out_of_luck:
    print('Uh-oh!!! You Lose')
else:
    print("You Win")
