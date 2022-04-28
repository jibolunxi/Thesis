import csv

SOURCE_DATA_DIRECTORY = 'G:\\thesis2022\\'

if __name__ == '__main__':
    count = 0
    pro_file = SOURCE_DATA_DIRECTORY + 'new_projects.csv'
    pro_read = open(pro_file, 'r', encoding='utf-8')
    pro_reader = csv.reader(pro_read)
    for pro in pro_reader:
        count += 1
    print(count)
