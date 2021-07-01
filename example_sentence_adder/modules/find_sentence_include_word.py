import nltk
from nltk.stem.wordnet import WordNetLemmatizer
#https://stackoverflow.com/questions/3753021/using-nltk-and-wordnet-how-do-i-convert-simple-tense-verb-into-its-present-pas

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

class FindSentenceIncludeWordNlp:
    def __init__(self, sentences_list):
        if str(type(sentences_list)) != "<class 'list'>":
            raise Exception("type of sentences_list should be list.")
        self.SENTENCE_DICT = dict() 
        for one_sentence in sentences_list:
            self.SENTENCE_DICT[self.__divideSentenceBasedOnPOS(one_sentence)] = one_sentence 
    
    def __divideSentenceBasedOnPOS(self, one_sentence): # POS - Parts of speech
        one_sentence = one_sentence.lower()
        pos_list = nltk.pos_tag(nltk.word_tokenize(one_sentence)) # https://medium.com/@gianpaul.r/tokenization-and-parts-of-speech-pos-tagging-in-pythons-nltk-library-2d30f70af13b
        sent_preprocessed = list()
        for one_word in pos_list:
            word = one_word[0]
            parts_of_speech = one_word[1] # parts_of_speech == 품사
            sent_preprocessed.append(word)
            if parts_of_speech == "NNS": # noun plural
                sent_preprocessed.append(self.__getSingularNoun(word))
            elif parts_of_speech == "JJR": #adjective comparative
                sent_preprocessed.append("-er")
            elif parts_of_speech == "JJS": # adjective, surperlative
                sent_preprocessed.append("-est")
            elif parts_of_speech == "POS": # possesive ending
                sent_preprocessed.append("one's")
            elif parts_of_speech == "PRP$": # jposessive pronoun
                sent_preprocessed.append("one's")
            elif parts_of_speech == "VBD": # verb, past tense
                sent_preprocessed.append(self.__getNon3rdPresentTense(word))
            elif parts_of_speech == "VBG": # gerund/present participle ex.taking
                sent_preprocessed.append(self.__getNon3rdPresentTense(word))
            elif parts_of_speech == "VBN": # past participle
                sent_preprocessed.append(self.__getNon3rdPresentTense(word))
            elif parts_of_speech == "VBP": # non 3rd person present
                sent_preprocessed.append(self.__getNon3rdPresentTense(word))
            elif parts_of_speech == "VBZ": # 3rd person present
                sent_preprocessed.append(self.__getNon3rdPresentTense(word))
        return tuple(sent_preprocessed)
    
    def __getSingularNoun(self, word):
        return WordNetLemmatizer().lemmatize(word)
    def __getNon3rdPresentTense(self, word):
        return WordNetLemmatizer().lemmatize(word, 'v')
    
    def find(self, word_to_find):
        keys_divided_sentences = list()
        divided_sentences = self.SENTENCE_DICT.keys()
        for one_divided_sentence in divided_sentences:
            if word_to_find in one_divided_sentence:
                keys_divided_sentences.append(one_divided_sentence)

        to_return = list()
        for one_divided_sentences_contains_word_to_find in keys_divided_sentences:
            to_return.append(self.SENTENCE_DICT[one_divided_sentences_contains_word_to_find])
        
        return to_return

def test():
    pass

if __name__=="__main__":
    test()

