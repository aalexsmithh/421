from pimento import menu


def boolean_menu(prompt):
    post_prompt = prompt + " [{}] "

    result = menu(
        ["yes", "no"],
        pre_prompt="Options:",
        post_prompt=post_prompt,
        default_index=1,
        insensitive=True,
        fuzzy=True)

    if result == "yes":
        return True
    elif result == "no":
        return False
    else:
        raise Exception("This should not happen!")
