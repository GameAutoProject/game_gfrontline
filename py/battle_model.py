# -*- encoding=utf8 -*-

from battle_link_action import *
from page_switch_action import *
from swap_dolls import init_swap_124e, swap_124e


def model_circle_battle(times: int, stage_name: str):
    """
    times:次数(尽量为复数)
    stage_name:关卡名 格式"12-4-e"
    wait_name:等待时长
    """

    # # 维修周期，可设计进参数  (模块作废，后续删除)
    # repair_circle=8

    # 等待时间字典
    stage_message_dict = {
        "12-4-e": {
            "time_interval": 50 + 2 * 60,
        },
    }
    
    # 判断关卡信息是否存在
    if stage_message_dict.get(stage_name) is None:
        print("!!!stage_name is None!!!")
        return

    # 关卡脚本读入
    if stage_name == "12-4-e":
        battle_into_script = battle_into_formation_about_124e
        swap_script = swap_124e
        stage_script = stage_12_4_e_script

    # 人形循环
    circle_doll_key = 0
    # 循环轮数
    index = 0

    # 脚本
    # 编码内index+1表示作战次数
    while index < times:
        # 战役选择界面切入战役界面
        combat_into_battle(stage_name)

        # 部分地图需要做位移初始化,使用swag()
        if index == 0:
            if not exists(image_124e_map):
                swipe((800,450), vector=(0,-0.6))
                pass

        # 战旗界面转移至编队界面
        p1 = battle_into_script()

        # 初始换人优化,自动感知首发换人
        if index == 0:
            circle_doll_key = init_swap_124e()
            #   test
            # print(circle_doll_key)
            # 空值处理
            if circle_doll_key is None:
                log("首发自动感知换人出现问题")
                return
        
        # 编队人形位置坐标之后用字典来顶替
        sleep(1) # 休眠1秒，防止未点击
        swap_script(circle_doll_key, (1200, 300))  

        # 编队界面退出
        sleep(1)
        touch((60, 60))  # 返回键,坐标先代替
        sleep(4)

        # # 前排维修 (游戏机制修改，该模块作废)
        # if ((index+1) % (repair_circle+1)) == 0:
        #     touch(p1)
        #     sleep(2)
        #     # 第四位 300 + 230 * (4 - 1)
        #     doll_repair((990,300))
        #     # 暂且先做此类操作，后续将部署与作战逻辑分开编写
        #     touch((1200, 780))  # 取消键,坐标先代替

        log("***THIS IS TURN {0} BATTLE ABOUT {1}***".format(index+1,stage_name))

        stage_script()
        
        #   等待刷本一轮结束
        sleep(stage_message_dict.get(stage_name)["time_interval"])
        
        # wait()

        #   结算点击
        if wait(image_battle_result_great, timeout=120, intervalfunc=log('结算失败')):
            i = 0
            while i < 5 :
                touch((1250, 50))
                sleep(1)
                i += 1
        
        log("***TURN {0} BATTLE ABOUT {1} END!***".format(index+1,stage_name))

        #   内部变量变化
        circle_doll_key += 1
        index += 1
        sleep(5)

