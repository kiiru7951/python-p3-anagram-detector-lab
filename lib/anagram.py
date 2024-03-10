class Anagram:
    def __init__(self, word=""):
        self.word = word
        self.word_let = []
        self.check_word()
        
    def match(self, word_list):
        word_match = []
        for word in word_list:
            listword_let = [letter for letter in word]
            if sorted(self.word_let) == sorted(listword_let):
                word_match.append(word)
        return word_match
    
    def check_word(self):
        self.word_let = [letter for letter in self.word]