import csv
from Eng_ForExample import list_maker, pprint, HowMakeTag

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
        name_csv = "/home/yum_ki/anki_csv_files/" + self.file_name + ".csv"
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

#From here, int main()
def main():
    print("제작자:박형규")
    print("제작일:2020년4월30일")
    print("리눅스 포매팅:2020년 11월 25일")
    print("예문 모듈 제작일:2020년 11월 29일")
    print("입력받은 텍스트들을 csv파일로 만들어주는 프로그램.")
    print("저장 경로: /home/yum_ki/anki_csv_files/")
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
