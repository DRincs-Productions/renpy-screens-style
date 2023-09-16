define dr_multiplicateur = 2
default dr_moblile_zoom = 1

init:
    if renpy.variant("pc"):
        $ dr_moblile_zoom = 1
    else:
        $ dr_moblile_zoom = 1.5

# text
define gui.little_text_size = 18 * dr_multiplicateur
define gui.normal_text_size = 24 * dr_multiplicateur
define gui.big_normal_text_size = 28 * dr_multiplicateur
define gui.hour_text_size = 60 * dr_multiplicateur
# image
define gui.middle_action_size = 120 * dr_multiplicateur
define gui.small_face_size = 60 * dr_multiplicateur
define gui.middle_room_size = 136 * dr_multiplicateur
define gui.small_map_size = 90 * dr_multiplicateur
define gui.small_menu_size = 80 * dr_multiplicateur * dr_moblile_zoom
define gui.middle_map_size = 50 * dr_multiplicateur
define gui.dr_close_button_size = 35 * dr_multiplicateur
# nqtr menu_memo
define gui.nqtr_menu_memo_image_ysize = 400 * dr_multiplicateur
define gui.nqtr_menu_memo_image_xsize = 800 * dr_multiplicateur
define gui.nqtr_menu_memo_frame_xsize = 1190 * dr_multiplicateur
define gui.nqtr_menu_memo_frame_ysize = 400 * dr_multiplicateur
define gui.nqtr_menu_memo_ypos = 170 * dr_multiplicateur
define gui.nqtr_menu_memo_xpos = 80 * dr_multiplicateur
define gui.nqtr_menu_memo_ysize = 850 * dr_multiplicateur
define gui.nqtr_menu_memo_xsize = 400 * dr_multiplicateur
