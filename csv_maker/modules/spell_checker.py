from spellchecker import SpellChecker

class misspelled_word:
    def __init__(self):
        self.misspelled = ""
        self.correction = ""
        self.candidates = ()
    def setMisspelled(self, word_misspelled):
        self.misspelled = word_misspelled
    def setCorrection(self, word_corrected):
        self.correction = word_corrected
    def setCandidates(self, candidates_set):
        self.candidates = tuple(candidates_set)

def check_spell(word_list):
    if str(type(word_list)) != "<class 'list'>":
        raise Exception('type of word_list in class SpellChecker should be list.')
    checker = SpellChecker()
    checker.word_frequency.load_words(['-er', '-es']) 
    checker.word_frequency.load_words(['...', '~'])

    misspelled = checker.unknown(word_list)

    misspelled_words = []
    index = 0
    for one_word in misspelled:
        correction = checker.correction(one_word)
        candidates = checker.candidates(one_word)

        misspelled_words.append(misspelled_word())
        misspelled_words[index].setMisspelled(one_word)
        misspelled_words[index].setCorrection(correction)
        misspelled_words[index].setCandidates(candidates)
        index += 1
    return tuple(misspelled_words)

def tes():
    a = SpellChecker()

if __name__ == '__main__':
    tes()

