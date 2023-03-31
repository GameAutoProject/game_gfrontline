# -*- encoding=utf8 -*-
__author__ = "10267"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

from page_switch_action import *
from battle_model import *

# 62026 笔电
# 62027 台式
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
               "android://127.0.0.1:5037/127.0.0.1:62027?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=MINITOUCH",], project_root="D:/code_space/game_test/game_gfrontline")

# script content
print("start...")


back_base()

battel_time = 20 #10
battel_stage = "12-4-e"

model_circle_battle(battel_time,battel_stage)
