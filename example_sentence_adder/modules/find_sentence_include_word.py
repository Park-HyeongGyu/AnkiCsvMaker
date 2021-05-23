class FindSentenceIncludeWord:
    def __init__(self, sentences_list_):
        if str(type(sentences_list_)) != "<class 'list'>":
            raise Exception("type of sentences_list should be list.")
        self.SENTENCES_LIST = sentences_list_
        self.LEN_SENTENCES_LIST = len(self.SENTENCES_LIST)
    
    def find(self, word_to_find):
        to_return = list()
        index = 0
        lower_word_to_find = word_to_find.lower()
        while index < self.LEN_SENTENCES_LIST:
            sentence = self.SENTENCES_LIST[index]
            lower_sentence = sentence.lower()
            if lower_sentence.find(lower_word_to_find) != -1:
                to_return.append(sentence)
            index += 1
        return to_return

def test():
    pass

if __name__=="__main__":
    test()

