import csv
from Eng_Anki_CSV_ForTag import HowMakeTag

class CSV_manual:
    def __init__(self, file_name):
        #print("생성자 호출!")
        self.d_file_name = "C:\Users\user\Desktop\csvs\Eng\ " + file_name + ".csv"
        self.d_file_name = self.d_file_name.replace(" ", "")
    '''def set_info(self, file_name, list_original):
        print("set_info")
        self.file_name = file_name
        self.list_original = list_original'''
    def CSV_adder(self, content):
        with open(self.d_file_name, 'a', encoding = 'utf-8', newline='') as f:
            wr = csv.writer(f)
            wr.writerow(content)
#End of the class CSV_manual
#To distinguish original csv module and new csv class that I made
#I wrote all the name that contains 'csv' in upper case and set class name as CSV_manual
    
                  
        
def list_maker():
    column = int(input("input a column : "))
    tag = input("input a tag : ")
    line = 1
    file_name = input("input file name : ")
    CSV_module = CSV_manual(file_name)
    print("if you input 'end' then the input proceds end")
    while True:
        count = 0
        #print("appending line......")
        content_list = []
        while count <= column:
            if count==column:#In case of example sentence.
                tem = input("Example of "+str(line)+": ")
                if tem == "end":
                    return 0 
                content_list.append(tem)
            else:
                tem = input(str(line) + ": ")
                if tem == "end":
                    return 0
                content_list.append(tem)
            #print("appending tem.... this is count" + str(count) + " this is line" + str(line))
            count += 1
        content_list.append(tag)
        CSV_module.CSV_adder(content_list)
        line += 1
        print()
#End of the maker

def pprint(list):
    for line in list:
        print(line)
#End of the pprint

#From here, int main()
def main():
    print("제작자:박형규")
    print("제작일:2020년4월30일")
    print("예문 모듈 제작일:2020년 11월 29일")
    print("append 수정일:2021년2월1일")
    print("입력받은 텍스트들을 csv파일로 만들어주는 프로그램.")
    print("저장 경로:D:")
    print("위의 폴더 안에 자동으로 .csv가 붙은 파일을 만들어줍니다.")
    HowMakeTag()
    list_maker()
    print("Press enter to exit program......", end="")
    input()

if __name__ == "__main__":
    main()
