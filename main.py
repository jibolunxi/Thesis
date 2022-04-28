from source_data import projects_filter, get_pros_id, watchers_filter, repo_labels_filter, \
    project_members_filter, commits_filter, pull_requests_filter, pr_history_filter_by_status, pr_and_history_merge, \
    get_mul_developers_pros, merged_pr_filter, projects_filter_by_committer


# 数据筛选
def data_filter():
    # projects
    projects_filter()

    # others
    pro_ids = get_pros_id()
    commits_filter(pro_ids)
    watchers_filter(pro_ids)
    repo_labels_filter(pro_ids)
    project_members_filter(pro_ids)
    pull_requests_filter(pro_ids)

    # pull request deal
    pr_history_filter_by_status()
    pr_and_history_merge()

    print('end')


def main():
    # 数据筛选
    data_filter()


if __name__ == '__main__':
    main()
