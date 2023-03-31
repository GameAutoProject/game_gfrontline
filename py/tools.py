"""
    工具箱整合
"""
from airtest.core.api import *

def point_step_processor(point_list: list):
    """
        延时连点
    """
    for point in point_list:
        touch(point)
        sleep(1)


def dolls_filter(rate: list, specie: list = [], max=None):
    """
        人形筛选
        rate: list<num> 星级
        specie: list<string> 种类
        max: boolean 是否满级
    """
    list = []
    #   星级
    ratings = {
        1: (1230, 340),
        2: (1000, 340),
        3: (770, 340),
        4: (1230, 230),
        5: (1000, 230),
        6: (770, 230),
    }
    #   种类
    species = {
        "pistol": (770, 500),
        "sub_machinegun": (1000, 500),
        "rifle": (1230, 500),
        "assault_rifle": (770, 610),
        "machinegun": (1000, 610),
        "shotgun": (1230, 610),
    }
    #   是否满级
    is_max = {
        True: (770, 770),
        False: (1000, 770),
    }
    #   确认按钮
    ok_btn = (1170, 850)

    list.append((1480, 350))

    for r in rate:
        list.append(ratings[r])

    for sp in specie:
        list.append(species[sp])
    
    if max != None:
        list.append(is_max[max])

    list.append(ok_btn)

    return list

