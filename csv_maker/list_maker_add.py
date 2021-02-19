import csv

class csvs:
    def __init__(self, filename):
        self.file_name = filename
    def reader(self):
        line_numbers = 0
        try:
            f = open(self.file_name, 'r', encoding = 'utf-8')
            line_numbers = len(f.readlines())
            f.close()
        except:
            line_numbers = 0
        return line_numbers
    def adder(self, content):
        with open(self.file_name, 'a+', encoding = 'utf-8', newline='') as f:
            wr = csv.writer(f)
            wr.writerow(content)

def list_maker(filename_with_path_ended_with_.csv):
    for_csv = csvs(filename_with_path_ended_with_.csv) 
    column = int(input("input a column : "))
    tag = input("input a tag : ")
    line = for_csv.reader() + 1
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
        for_csv.adder(content_list)
        line += 1
        print()
#End of the maker