import csv

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
        name_csv = "D:\CSV_For_Anki\Eng_started_200130\ " + self.file_name + ".csv"
        name_csv = name_csv.replace(" ", "")
        #print("this is name_csv" + name_csv)
        with open(name_csv, 'w', encoding = 'utf-8', newline='') as f:
            wr = csv.writer(f)
            wr.writerows(self.list_original)
    def CSV_reader(self):
        name_csv = self.file_name + ".csv"
        with open(name_csv, 'r', encoding = 'utf-8') as f:
            rdr = csv.reader(f)
            for line in rdr:
                print(line)
#End of the class CSV_manual
#To distinguish original csv module and new csv class that I made
#I wrote all the name that contains 'csv' in upper case and set class name as CSV_manual
    
                  
        
def list_maker():
    column = int(input("input a column : "))
    tag = input("input a tag : ")
    maker_list = []
    line = 0
    print("if you input 'end' then the input proceds end")
    while True:
        count = 0
        maker_list.append([])
        #print("appending line......")
        while count <= column:
            if count==column:#In case of example sentence.
                tem = input("Example of "+str(line+1)+": ")
                if tem == "end":
                    del maker_list[line]
                    return maker_list
                maker_list[line].append(tem)
            else:
                tem = input(str(line+1) + ": ")
                if tem == "end":
                    del maker_list[line]
                    return maker_list
                maker_list[line].append(tem)
            #print("appending tem.... this is count" + str(count) + " this is line" + str(line))
            count += 1
        #main_list.append([])
        maker_list[line].append(tag)
        line +=1
        print()
#End of the maker

def pprint(list):
    for line in list:
        print(line)
#End of the pprint

def HowMakeTag():
    print("<태그 붙이는법>")
    print("----모의고사----")
    print("%Y%MH%G -> %G:학년")
    print("Ex) 2020년 6월 고3모의고사: 20063")
    print("----문제집----")
    print("수특:st%Y%T -> %T:영어=>E, 영어독해연습=>EP")
    print("만약 문제 번호를 추가하고 싶다면 st%Y%T%P%N -> %P:page, %N:number")
    print("Ex) 2021년 수능 대비 수능특강 영어 : st20E")


#From here, int main()
def main():
    print("제작자:박형규")
    print("제작일:2020년4월30일")
    print("예문 모듈 제작일:2020년 11월 29일")
    print("입력받은 텍스트들을 csv파일로 만들어주는 프로그램.")
    print("저장 경로:D:\CSV_For_Anki\Eng_started_200130")
    print("위의 폴더 안에 자동으로 .csv가 붙은 파일을 만들어줍니다.")
    HowMakeTag()
    main_list = list_maker()
    print("")
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
