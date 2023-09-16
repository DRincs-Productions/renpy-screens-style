style menu_vscroll is vscrollbar:
    xsize 7
    unscrollable 'hide'

init:
    transform middle_room:
        size (gui.middle_room_size, gui.middle_room_size)
        on selected_idle:
            yanchor 0 alpha 0.9 matrixcolor BrightnessMatrix(-0.3)
        on idle:
            yanchor 0 alpha 0.9 matrixcolor BrightnessMatrix(0)
        on hover:
            yanchor 1 alpha 0.9 matrixcolor BrightnessMatrix(0.1)
        on selected_hover:
            yanchor 1 alpha 0.9 matrixcolor BrightnessMatrix(-0.5)
        on insensitive:
            yanchor 0 alpha 0.9 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 alpha 0.9 matrixcolor BrightnessMatrix(-0.5)
    transform small_map:
        size (gui.small_map_size, gui.small_map_size)
        on selected_idle:
            yanchor 0 matrixcolor BrightnessMatrix(-0.3)
        on idle:
            yanchor 0 matrixcolor BrightnessMatrix(0)
        on hover:
            yanchor 1 matrixcolor BrightnessMatrix(0.1)
        on selected_hover:
            yanchor 1 matrixcolor BrightnessMatrix(-0.5)
        on insensitive:
            yanchor 0 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
    transform middle_action:
        size (gui.middle_action_size, gui.middle_action_size)
        on selected_idle:
            yanchor 0 alpha 0.7
        on idle:
            yanchor 0 alpha 0.7
        on hover:
            yanchor 1 alpha 1.0
        on selected_hover:
            yanchor 1 alpha 1.0
        on insensitive:
            yanchor 0 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
    transform middle_action_is_in_room:
        on selected_idle:
            yanchor 0 matrixcolor BrightnessMatrix(-0.3)
        on idle:
            yanchor 0 matrixcolor BrightnessMatrix(0)
        on hover:
            yanchor 0 matrixcolor BrightnessMatrix(0.1)
        on selected_hover:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
        on insensitive:
            yanchor 0 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
    transform small_face:
        size (gui.small_face_size, gui.small_face_size)
        on selected_idle:
            yanchor 0 alpha 1.0
        on idle:
            yanchor 0 alpha 1.0
        on hover:
            yanchor 1 alpha 0.93
        on selected_hover:
            yanchor 1 alpha 0.93
        on insensitive:
            yanchor 0 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
    transform small_menu:
        size (gui.small_menu_size, gui.small_menu_size)
        on selected_idle:
            yanchor 0 alpha 0.4
        on idle:
            yanchor 0 alpha 0.4
        on hover:
            yanchor 1 alpha 1.0
        on selected_hover:
            yanchor 1 alpha 1.0
        on insensitive:
            yanchor 0 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
    transform close_zoom:
        xanchor 25
        size (75, 25)
        on idle:
            yanchor 0 matrixcolor BrightnessMatrix(0)
        on hover:
            yanchor 0 matrixcolor BrightnessMatrix(0.9)
    transform close_zoom_mobile:
        xanchor 35
        size (105, 35)
        on idle:
            yanchor 0 matrixcolor BrightnessMatrix(0)
        on hover:
            yanchor 0 matrixcolor BrightnessMatrix(0.9)
    transform middle_map(rotation = 0):
        rotate rotation
        xysize (gui.middle_map_size, gui.middle_map_size)
        on selected_idle:
            yanchor 0 alpha 0.6
        on idle:
            yanchor 0 alpha 0.6
        on hover:
            yanchor 1 alpha 1.0
        on selected_hover:
            yanchor 1 alpha 1.0
        on insensitive:
            yanchor 0 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
    transform next_button_tran(rotation = 0):
        rotate rotation
        on idle:
            alpha 0.6 matrixcolor BrightnessMatrix(0)
        on hover:
            alpha 1.0 matrixcolor BrightnessMatrix(0.2)
        on insensitive:
            alpha 0.6 matrixcolor BrightnessMatrix(-0.5)
