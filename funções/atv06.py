import random

def choose_word():
    words = ["womakerscode", "python", "programação", "software", "codigo"]
    return random.choice(words)

def verify_word(word, word_to_choose, reveal_char):
    found = False
    for i, char in enumerate(word_to_choose):
        if char == word:
            reveal_char[i] = word
            found = True
        return found
            

def secret_word(word_to_choose, reveal_char):
    for char in reveal_char:
        print(char, end=' ')
    print()
    


def play_game():
    word_to_choose = choose_word()
    reveal_char = ["-"] * len(word_to_choose)
    max_attempt = 6
    attempt_done = 0

    while '-' in reveal_char and attempt_done < max_attempt:
        secret_word(word_to_choose, reveal_char)
        word = input("Digite uma letra: ").lower()
        if not word.isalpha() or len(word) != 1:
            print("Por favor, digite uma única letra válida.")
            continue

        if word in reveal_char:
            print("Você já tentou esta letra. Tente outra.")
            continue

        if verify_word(word, word_to_choose, reveal_char):
            print("Letra correta!")
        else:
            print("Letra incorreta.")
        attempt_done += 1

    if '-' not in reveal_char:
        print("Parabéns! Você advinhou a palavra.")
    else:
        print(f'Você atingiu o número de tentativas. A palavra era: {word_to_choose}')

play_game()