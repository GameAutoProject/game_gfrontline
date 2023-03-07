"""换人"""
from airtest.core.api import *

from image_source import image_dolls as dolls


def swap_124e(doll_key: int, change_point: tuple):
    """
        124e,换人,默认hk416.k11互换
    """
    dolls_list = {
        0: "hk416",
        1: "k11",
    }

    # 越位溢出处理
    doll_key = doll_key % len(dolls_list)

    if doll_key is None:
        print("    doll_key is None!!  ")
        return

    # touch((1200,300))
    touch(change_point)
    sleep(2)
    point_step_processor(_dolls_filter([5, 6], ["assault_rifle"], True))
    # _dolls_search(dolls[dolls_list[doll_key]])
    print(doll_key)
    print(dolls_list.get(doll_key))
    print(dolls.get(dolls_list.get(doll_key)))
    _dolls_search(dolls.get(dolls_list.get(doll_key)))


def init_swap_124e() -> int:
    # 暂不做页面感知确认,请确保切入编队页面
    doll_0 = dolls["hk416"]
    doll_1 = dolls["k11"]

    for d in doll_0:
        if exists(d):
            return 1

    for d in doll_1:
        if exists(d):
            return 0

    return None




def point_step_processor(point_list: list):
    """
        延时连点
    """
    for point in point_list:
        touch(point)
        sleep(1)


def _dolls_filter(rate: list, specie: list, max):
    """
        人形筛选
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

    list.append(is_max[max])
    list.append(ok_btn)

    return list


def _dolls_search(doll_pic:dict):
    for doll in doll_pic:
        is_searched = exists(doll)
        if is_searched:
            touch(is_searched)
            sleep(3)
            break
