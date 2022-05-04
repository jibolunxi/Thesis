import csv
from utils import get_every_month

SOURCE_DATA_DIRECTORY = 'G:\\thesis2022\\second_filter\\'
TARGET_DIRECTORY = 'G:\\thesis2022\\second_filter\\'


def divide_pull_request():
    fs_reader = {}
    for month in get_every_month('2001-01-01', '2022-01-01'):
        fs_reader[month] = csv.writer(open(TARGET_DIRECTORY + 'pr_by_month\\' + 'pr_' + month + '.csv',
                                           'a', encoding='utf-8', newline=''))

    pull_request_file = SOURCE_DATA_DIRECTORY + 'new_pull_requests.csv'
    pull_request_read = open(pull_request_file, 'r', encoding='utf-8')
    pull_request_reader = csv.reader(pull_request_read)
    for pull_request in pull_request_reader:
        create_time = pull_request[2]
        if create_time != '\\N':
            try:
                month_value = create_time[:7]
                fs_reader[month_value].writerow(pull_request)
            except KeyError:
                print("catch", pull_request)


def divide_commits():
    fs_reader = {}
    for month in get_every_month('2001-01-01', '2022-01-01'):
        fs_reader[month] = csv.writer(open(TARGET_DIRECTORY + 'commit_by_month\\' + 'commit_' + month + '.csv',
                                           'a', encoding='utf-8', newline=''))

    commit_file = SOURCE_DATA_DIRECTORY + 'new_commits.csv'
    commit_read = open(commit_file, 'r', encoding='utf-8')
    commit_reader = csv.reader(commit_read)
    for commit in commit_reader:
        create_time = commit[-1]
        if create_time != '\\N':
            try:
                month_value = create_time[:7]
                fs_reader[month_value].writerow(commit)
            except KeyError:
                print("catch", commit)
