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
# End of the class CSV_manual
# To distinguish original csv module and new csv class that I made
# I wrote all the name that contains 'csv' in upper case and set class name as CSV_manual
    
                  
        
def list_maker():
    column = int(input("input a column : "))
    maker_list = []
    line = 0
    print("if you input 'end' then the input proceds end")
    while True:
        count = 0
        maker_list.append([])
        # print("appending line......")
        while count < column:
            tem = input(str(line+1) + ": ")
            if tem == "end":
                del maker_list[line]
                return maker_list
            maker_list[line].append(tem)
            # print("appending tem.... this is count" + str(count) + " this is line" + str(line))
            count += 1
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
