import csv


SOURCE_DATA_DIRECTORY = 'G:\\mysql-2019-01-01\\'
TARGET_DIRECTORY = 'G:\\thesis2022\\'


def pr_history_filter_by_status():
    # 过滤结果文件
    filtered_pull_request_file = TARGET_DIRECTORY + 'filtered_pull_request_history.csv'
    pull_request_write = open(filtered_pull_request_file, 'a', encoding='utf-8', newline='')
    pull_request_writer = csv.writer(pull_request_write)

    pull_request_file = SOURCE_DATA_DIRECTORY + 'pull_request_history.csv'
    pull_request_read = open(pull_request_file, 'r', encoding='utf-8')
    pull_request_reader = csv.reader(pull_request_read)
    for pull_request in pull_request_reader:
        # 数据完整性
        if len(pull_request) > 4:
            # 状态是否为opened
            if pull_request[-2] == 'opened':
                pull_request_writer.writerow(pull_request)


def pull_requests_filter(pro_ids, res_file='filtered_pull_requests.csv'):
    # 过滤结果文件
    filtered_pull_request_file = TARGET_DIRECTORY + res_file
    pull_request_write = open(filtered_pull_request_file, 'a', encoding='utf-8', newline='')
    pull_request_writer = csv.writer(pull_request_write)

    pull_request_file = SOURCE_DATA_DIRECTORY + 'pull_requests.csv'
    pull_request_read = open(pull_request_file, 'r', encoding='utf-8')
    pull_request_reader = csv.reader(pull_request_read)
    for pull_request in pull_request_reader:
        # 数据完整性
        if len(pull_request) > 6:
            # 是否在项目列表中
            if pro_ids.__contains__(pull_request[1]) and pro_ids.__contains__(pull_request[2]):
                pull_request_writer.writerow(pull_request[:3])


def pr_and_history_merge():
    # 合并结果文件
    filtered_pull_request_file = TARGET_DIRECTORY + 'merged_pull_requests.csv'
    pull_request_write = open(filtered_pull_request_file, 'a', encoding='utf-8', newline='')
    pull_request_writer = csv.writer(pull_request_write)

    pr_dict = {}
    pull_request_file = TARGET_DIRECTORY + 'filtered_pull_requests.csv'
    pull_request_read = open(pull_request_file, 'r', encoding='utf-8')
    pull_request_reader = csv.reader(pull_request_read)
    for pull_request in pull_request_reader:
        pr_dict[pull_request[0]] = pull_request[1:]

    pull_request_his_file = TARGET_DIRECTORY + 'filtered_pull_request_history.csv'
    pull_request_his_read = open(pull_request_his_file, 'r', encoding='utf-8')
    pull_request_his_reader = csv.reader(pull_request_his_read)
    for pull_request_his in pull_request_his_reader:
        if pull_request_his[1] in pr_dict:
            pull_request_writer.writerow(pull_request_his + pr_dict[pull_request_his[1]])


def merged_pr_filter(pro_ids, res_file='new_pull_requests.csv'):
    # 过滤结果文件
    filtered_pull_request_file = TARGET_DIRECTORY + res_file
    pull_request_write = open(filtered_pull_request_file, 'a', encoding='utf-8', newline='')
    pull_request_writer = csv.writer(pull_request_write)

    pull_request_file = TARGET_DIRECTORY + 'merged_pull_requests.csv'
    pull_request_read = open(pull_request_file, 'r', encoding='utf-8')
    pull_request_reader = csv.reader(pull_request_read)
    for pull_request in pull_request_reader:
        # 数据完整性
        if len(pull_request) > 6:
            # 是否在项目列表中
            if pro_ids.__contains__(pull_request[-1]) and pro_ids.__contains__(pull_request[-2]):
                pull_request_writer.writerow(pull_request)
