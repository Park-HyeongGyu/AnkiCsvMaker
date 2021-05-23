from modules.handle_csv import HandleCsv

class CheckOverlapWithOriginal:
    def __init__(self):
        with open("modules/original_file_name.txt", 'r', encoding = 'utf-8') as f:
            self.original_file_name = f.readline()
        self.original_words = list()
        csv_handler = HandleCsv()
        self.original_file_name = "modules/" + self.original_file_name
        original_csv = csv_handler.read_tsv(self.original_file_name)
        # When handling csv, I use 2 dimension list at now. (wanna use pandas but don't know how.)
        for line in original_csv:
            self.original_words.append(line[0])
    
    def isOverlapped(self, word):
        if word in self.original_words:
            return True
        else:
            return False

def test():
    pass

if __name__ == "__main__":
    test()
