class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        new_words = [word for word in words if len(word) == len(self.word)]
        result = []
        for word in new_words:
            word_letters = [letter for letter in word]
            self_letters = [letter for letter in self.word]
            if sorted(word_letters) == sorted(self_letters):
                result.append(word)
        return result