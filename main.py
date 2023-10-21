import string
from googletrans import Translator



class Translator_dist:
    def __init__(self, word = "яблоко"):
        self.word = word
        # Экземпляр класса
        self.translator = Translator()

    def translate_text(self):
        if self.word[0].upper() in string.ascii_uppercase:
            translate_word = self.translator.translate(self.word, dest='en').text
            return translate_word

        if self.word[0].upper() not in string.ascii_uppercase:
            translate_word = self.translator.translate(self.word, dest='ru').text
            return translate_word


trans = Translator_dist('programm')
print(trans.translate_text())