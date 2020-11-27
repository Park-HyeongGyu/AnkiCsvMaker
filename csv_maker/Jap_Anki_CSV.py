import csv
#1만단어를 위한 1만개의퀴즈 1권 기초일본어 + JLPT N3태그를 자동으로 뒤에 붙여줌
# column은 자동으로 3으로 설정(Kanzi - Korean - Hiragana)

class CSV_manual:
    def __init__(self, file_name, list_original):
        #print("생성자 호출!")
        self.file_name = file_name
        self.list_original = list_original
    '''def set_info(self, file_name, list_original):
        print("set_info")
        self.file_name = file_name
        self.list_original = list_original'''
    
    def CSV_writer(self):
        name_csv = 'D:\CSV_For_Anki\Jap_FirstBook\ ' + self.file_name + ".csv" #30
        name_csv = name_csv.replace(" ", "")
        with open(name_csv, 'w', encoding = 'utf-8', newline='') as f:
            wr = csv.writer(f)
            wr.writerows(self.list_original)
    # 배열(클래스 생성자에서 초기화 된)을 csv파일에 그대로 써줌
    def CSV_reader(self):
        name_csv = self.file_name + ".csv"
        with open(name_csv, 'r', encoding = 'utf-8') as f:
            rdr = csv.reader(f)
            for line in rdr:
                print(line)
    
#End of the class CSV_manual
#To distinguish original csv module and new csv class that I made
#I wrote all the name that contains 'csv' in upper case and set class name as CSV_manual
    
                  
        
def list_maker(var_type):
    column = 4
    maker_list = []
    line = 0
    print("if you input 'end' or '끝' or 'おわり' then the input proceds end")
    tag = '100_1만단어를위한_1만개의퀴즈_1권_기초일본어+JLPT_N3'
    while True:
        count = 0
        maker_list.append([])
        #print("appending line......")
        while count < column:
            if count == 0:
                print("漢  字  _" + str(line + 1) + ":", end='')
                tem = input()
                if tem == "end" or tem == '끝' or tem == 'おわり':
                    del maker_list[line]
                    return maker_list
                maker_list[line].append(tem)
                # print("appending tem.... this is count" + str(count) + " this is line" + str(line))
                count += 1
            elif count == 2:
                print("한글(뜻)_" + str(line + 1) + ":", end='')
                tem = input()
                if tem == "end" or tem == '끝' or tem == 'おわり':
                    del maker_list[line]
                    return maker_list
                maker_list[line].append(tem)
                # print("appending tem.... this is count" + str(count) + " this is line" + str(line))
                count += 1
            elif count == 1:
                print("ひらがな_" + str(line + 1) + ":", end='')
                tem = input()
                if tem == "end" or tem == '끝' or tem == 'おわり':
                    del maker_list[line]
                    return maker_list
                maker_list[line].append(tem)
                # print("appending tem.... this is count" + str(count) + " this is line" + str(line))
                count += 1
            elif count == 3:
                #print("T y p e _" + str(line + 1) + ":", end='')
                tem = var_type
                if tem == "end" or tem == '끝' or tem == 'おわり':
                    del maker_list[line]
                    return maker_list
                maker_list[line].append(tem)
                # print("appending tem.... this is count" + str(count) + " this is line" + str(line))
                count += 1
            else:
                print("Error on while True in def list_maker")
            '''tem = input()
            if tem == "end" or tem == '끝' or tem == 'おわり':
                del maker_list[line]
                return maker_list
            maker_list[line].append(tem)
            #print("appending tem.... this is count" + str(count) + " this is line" + str(line))
            count += 1'''
        maker_list[line].append(tag)
        #main_list.append([])
        line +=1
        print()
#End of the maker

def pprint(list):
    for line in list:
        print(line)
#End of the pprint
'''
<var_type>
1:명사
2:1동사
3:2동사
4:3동사
5:い형용사
6:な형용사
7:형(연체사)
8:형용사 표현
9:부사
10:대명사
11:감동사
12:조사
'''

#From here, int main()
def main():
    print("제작자:박형규")
    print("anki 일본어 등록을 위해 만들어진 버전")
    print("저장 경로:D:\CSV_For_Anki\Jap_FirstBook\ \n")
    var_type = input("type을 입력하세요 : ")
    print("")
    main_list = list_maker(var_type)
    name = input("input a name of csv file which you want to make : ")
    '''name = "testing"
    main_list = [["first", "one"], ["second", "two"]]'''
    a = CSV_manual(name, main_list)
    a.CSV_writer()
    print("writing csv file process is end")
    input("press enter to end program......")
    '''print("from here, made to test csv file\n\n")
    a.CSV_reader()'''

if __name__ == "__main__":
    main()
