

# 获取月份
import datetime


def get_every_month(begin_date_str, end_date_str):
    month_list = [0, ]
    begin_date = datetime.datetime.strptime(begin_date_str, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")[:-3]
        if date_str != month_list[-1]:
            month_list.append(date_str)
        begin_date += datetime.timedelta(weeks=3)
    return month_list[1:]
