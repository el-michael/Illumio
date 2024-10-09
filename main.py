import csv

LOOKUP_TABLE_FILE = "lookup_table.csv"

def read_csv_file(filename):
    tags_dict = {}
    with open("lookup_table.csv", "r") as file:
        csv_file = csv.reader(file)
        for line in csv_file:
            print(line)
            dst_port = line[0].strip()
            protocol = line[1].strip()
            tag = line[2].strip()
            tags_dict[(dst_port, protocol)] = tag
    print(tags_dict)
def main():
    read_csv_file(LOOKUP_TABLE_FILE)


main()