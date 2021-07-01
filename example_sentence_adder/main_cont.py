from modules.preprocess_example_sentences import PreprocessExampleSentences
from modules.check_overlap_with_original import CheckOverlapWithOriginal
from modules.find_sentence_include_word import FindSentenceIncludeWordNlp
from modules.handle_csv import HandleCsv
from modules.parse_by_dot import ParseByDot

def description():
    print("this is program is prototype and is for temporary use.")
    print("made by Park Hyeong-gyu in 2021-0523.")
    print("\nWARNING")
    print("If you are going to use this program again, you should read code carefully.")
    print("Because I didn't complete making it.")
    print("\n")

def main():
    description()

    print("input name of file that is consisted with new words.")
    file_name_new_words = input("file name : ")
    print("input file name that you are gonna make (file that include example sentences)")
    file_name_to_make = input("file name : ")
    print("input file name of example sentences.")
    file_name_example_sentences = input("file name : ")

    file_name_new_words = "contents/" + file_name_new_words
    file_name_to_make = "contents/" + file_name_to_make
    file_name_example_sentences = "contents/" + file_name_example_sentences

    preprocess_example_sentence = PreprocessExampleSentences(file_name_example_sentences)
    example_sentences = preprocess_example_sentence.get()

    parse_by_dot = ParseByDot(example_sentences)
    parsed_example_sentences = parse_by_dot.getSentenceSplitedAsList()

    handle_csv = HandleCsv()
    new_words = handle_csv.read(file_name_new_words)
    # structure of new_words = [english, korean, tag]
    if len(new_words[0]) >= 4:
        raise Exception("members of new words should be smaller than 3(english, meaning, tag)")

    find_sentence_include_word = FindSentenceIncludeWordNlp(parsed_example_sentences)
    
    overlaped_words = list()
    write_in_normal = HandleCsv()
    write_in_overlapped = HandleCsv()
    write_in_normal.setFileNameToWrite(file_name_to_make)
    write_in_overlapped.setFileNameToWrite('contents/overlapped_words.csv')
    check_overlap_with_original = CheckOverlapWithOriginal()
    
    print()
    for line in new_words:
        example_to_append = ""
        english = line[0]
        meaning = line[1]
        tag = line[2]
        print(english,"-", meaning, "tag :", tag)
        example_of_word = find_sentence_include_word.find(english)

        if len(example_of_word) == 0:
            print("there is no example sentences")
            example_to_append = input("input example sentence : ")
        elif len(example_of_word) >= 1 and len(example_of_word) <= 3:
            for one_example in example_of_word:
                if example_to_append == "":
                    example_to_append = one_example
                else:
                    example_to_append = example_to_append + " / " + one_example
        elif len(example_of_word) > 3:
            print("<there is so much example sentences. choose which to append.>")
            count = 1 
            for one in example_of_word:
                print(count, ":", one)
                count += 1
            chosens = getChosenNumbers(len(example_of_word))
            for one in chosens:
                example_to_append = example_to_append + " / " + example_of_word[one-1]
        
        to_write_to_file = [english, meaning, example_to_append, tag]
        if check_overlap_with_original.isOverlapped(english):
            write_in_overlapped.appendOne(to_write_to_file)
        else:
            write_in_normal.appendOne(to_write_to_file)
        print()

def getChosenNumbers(LIMIT):
    # This part should be modified to way that not uses while. But I don't have time now because I'm in school and doing Yaja.
    # I believe me in future will modify it.
    print("CAUTION : use only numbers and comma. ex)1,2,4")
    while True:
        chosed_numbers = input("Input which numbers to choose. : ")
        numbers = chosed_numbers.split(',')
        for x in range(len(numbers)):
            numbers[x] = int(numbers[x])
        cont = 0
        for one in numbers:
            if one <= 0 or one > LIMIT:
                print("input correct numbers.\n")
                cont += 1
        if cont == 0:
            break

    return numbers

if __name__ == "__main__":
    main()
