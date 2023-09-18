define dr_multiplicateur = 1
default dr_moblile_zoom = 1

init:
    if renpy.variant("pc"):
        $ dr_moblile_zoom = 1
    else:
        $ dr_moblile_zoom = 1.5

# text
define gui.dr_little_text_size = 18 * dr_multiplicateur
define gui.dr_normal_text_size = 24 * dr_multiplicateur
define gui.dr_big_normal_text_size = 28 * dr_multiplicateur
define gui.nqtr_hour_text_size = 60 * dr_multiplicateur
# image
define gui.nqtr_button_action_size = 120 * dr_multiplicateur
define gui.dr_small_face_size = 60 * dr_multiplicateur
define gui.nqtr_button_room_size = 136 * dr_multiplicateur
define gui.nqtr_button_location_size = 90 * dr_multiplicateur
define gui.dr_small_menu_size = 80 * dr_multiplicateur * dr_moblile_zoom
define gui.nqtr_button_map_size = 50 * dr_multiplicateur
define gui.dr_close_button_size = 35 * dr_multiplicateur
# scrrens
define gui.nqtr_menu_memo_ypos = 170
define gui.nqtr_menu_memo_xpos = 80
define gui.nqtr_menu_memo_ysize = 850
define gui.nqtr_menu_memo_xsize = 400
# nqtr menu_memo
define gui.nqtr_menu_memo_image_ysize = 400 * dr_multiplicateur
define gui.nqtr_menu_memo_image_xsize = 800 * dr_multiplicateur
define gui.nqtr_menu_memo_frame_xsize = 1190 * dr_multiplicateur
define gui.nqtr_menu_memo_frame_ysize = 400 * dr_multiplicateur
