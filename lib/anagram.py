class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        # get rid of words that are not the same length as self.word
        new_words = [word for word in words if len(word) == len(self.word)]
        # create empty array to return result of matching words
        result = []
        # for loop to test each word individually
        for word in new_words:
            # create array of letters in word we are comparing
            word_letters = [letter for letter in word]
            # create array of letters of self.word
            self_letters = [letter for letter in self.word]
            # sort arrays and compare if they are the same
            if sorted(word_letters) == sorted(self_letters):
                # add orginial word to result array if it passes
                result.append(word)
        #return result with matches or empty if nothing passes 
        return result