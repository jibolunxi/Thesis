import csv

SOURCE_DATA_DIRECTORY = '/media/omen/data/thesis2022/networks/'
TARGET_DIRECTORY = '/media/omen/data/thesis2022/ecosystems/'


def label_by_fork_and_org():
    fork_nodes = {}
    fork_node_file = SOURCE_DATA_DIRECTORY + 'fork_nodes.csv'
    fork_node_read = open(fork_node_file, 'r', encoding='utf-8')
    fork_node_reader = csv.reader(fork_node_read)
    next(fork_node_reader)
    for fork_node in fork_node_reader:
        fork_nodes[fork_node[0]] = fork_node[1]

    forked_counts = {}
    fork_link_file = SOURCE_DATA_DIRECTORY + 'fork_links.csv'
    fork_link_read = open(fork_link_file, 'r', encoding='utf-8')
    fork_link_reader = csv.reader(fork_link_read)
    next(fork_link_reader)
    for fork_link in fork_link_reader:
        if fork_link[1] in forked_counts:
            forked_counts[fork_link[1]] += 1
        else:
            forked_counts[fork_link[1]] = 1

    ori_pro_ids = set()
    for key in forked_counts:
        if forked_counts[key] > 5:
            ori_pro_ids.add(key)

    label = 0
    org_labels = {}
    for pro_id in ori_pro_ids:
        org = fork_nodes[pro_id].split('/')[0]
        if org not in org_labels:
            org_labels[org] = label
            label += 1

    nodes_label = {}
    for node in fork_nodes:
        org = fork_nodes[node].split('/')[0]
        if org in org_labels:
            nodes_label[node] = org_labels[org]

    fork_link_read = open(fork_link_file, 'r', encoding='utf-8')
    fork_link_reader = csv.reader(fork_link_read)
    next(fork_link_reader)
    for fork_link in fork_link_reader:
        if fork_link[1] in nodes_label:
            nodes_label[fork_link[0]] = nodes_label[fork_link[1]]
        else:
            nodes_label[fork_link[1]] = label
            nodes_label[fork_link[0]] = label
            label += 1

    labels_file = TARGET_DIRECTORY + 'eco_labels.csv'
    labels_write = open(labels_file, 'a', encoding='utf-8', newline='')
    labels_writer = csv.writer(labels_write)
    labels_writer.writerow(['Id', 'Label'])
    for node_id in nodes_label:
        labels_writer.writerow([node_id, nodes_label[node_id]])


def get_all_repos():
    repo_ids = set()
    labels_file = TARGET_DIRECTORY + 'eco_labels.csv'
    labels_read = open(labels_file, 'r', encoding='utf-8')
    labels_reader = csv.reader(labels_read)
    next(labels_reader)
    for label in labels_reader:
        repo_ids.add(label[0])

    return repo_ids
