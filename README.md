# Thesis
#### 1 源数据
##### 1.1 下载地址
- https://ghtorrent.org/downloads.html
- 数据集已停止更新，最新数据集中的2019年下半年数据异常
- 选择2019-01-01前数据
##### 1.2 数据选择
- 项目相关：projects.csv、project_members.csv、repo_labels.csv
- 开发者相关：users.csv、organization_members.csv
- 开发者活动相关：watchers.csv、commits.csv、pull_requests.csv、pull_request_history.csv

#### 2 数据预处理
##### 2.1 projects.csv
- 删除deleted=1的项目
- 删除Language=None的项目
- 删除Description=None的项目
- projects_filter()
##### 2.2 依据过滤后的projects筛选其他数据
- watchers_filter()、commits_filter()、pull_requests_filter()
- repo_labels_filter()、project_members_filter()
##### 2.3 pull request数据处理
- pull_request_history依据状态过滤，只留'opened'
- pr_history_filter_by_status()
- 合并pull_request_history和pull_requests
- pr_and_history_merge()
##### 2.4 去除只有一个人参与的项目
- get_mul_developers_pros()
- 代码冗余，已移除

