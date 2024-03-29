# 各关卡行为脚本

from airtest.core.api import *

from image_source import *


time_sleep = 5


def _lay_army(point, echelon):
    """放置选择梯队 point:位置 echelon:选择梯队"""
    touch(point)
    # touch(wait(echelon, timeout=120, intervalfunc=touch(point)))
    sleep(1)
    touch(image_certain)
    sleep(1)


def stage_12_4_e_script():
    """124e刷关脚本"""
    points = wait(image_124e_map, timeout=60)
    #   地图内脚本
    if points:
        X = points[0]
        Y = points[1]
        #   设置点击位置
        point_put_1 = (X-93, Y+374)
        point_put_2 = (X-208, Y-395)
        point_a = (X+118, Y-63)
        point_b = (X+339, Y-62)
        #   放人
        sleep(2)
        _lay_army(point_put_1, image_echelon_1)
        sleep(1)
        _lay_army(point_put_2, image_echelon_2)
        #   开始
        touch(image_start_battle_btn)
        sleep(time_sleep)
        #   补给
        touch(point_put_2)
        sleep(1)
        touch(point_put_2)
        supply_btn = wait(image_supply_btn, timeout=240)
        touch(supply_btn)
        sleep(time_sleep)
        #   计划作战
        touch(point_put_1)
        touch(image_plan_off_btn)
        sleep(1)
        touch(point_a)
        sleep(1)
        touch(point_b)
        sleep(1)
        touch(image_execute_plan)
    
    def supply(point:tuple):
        touch(point)
        touch(wait(image_supply_btn, timeout=120, intervalfunc=supply(point)))
