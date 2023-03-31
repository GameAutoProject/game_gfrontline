# 界面切换行为

from airtest.core.api import *

from image_source import *

from event_watcher import *


sleep_time = 5


def battle_into_formation_about_124e():
    """
        124e地图切换到编队界面
    """
    point = wait(image_124e_map, timeout=30)
    if point:
        battle_into_formation((point[0]-125, point[1]+347))
    
    return (point[0]-125, point[1]+347)

def battle_into_formation(point: tuple):
    touch(point)
    sleep(sleep_time)
    #  判断是否为重装机场  重装/普通编队   选择普通编队
    choose_norm = exists(image_army_choose_norm)
    if choose_norm:
        touch(choose_norm)
        
    sleep(sleep_time)
    #   选择"队伍编队"
    touch(wait(image_formation_btn, timeout=30))
    sleep(sleep_time)


def combat_into_battle(choose_stage: str):
    """
        choose_stage:str    格式以124e为例,字符串为"12-4-e"
        难度说明:   n:普通   e:困难   m:夜间
    """
    #   检查当前是否为战役选择界面
    wait(image_combat_mission, timeout=120, interval=1, intervalfunc=any_into_combat)
    #   战役选择界面
    touch(image_combat_mission)
    sleep(2)
    #   战役选择
    difficulty, episode, stage = _analyse_choose_message(choose_stage)
    _choose_episode(episode)
    _choose_difficulty(difficulty)
    _choose_stage(stage)
    #   进入地图
    touch(image_start_special_btn)
    #   满仓处理
    if exists(image_event_bed_full):
        bed_full_clear()
        combat_into_battle(choose_stage)
    sleep(sleep_time)


def base_into_combat():
    """
        主页切至战役选择界面
        确保当前页面为主页
    """
    # 进入选择战役(主线)页面
    touch(exists(image_battle_btn))

def back_base():
    """
        返回主页
    """
    is_menu_on = exists(image_menu_on)
    is_menu_off = exists(image_menu_off)
    back_btn = (30,30)

    # 存在该按钮,当前已在主页
    if exists(image_battle_btn):
        return

    if is_menu_off:
        touch(is_menu_off)
        touch(image_menu_return_base)
    elif is_menu_on:
        touch(image_menu_return_base)
    else:
        touch(back_btn)
        back_base()

def any_into_combat():
    """
        any_into_***:用于适应各个页面跳转
        内容使用back_base跳回主页,在进行主页向各页面的跳转
    """
    back_base()
    sleep(sleep_time)
    base_into_combat()


def _choose_difficulty(difficulty: str):
    """
        选择难度
    """
    if difficulty == "n":
        while (not exists(image_difficulty_n)):
            touch((837, 208))
    elif difficulty == "e":
        while (not exists(image_difficulty_e)):
            touch((837, 208))
    elif difficulty == "m":
        # while (not exists(image_difficulty_m)):
        #     touch((837, 208))
        print("夜战图片未收集")

def _choose_episode(episode: str):
    """
        选择战役
    """

    if episode == "12":
        # 当前记录点判断
        if exists(image_episode_12_btn_selected):
            return
        touch(image_episode_12_btn)

def _choose_stage(stage: str):
    """
        选择关卡
    """
    if stage == "4":
        touch(image_stage_12_4_e_btn)

def _analyse_choose_message(message: str):
    """
        提取出"12-4-e"内元素
    """
    list = message.split("-")
    episode = list[0]
    stage = list[1]
    difficulty = list[2]
    return difficulty, episode, stage
