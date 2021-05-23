from modules.check_overlap_with_original import CheckOverlapWithOriginal
from modules.handle_csv import HandleCsv

def main():
    file_prior = input("Input file name that will be checked : ")
    will_be_made = input("Input file name that will be made : ")
    handle_csv = HandleCsv()
    
    file_prior = "contexts/" + file_prior
    will_be_made = "contexts/" + will_be_made
    prior_words = handle_csv.read(file_prior)

    check_overlap_with_original = CheckOverlapWithOriginal()
    write_in_normal = HandleCsv()
    write_in_overlapped = HandleCsv()
    write_in_normal.setFileNameToWrite(will_be_made)
    write_in_overlapped.setFileNameToWrite("contexts/overlapped_words.csv")

    for one in prior_words:
        english = one[0]
        if check_overlap_with_original.isOverlapped(english):
            print("overlapped :", one)
            write_in_overlapped.appendOne(one)
        else:
            write_in_normal.appendOne(one)

if __name__ == "__main__":
    main()
