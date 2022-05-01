import csv

SOURCE_DATA_DIRECTORY = 'G:\\thesis2022\\second_filter\\'
TARGET_DIRECTORY = 'G:\\networks\\'


def fork_network():
    links_file = TARGET_DIRECTORY + 'fork_links.csv'
    links_write = open(links_file, 'a', encoding='utf-8', newline='')
    links_writer = csv.writer(links_write)
    links_writer.writerow(['Source', 'Target', 'Weight', 'Type'])
    nodes_file = TARGET_DIRECTORY + 'fork_nodes.csv'
    nodes_write = open(nodes_file, 'a', encoding='utf-8', newline='')
    nodes_writer = csv.writer(nodes_write)
    nodes_writer.writerow(['Id', 'Label'])
    nodes_id = set()

    pros_name = {}
    pro_file = SOURCE_DATA_DIRECTORY + 'new_projects.csv'
    pro_read = open(pro_file, 'r', encoding='utf-8')
    pro_reader = csv.reader(pro_read)
    for pro in pro_reader:
        pros_name[pro[0]] = pro[1][29:]

    pro_read = open(pro_file, 'r', encoding='utf-8')
    pro_reader = csv.reader(pro_read)
    for pro in pro_reader:
        if pro[-4] != '\\N' and pro[-4] in pros_name:
            nodes_id.add(pro[0])
            nodes_writer.writerow([pro[0], pro[1][29:]])
            links_writer.writerow([pro[0], pro[-4], 1, 'undirected'])
            if pro[-4] not in nodes_id:
                nodes_id.add(pro[-4])
                nodes_writer.writerow([pro[-4], pros_name[pro[-4]]])



