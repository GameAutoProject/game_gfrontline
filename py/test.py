# from airtest.core.api import *
# from airtest.cli.parser import cli_setup

# from image_source import *

# 62026 笔电
# 62027 台式
# if not cli_setup():
#     auto_setup(__file__, logdir=True, devices=[
#                "android://127.0.0.1:5037/127.0.0.1:62027?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=MINITOUCH",], project_root="D:/code_space/game_test/game_gfrontline")

# print("************",exists(image_army_choose_norm))
# point = exists(image_army_choose_norm)
# touch((point[0]+20,point[1]))

# dY = -469.5
# Y = -0.6
# swipe((800,450), vector=(0,Y))
# sleep(3)
# swipe((800,450), vector=(0,-Y))

# img_test = Template('../image/battle_map/12-4-e_map.png')
# point:tuple = exists(img_test)   # (948, 493)

# # home1 (855,867)  home2 (740,98)
# #       (-93,+374)       (-208,-395)
# # path (1066,430) (1287,431)
# #      (+118,-63) (+339,-62)

# X=point[0]
# Y=point[1]

# # touch((X-93,Y+374))
# # touch((X-208,Y-395))
# touch((X+118,Y-63))
# sleep(1)
# touch((X+339,Y-62))

import main_exec

main_exec.script(battel_stage='12-4-e', battel_times=2)
