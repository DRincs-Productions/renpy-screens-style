init -1:
    define gui.dr_multiplicateur = 1
    default gui.dr_moblile_zoom = 1

    if renpy.variant("pc"):
        $ gui.dr_moblile_zoom = 1
    else:
        $ gui.dr_moblile_zoom = 1.5

# text
define gui.dr_little_text_size = 18 * gui.dr_multiplicateur
define gui.dr_normal_text_size = 24 * gui.dr_multiplicateur
define gui.dr_big_normal_text_size = 28 * gui.dr_multiplicateur
define gui.nqtr_hour_text_size = 60 * gui.dr_multiplicateur
# image
define gui.nqtr_button_action_size = 120 * gui.dr_multiplicateur
define gui.dr_small_face_size = 60 * gui.dr_multiplicateur
define gui.nqtr_button_room_size = 136 * gui.dr_multiplicateur
define gui.nqtr_button_location_size = 90 * gui.dr_multiplicateur
define gui.dr_small_menu_size = 80 * gui.dr_multiplicateur * gui.dr_moblile_zoom
define gui.nqtr_button_map_size = 50 * gui.dr_multiplicateur
define gui.dr_close_button_size = 35 * gui.dr_multiplicateur
# screens
define gui.nqtr_menu_memo_ypos = 170
define gui.nqtr_menu_memo_xpos = 80
define gui.nqtr_menu_memo_ysize = 850
define gui.nqtr_menu_memo_xsize = 400
# nqtr menu_memo
define gui.nqtr_menu_memo_image_ysize = 400 * gui.dr_multiplicateur
define gui.nqtr_menu_memo_image_xsize = 800 * gui.dr_multiplicateur
define gui.nqtr_menu_memo_frame_xsize = 1190 * gui.dr_multiplicateur
define gui.nqtr_menu_memo_frame_ysize = 400 * gui.dr_multiplicateur
# ds userinfo
define gui.ds_userinfo_textdistance_xsize = 250
