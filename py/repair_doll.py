from image_source import *
from airtest.core.api import *

def doll_repair(doll_point:tuple):
    """ 
    修复人形 
    param:tuple
    输出需要维护人形的梯队位置坐标
    """
    # log(doll_point)
    # touch((990,300))
    touch(doll_point)
    sleep(1)
    # wait(image_general_certain, timeout=120)
    touch((1200,680))
