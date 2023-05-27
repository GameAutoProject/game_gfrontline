from airtest.core.api import *

from image_source import *

import tools

def bed_full_clear():
    touch(image_event_bed_full)
    touch(image_factory_doll_return)
    sleep(2)
    doll_choose_low()
    touch((1420,755))
    sleep(2)
    doll_choose_high()
    touch((1420,755))
    sleep(1)
    touch((960,780))
    # wait(image_factory_certain, timeout=120)
    sleep(2)

def doll_choose_low():
    """低星清除"""
    touch((370,270))
    sleep(1)
    touch((1480,820))
    sleep(1)
    touch((1480,820))
    sleep(1)

def doll_choose_high():
    """高星清除(暂且清理3.4.5星)"""
    touch((370,270))
    sleep(1)
    list=tools.dolls_filter([3,4,5])
    tools.point_step_processor(list)
    sleep(1)
    # 单点选人
    for i in range(6):
        touch((130 + i*220,300))
    for i in range(6):
        touch((130 + i*220,670))

    sleep(1)
    touch((1480,820))
    sleep(1)
    
def supportDispath():
    point = exists(image_support_again_btn)
    if point:
        touch(point)
        sleep(1)
        touch(image_general_certain)
        sleep(2)
