import csv

class CSV_manual:
    def __init__(self, file_name):
        #print("생성자 호출!")
        self.file_name = file_name
        self.list_original = list()
        self.list_remember = list()
    '''def set_info(self, file_name, list_original):
        print("set_info")
        self.file_name = file_name
        self.list_original = list_original'''
    def CSV_writer(self):
        name_csv = "/home/yum_ki/" + self.file_name + ".csv"
        #print("this is name_csv" + name_csv)
        with open(name_csv, 'w', encoding = 'utf-8', newline='') as f:
            wr = csv.writer(f)
            wr.writerows(self.list_original)
    def CSV_reader(self):
        name_csv = self.file_name
        with open(name_csv, 'r', encoding = 'utf-8') as f:
            rdr = csv.reader(f)
            for line in rdr:
                self.list_original.append(line)
    def Memorize_maker(self):
        counter = 1
        for line in self.list_original:
            one = str(counter) + "." + str(line[0])+" - "+str(line[1])
            self.list_remember.append(one)
            counter += 1
    def ReturnListRemember(self):
        return self.list_remember
#End of the class CSV_manual
#To distinguish original csv module and new csv class that I made
#I wrote all the name that contains 'csv' in upper case and set class name as CSV_manual

def TxtMaker(for_mix):
    n_aft = len(for_mix)
    name_aft = input('생성될 파일의 이름을 입력하세요(확장자 붙이세요.):')
    with open(name_aft, 'w', encoding='utf-8') as f_a:
        for aa in range(0, n_aft):
            f_a.write(for_mix[aa])
            f_a.write('\n')

def pprint(list):
    for line in list:
        print(line)
#End of the pprint

def main():
    print("제작일:2020년10월16일\n박형규가 시험보기전에 영어암기하려고 만든 코드\n추후 수정 필요(대충만듦)")
    print("파일 이름 적을 때 확장자 필히 적으세요.")
    name = input("input file name : ")
    c = CSV_manual(name)
    c.CSV_reader()
    c.Memorize_maker()
    lim = c.ReturnListRemember()
    TxtMaker(lim)
    print("\n\n")
    input("Press enter to exit program......")




if __name__=="__main__":
    main()