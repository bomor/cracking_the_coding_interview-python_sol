import pytest


# 1.5 (The easiest way would be to use a built in str func)
def replace_spaces(s):
    return s.replace(" ", "%20")


# OR
def replace_spaces2(s):
    ch_list = list(s)
    spaces_counter = 0
    for ch in ch_list:
        if ch == " ":
            spaces_counter += 1
    old_len = len(ch_list)
    ch_list.extend([""] * (spaces_counter * 2))
    next_new_index = len(ch_list) - 1
    for ch in ch_list[old_len - 1::-1]:
        if ch == " ":
            ch_list[next_new_index] = "0"
            ch_list[next_new_index - 1] = "2"
            ch_list[next_new_index - 2] = "%"
            next_new_index -= 3
        else:
            ch_list[next_new_index] = ch
            next_new_index -= 1
    return "".join(ch_list)


# Tests

@pytest.mark.parametrize("impl", [replace_spaces, replace_spaces2])
def test_replace_spaces(impl):
    assert impl("s for test ") == "s%20for%20test%20"
    assert impl("no_spaces") == "no_spaces"
