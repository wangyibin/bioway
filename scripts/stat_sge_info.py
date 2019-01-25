#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time: 2019/1/25 13:57

#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
A script for stat sge used info.
"""

import os
import sys


def stat_sge_used(mode='r',user="all"):
    info = os.popen("qstat -u '*'")
    info_dict = {}
    head = info.readline().strip().split()

    for line in info:
        data = line.strip().split()

        if len(data) >= 8 and data[4] == mode:
            if data[3] not in info_dict:
                info_dict[data[3]] = 0
            info_dict[data[3]] += int(data[8])

    info_dict = sorted(info_dict.items(),
                key=lambda x:x[1],reverse=True)

    total = 0
    for item in info_dict:
        print("{0}\t{1}".format(item[0],item[1]))
        total += item[1]

    print("Total:\t{}".format(total))



if __name__ == "__main__":
    stat_sge_used()
