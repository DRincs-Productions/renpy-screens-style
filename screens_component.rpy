define dr_current_next_value = 0

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
        idle 'gui close_button'
        action [
            Hide(screen_name),
        ]
        if renpy.variant("pc"):
            focus_mask True
        at dr_close_button_transform
