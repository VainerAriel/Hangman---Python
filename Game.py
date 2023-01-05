from settings import *


class Game:
    def __init__(self):
        # choosing a random word
        self.random_word = lines[random.randint(0, len(lines))]

        self.word = []
        for letter in range(len(self.random_word)):
            self.word.append("_")

        self.used_letters = []
        self.letters_ascii = []

        self.used_letters.clear()
        self.letters_ascii.clear()

        for i in range(len(self.random_word)):
            self.letters_ascii.append(ord(self.word[i]) - 97)

        # setting the letters and the font
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u', 'v', 'w', 'x', 'y', 'z']

        # seven lives
        self.life_count = 7

        # win
        self.winner = False

        # text settings
        self.text = font.render(self.random_word, True, BLACK)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (670 // 2 + 15, 580)

        # letter pieces
        self.b = [pygame.image.load("images\\black\\b (" + str(i + 1) + ").png") for i in range(26)]
