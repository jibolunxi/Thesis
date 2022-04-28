import csv


SOURCE_DATA_DIRECTORY = 'G:\\mysql-2019-01-01\\'
TARGET_DIRECTORY = 'G:\\thesis2022\\'


def watchers_filter(pro_ids, res_file='filtered_watchers.csv'):
    # 过滤结果文件
    filtered_watcher_file = TARGET_DIRECTORY + res_file
    watcher_write = open(filtered_watcher_file, 'a', encoding='utf-8', newline='')
    watcher_writer = csv.writer(watcher_write)

    watcher_file = SOURCE_DATA_DIRECTORY + 'watchers.csv'
    watcher_read = open(watcher_file, 'r', encoding='utf-8')
    watcher_reader = csv.reader(watcher_read)
    for watcher in watcher_reader:
        # 数据完整性
        if len(watcher) > 2:
            # 是否在项目列表中
            if pro_ids.__contains__(watcher[0]):
                watcher_writer.writerow(watcher)
