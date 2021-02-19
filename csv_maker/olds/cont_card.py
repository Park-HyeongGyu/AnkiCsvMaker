import csv
# 1만단어를 위한 1만개의퀴즈 1권 기초일본어 + JLPT N3태그를 자동으로 뒤에 붙여줌
# column은 자동으로 3으로 설정(Kanzi - Korean - Hiragana)

class CSV_manual:
    def SetName(self, file_name):
        self.file_name = file_name
    def SetList(self,list_):
        self.lister = list_
    
    def CSV_writer(self):
        name_csv = 'D:\\' + self.file_name + ".csv" #30
        with open(name_csv, 'a', encoding = 'utf-8', newline='') as f:
            wr = csv.writer(f)
            wr.writerow(self.lister)
    # 배열(클래스 생성자에서 초기화 된)을 csv파일에 그대로 써줌
    def CSV_reader(self):
        name_csv = self.file_name + ".csv"
        with open(name_csv, 'r', encoding = 'utf-8') as f:
            rdr = csv.reader(f)
            for line in rdr:
                print(line)
    
# End of the class CSV_manual
# To distinguish original csv module and new csv class that I made
# I wrote all the name that contains 'csv' in upper case and set class name as CSV_manual
    
                  
        
def list_maker():
    numbers = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    marks = ['♠', '♦', '♥', '♣']
    cards = []
    for mar in range(4):
        for num in range(13):
            cards.append(numbers[num]+marks[mar])
    #print(cards)
    column = 4
    maker_list = []
    line = 0
    tag = "playing_card_memorization"

    name = input("input name : ")
    writer = CSV_manual()
    writer.SetName(name)

    print("if you input 'end' or '끝' or 'おわり' then the input proceds end")
    while line < 52:
        count = 0
        maker_list.append([])
        # print("appending line......")
        while count < column:
            #print("this is count", count)
            if count == 0:
                print("Card_" + str(line + 1) + ":",cards[line])
                tem = cards[line] 
                maker_list[line].append(tem)
                count += 1
            elif count == 1: 
                print(" P _" + str(line + 1) + ":", end='')
                tem = input()
                if tem == "end" or tem == '끝' or tem == 'おわり':
                    del maker_list[line]
                    return maker_list
                maker_list[line].append(tem)
                count += 1
            elif count == 2:
                print(" O _" + str(line + 1) + ":", end='')
                tem = input()
                if tem == "end" or tem == '끝' or tem == 'おわり':
                    del maker_list[line]
                    return maker_list
                maker_list[line].append(tem)
                count += 1
            elif count == 3:
                print(" A _" + str(line + 1) + ":", end='')
                tem = input() 
                if tem == "end" or tem == '끝' or tem == 'おわり':
                    del maker_list[line]
                    return maker_list
                maker_list[line].append(tem)
                count += 1
            else:
                print("Error on while True in def list_maker")
        maker_list[line].append(tag)
        writer.SetList(maker_list[line])
        writer.CSV_writer()
        # main_list.append([])
        line +=1
        print()
# End of the maker

def pprint(list):
    for line in list:
        print(line)
# End of the pprint

# From here, int main()
def main():
    print("제작자:박형규")
    print("제작일:2021-0114")
    print("카드 52장 암기하는데 POA 외우기 위해서 기존 일본어 anki 등록 수정해서 만듦.")
    print("")
    main_list = list_maker()
    input("press enter to end program......")

if __name__ == "__main__":
    main()
