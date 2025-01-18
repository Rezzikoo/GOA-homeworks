def cat_and_mouse(s):
    cat_pos = s.index('C')
    mouse_pos = s.index('m')
    distance = mouse_pos - cat_pos - 1
    if distance <= 3:
        return "Caught!"
    else:
        return "Escaped!"
