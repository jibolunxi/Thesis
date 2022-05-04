import csv

from model import get_all_repos
from utils import get_every_month

SOURCE_DATA_DIRECTORY = '/media/omen/data/thesis2022/data/second_filter/'
TARGET_DIRECTORY = '/media/omen/data/thesis2022/networks/'


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


def commit_network():
    months = get_every_month('2001-01-01', '2019-01-01')
    repo_ids = get_all_repos()
    for month in months:
        links_file = TARGET_DIRECTORY + 'commits/commit_' + month + '_links.csv'
        links_write = open(links_file, 'a', encoding='utf-8', newline='')
        links_writer = csv.writer(links_write)
        links_writer.writerow(['Source', 'Target', 'Weight', 'Type'])

        commits_dict = {}
        commit_file = SOURCE_DATA_DIRECTORY + 'commit_by_month/commit_' + month + '.csv'
        commit_read = open(commit_file, 'r', encoding='utf-8')
        commit_reader = csv.reader(commit_read)
        for commit in commit_reader:
            if commit[4] in repo_ids:
                if commits_dict.__contains__(commit[4]):
                    commits_dict[commit[4]].add(commit[3])
                else:
                    commits_set = set()
                    commits_set.add(commit[3])
                    commits_dict[commit[4]] = commits_set

        nodes = list(commits_dict.keys())
        length = len(nodes)
        for index_i in range(length):
            for index_j in range(index_i + 1, length):
                weight = len(commits_dict[nodes[index_i]] & commits_dict[nodes[index_j]]) / \
                         max(len(commits_dict[nodes[index_i]]), len(commits_dict[nodes[index_j]]))
                if weight > 0:
                    links_writer.writerow([nodes[index_i], nodes[index_j], weight, 'undirected'])


def pull_request_network():
    months = get_every_month('2010-08-01', '2019-01-01')
    repo_ids = get_all_repos()
    for month in months:
        links_file = TARGET_DIRECTORY + 'pr/pr_' + month + '_links.csv'
        links_write = open(links_file, 'a', encoding='utf-8', newline='')
        links_writer = csv.writer(links_write)
        links_writer.writerow(['Source', 'Target', 'Weight', 'Type'])

        prs_dict = {}
        pr_file = SOURCE_DATA_DIRECTORY + 'pr_by_month/pr_' + month + '.csv'
        pr_read = open(pr_file, 'r', encoding='utf-8')
        pr_reader = csv.reader(pr_read)
        for pr in pr_reader:
            if pr[-1] in repo_ids:
                if prs_dict.__contains__(pr[-1]):
                    prs_dict[pr[-1]].add(pr[-3])
                else:
                    prs_set = set()
                    prs_set.add(pr[-3])
                    prs_dict[pr[-1]] = prs_set

        nodes = list(prs_dict.keys())
        length = len(nodes)
        for index_i in range(length):
            for index_j in range(index_i + 1, length):
                weight = len(prs_dict[nodes[index_i]] & prs_dict[nodes[index_j]]) / \
                         max(len(prs_dict[nodes[index_i]]), len(prs_dict[nodes[index_j]]))
                if weight > 0:
                    links_writer.writerow([nodes[index_i], nodes[index_j], weight, 'undirected'])