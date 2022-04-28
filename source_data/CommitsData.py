import csv


SOURCE_DATA_DIRECTORY = 'G:\\mysql-2019-01-01\\'
TARGET_DIRECTORY = 'G:\\thesis2022\\'


def commits_filter(pro_ids, res_file='filtered_commits.csv'):
    # 过滤结果文件
    filtered_commit_file = TARGET_DIRECTORY + res_file
    commit_write = open(filtered_commit_file, 'a', encoding='utf-8', newline='')
    commit_writer = csv.writer(commit_write)

    commit_file = SOURCE_DATA_DIRECTORY + 'commits.csv'
    commit_read = open(commit_file, 'r', encoding='utf-8')
    commit_reader = csv.reader(commit_read)
    for commit in commit_reader:
        # 数据完整性
        if len(commit) > 5:
            # 是否在项目列表中
            if pro_ids.__contains__(commit[-2]):
                commit_writer.writerow(commit)


# 获得多个开发者开发的项目
def get_mul_developers_pros():
    dev_dict = {}
    commit_file = TARGET_DIRECTORY + 'filtered_commits.csv'
    commit_read = open(commit_file, 'r', encoding='utf-8')
    commit_reader = csv.reader(commit_read)
    for commit in commit_reader:
        if commit[-2] in dev_dict:
            if dev_dict[commit[-2]] != -1:
                if dev_dict[commit[-2]] != commit[2]:
                    dev_dict[commit[-2]] = -1
        else:
            dev_dict[commit[-2]] = commit[2]

    pro_ids = set()
    for pro_id in dev_dict:
        if dev_dict[pro_id] == -1:
            pro_ids.add(pro_id)

    return pro_ids
