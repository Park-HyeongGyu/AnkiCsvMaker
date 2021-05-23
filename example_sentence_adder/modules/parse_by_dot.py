class ParseByDot:
    def __init__(self, original_sentences_):
        if str(type(original_sentences_)) != "<class 'str'>":
            raise Exception("type of original_sentence must be string.")
        self.__original_sentence = original_sentences_
        self.__sentence_splited = list()

        self.__splitByDot()
        self.__removeSentenceNotIncludeEnglish()
        self.__removeSpaceAtFront()
        self.__appendDotIfNotExistedAtEnd()
    
    # private:
    def __splitByDot(self):
        copied_original = self.__original_sentence
        self.__sentence_splited = copied_original.split('.')
    
    def __removeSentenceNotIncludeEnglish(self):
        to_substitute = list()
        for content in self.__sentence_splited:
            if self.__isStringHasAlphabet(content):
                to_substitute.append(content)
        self.__sentence_splited = to_substitute
    
    def __isStringHasAlphabet(self, string):
        alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' ,'m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        false_counts = 0
        # full = 26 * 2
        for one_alphabet in alphabets:
            if string.find(one_alphabet) == -1:
                false_counts += 1
        if false_counts == 52:
            return False
        else:
            return True

    def __removeSpaceAtFront(self):
        to_substitute = list()
        for content in self.__sentence_splited:
            if content[0] == ' ':
                content = content[1:]
            to_substitute.append(content)

        self.__sentence_splited = to_substitute
    
    def __appendDotIfNotExistedAtEnd(self):
        to_substitute = list()
        for content in self.__sentence_splited:
            if content[-1] != '.':
                content = content + '.'
            to_substitute.append(content)
        self.__sentence_splited = to_substitute
        
    # public:
    def getSentenceSplitedAsList(self):
        return self.__sentence_splited

    def printOriginals(self):
        print(self.original_sentence)

def test():
    a = 'Occasionally individuals do not merely come out as well as clearly state what is troubling them and instead select more indirect means of expressing their annoyance. One companion might talk to the various other in a way that is condescending and also indicates underlying hostility. Numerous other times, partners may mope and even frown without genuinely dealing with an issue. Companions may likewise merely prevent discussing an issue by swiftly switching over topics when the subject turns up or by being incredibly vague. Such indirect ways of expressing temper are not useful since they don’t provide the individual that is the target of the behaviors, an idea of exactly how to react. They understand their companion is irritated, but the absence of directness leaves them without advice regarding what they can do to solve the issue.'
    parsor = ParseByDot(a)
    cont = parsor.getSentenceSplitedAsList()
    print(cont)

if __name__=="__main__":
    test()
