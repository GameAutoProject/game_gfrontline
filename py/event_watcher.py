
from airtest.core.api import *

from image_source import *

def bed_full_event_watcher():
    event_page_point = exists(image_event_bed_full)
    
