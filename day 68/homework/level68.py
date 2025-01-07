def text_input():
    entered_texts = set()
    while True:
        user_input = input()
        if user_input in entered_texts:
            break
