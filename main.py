import csv
import os

file_path = "order"
filename = "simulation.log"

def main():
    group_list = []
    for directory in os.listdir(file_path):
        with open(os.path.join(file_path, directory + "/" + filename), 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            group_cnt = 0
            for row in reader:
                if row[0] == 'GROUP' and row[6] == 'OK':
                    group_cnt += 1
            group_list.append([group_cnt, os.path.join(file_path, directory + "/" + filename)])
    group_list.sort(reverse=True)
    print(group_list[0])

if __name__ == '__main__':
    main()
