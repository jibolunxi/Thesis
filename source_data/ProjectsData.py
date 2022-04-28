import csv


SOURCE_DATA_DIRECTORY = 'G:\\mysql-2019-01-01\\'
TARGET_DIRECTORY = 'G:\\thesis2022\\'


def projects_filter():
    # 过滤结果文件
    filtered_pro_file = TARGET_DIRECTORY + 'filtered_projects.csv'
    pro_write = open(filtered_pro_file, 'a', encoding='utf-8', newline='')
    pro_writer = csv.writer(pro_write)

    pro_file = SOURCE_DATA_DIRECTORY + 'projects.csv'
    pro_read = open(pro_file, 'r', encoding='utf-8')
    pro_reader = csv.reader(pro_read)
    for pro in pro_reader:
        # 数据完整性
        if len(pro) > 10:
            # 未被删除
            if pro[-3] == '0':
                # 语言不为None
                if pro[-6] != '\\N' and pro[-5][0] != ',':
                    # readme不为None
                    if pro[4] != '\\N':
                        if len(pro) == 11:
                            pro_writer.writerow(pro)
                        else:
                            new_pro = pro[0:4]
                            description_str = ''
                            for index in range(len(pro) - 10):
                                description_str += ' ' + pro[4 + index].replace('\\', ' ').replace('\"', ' ')\
                                    .replace('\'', ' ')
                            new_pro.append(description_str)
                            new_pro = new_pro + pro[-6:]
                            if len(new_pro) == 11:
                                pro_writer.writerow(new_pro)


def repo_labels_filter(pro_ids, res_file='filtered_repo_labels.csv'):
    # 过滤结果文件
    filtered_repo_label_file = TARGET_DIRECTORY + res_file
    repo_label_write = open(filtered_repo_label_file, 'a', encoding='utf-8', newline='')
    repo_label_writer = csv.writer(repo_label_write)

    repo_label_file = SOURCE_DATA_DIRECTORY + 'repo_labels.csv'
    repo_label_read = open(repo_label_file, 'r', encoding='utf-8')
    repo_label_reader = csv.reader(repo_label_read)
    for repo_label in repo_label_reader:
        # 数据完整性
        if len(repo_label) > 2:
            # 是否在项目列表中
            if pro_ids.__contains__(repo_label[1]):
                repo_label_writer.writerow(repo_label)


def project_members_filter(pro_ids, res_file='filtered_project_members.csv'):
    # 过滤结果文件
    filtered_project_member_file = TARGET_DIRECTORY + res_file
    project_member_write = open(filtered_project_member_file, 'a', encoding='utf-8', newline='')
    project_member_writer = csv.writer(project_member_write)

    project_member_file = SOURCE_DATA_DIRECTORY + 'project_members.csv'
    project_member_read = open(project_member_file, 'r', encoding='utf-8')
    project_member_reader = csv.reader(project_member_read)
    for project_member in project_member_reader:
        # 数据完整性
        if len(project_member) > 3:
            # 是否在项目列表中
            if pro_ids.__contains__(project_member[0]):
                project_member_writer.writerow(project_member)


def projects_filter_by_committer(pro_ids, res_file='new_projects.csv'):
    # 过滤结果文件
    filtered_project_file = TARGET_DIRECTORY + res_file
    project_write = open(filtered_project_file, 'a', encoding='utf-8', newline='')
    project_writer = csv.writer(project_write)

    project_file = TARGET_DIRECTORY + 'filtered_projects.csv'
    project_read = open(project_file, 'r', encoding='utf-8')
    project_reader = csv.reader(project_read)
    for project in project_reader:
        # 是否在项目列表中
        if pro_ids.__contains__(project[0]):
            project_writer.writerow(project)


def get_pros_id():
    pro_ids = set()
    pro_file = TARGET_DIRECTORY + 'filtered_projects.csv'
    pro_read = open(pro_file, 'r', encoding='utf-8')
    pro_reader = csv.reader(pro_read)
    for pro in pro_reader:
        pro_ids.add(pro[0])

    return pro_ids
