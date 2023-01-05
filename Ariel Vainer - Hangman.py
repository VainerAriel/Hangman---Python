import pygame

pygame.init()

from Game import *

game = Game()


def draw_on_screen():
    # draw the background
    image(hangman[7 - game.life_count], 0, 0)

    # draw the ending screen
    if game.life_count <= 0 or game.winner:
        if game.life_count <= 0:
            screen.blit(game.text, game.text_rect)
        else:
            image(win, 0, 0)
            image(fix, 364, 717)

        # check for both buttons
        if button(141, 717, 201, 86, 1):
            image(hangman[8], 141, 717)
        if button(364, 717, 201, 86, 1):
            image(hangman[9], 364, 717)

    # draw all the letters
    for i in range(5):
        for j in range(6):
            if i * 6 + j < 26:
                image(game.b[i * 6 + j], 1295 - 3 * 110 + j * 110, 450 + i * 110)

    # draw the word
    for i in range(len(game.random_word)):
        if game.letters_ascii[i] >= 0:
            image(w[game.letters_ascii[i]], 1295 - 70 * len(game.random_word) / 2 + i * 70, 250)
        else:
            image(blank, 1295 - 70 * len(game.random_word) / 2 + i * 70, 250)

    pygame.display.flip()


# main game
def check(a, life):
    keep_life = False
    check_for_letter = str(chr(a))
    new_life_num = life

    # check if letter was already used
    for i in range(len(game.used_letters)):
        if check_for_letter == game.used_letters[i]:
            return new_life_num

    # check for each letter in the word, if the letter pressed is the right one
    for i in range(len(game.random_word)):
        character_in_random_word = game.random_word[i]
        character_in_word = game.word[i]
        if character_in_random_word == check_for_letter:
            keep_life = True
            game.b[ord(check_for_letter) - 97] = g[ord(check_for_letter) - 97]
            if character_in_random_word != character_in_word:
                game.word[i] = character_in_random_word
        else:
            if game.b[ord(check_for_letter) - 97] != g[ord(check_for_letter) - 97]:
                game.b[ord(check_for_letter) - 97] = r[ord(check_for_letter) - 97]

    # wrong letter
    if not keep_life:
        new_life_num -= 1

    # right letter
    for i in range(len(game.letters)):
        if check_for_letter == game.letters[i]:
            game.letters.remove(check_for_letter)
            game.used_letters.append(check_for_letter)
            break

    return new_life_num


running = True
while running:
    for event in pygame.event.get():
        pressed_keys = pygame.key.get_pressed()
        pressed_buttons = pygame.mouse.get_pressed()

        if event.type == pygame.QUIT or pressed_keys[pygame.K_ESCAPE]:
            running = False

        if event.type == pygame.KEYDOWN:
            if 96 < event.key < 123 or 64 < event.key < 91:
                # main game with keyboard
                if game.life_count > 0 and not game.winner:
                    letter = pygame.key.name(event.key).lower()
                    game.life_count = check(ord(letter), game.life_count)

    # main game with mouse
    if game.life_count > 0 and not game.winner:
        for i in range(5):
            for j in range(6):
                if button(1295 - 3 * 110 + j * 110, 450 + i * 110, 100, 100, 0):
                    game.life_count = check(97 + i * 6 + j, game.life_count)
        for i in range(len(game.random_word)):
            game.letters_ascii[i] = int((ord(game.word[i]) - 97))

        # check for winning
        if "_" not in "".join(game.word):
            game.winner = True
    else:
        # if losing, check for button press and exit or restart
        if button(141, 717, 201, 86, 0):
            running = False
        if button(364, 717, 201, 86, 0):
            game = Game()
            game.used_letters = []

    draw_on_screen()

    clock.tick(FPS)
