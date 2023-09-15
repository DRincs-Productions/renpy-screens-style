screen menu_tile(title):

    frame:
        area (150, 70, 350, 50)
        background None
        text title:
            color gui.accent_color
            size gui.name_text_size

screen close_button(screen_name):

    # button for closure
    imagebutton:
        align (0.95, 0.05)
        idle '/screens_style/images/close_idle.webp'
        action [
            Hide(screen_name),
        ]
        if renpy.variant("pc"):
            focus_mask True
            at close_zoom
        else:
            at close_zoom_mobile

screen next_button(action_value, sensitive, align_value, rotation = 0):
    imagebutton align align_value:
        idle '/nqtr_interface/button/next_idle.webp'
        hover '/nqtr_interface/button/next_hover.webp'
        insensitive '/nqtr_interface/button/next_insensitive.webp'
        focus_mask True
        sensitive sensitive
        action action_value
        at next_button_tran(rotation)