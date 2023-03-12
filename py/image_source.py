from airtest.core.api import Template

# source
# image url
image_url = r"./image"

# main button
image_battle_btn = Template(image_url+"/page/home/battle_action.png",
                            record_pos=(0.228, 0.049), resolution=(1600, 900))

episode_threshold = 0.8

# episode   识别阈值threshold=0.9
image_episode_12_btn = Template(
    image_url+"/page/combat/episode/episode_12.png", threshold=episode_threshold, rgb=True)

# episode_selected
image_episode_12_btn_selected = Template(
    image_url+"/page/combat/episode/episode_12_selected.png", threshold=episode_threshold, rgb=True)

# episode -> stage
image_stage_12_4_e_btn = Template(
    image_url+"/page/combat/stage/stage_12_4e.png", record_pos=(0.121, 0.227), resolution=(1600, 900))

# stage difficult
image_difficulty_n = Template(image_url+"/page/combat/difficulty/difficulty_normal.png",
                              rgb=True, record_pos=(0.288, -0.182), resolution=(1600, 900))
image_difficulty_e = Template(image_url+"/page/combat/difficulty/difficulty_emergency.png",
                              rgb=True, record_pos=(0.288, -0.182), resolution=(1600, 900))

# combat menu
image_combat_mission = Template(
    image_url+"/page/combat/menu/combat_mission.png", threshold=0.7)
image_combat_campaign = Template(
    image_url+"/page/combat/menu/combat_campaign.png")
image_combat_simulation = Template(
    image_url+"/page/combat/menu/combat_simulation.png")


image_army_choose_norm = Template(image_url+"/page/diagram/army_select/army_choose.png", target_pos=6)

image_start_special_btn = Template(
    image_url+"/page/combat/battle_setting/start_special.png")


image_plan_off_btn = Template(
    image_url+"/page/diagram/general/planning_mode_off.png", rgb=True)
image_execute_plan = Template(
    image_url+"/page/diagram/general/execute_plan.png")

image_echelon_1 = Template(
    image_url+"/page/diagram/army_select/echelon_choose.png", target_pos=2)

image_certain = Template(image_url+"/page/diagram/army_select/certain.png")

image_formation_btn = Template(image_url+"/page/diagram/army_select/formation_btn.png")


image_124e_map = Template(image_url+"/battle_map/12-4-e_map.png", rgb=True)

image_supply_btn = Template(
    image_url+"/page/diagram/army_select/supply_btn.png")
"""补给按钮"""

image_start_battle_btn = Template(
    image_url+"/page/diagram/general/start_battle.png")
"""开始作战按钮"""


# event
image_event_bed_full = Template(image_url+"/event/bed_full.png")

# top menu
image_menu_on = Template(image_url+"/page/top_menu/menu_on.png", rgb=True)
image_menu_off = Template(image_url+"/page/top_menu/menu_off.png")
image_menu_return_base = Template(image_url+"/page/top_menu/return_base.png")


image_dolls = {
    "hk416": {
        Template(image_url+"/entity/doll/hk416/1.png"),
        Template(image_url+"/entity/doll/hk416/2.png"),
    },
    "k11": {
        Template(image_url+"/entity/doll/k11/1.png"),
    }
}
"""人形池"""

# general image
image_general_certain = Template(image_url+"/general/image_general_certain.png")
