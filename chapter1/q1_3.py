import pytest
# 1.3
# (That way, we assume that lowercase<ch> != uppercase<ch>. Note that we get str, so that way we use an extra array)
def remove_dup_chars(my_str):
    if not my_str:
        return ""
    ch_list = list(my_str)
    for i in xrange(len(ch_list) - 1, 0, -1):
        if ch_list.count(ch_list[i]) > 1:
            ch_list.pop(i)
    return "".join(ch_list)


# OR
# (That way, we assume that lowercase<ch> != uppercase<ch>. No need for an additional buffer)
def remove_dup_chars2(my_str):
    if not my_str:
        return ""
    for i in xrange(len(my_str) - 1, 0, -1):
        if my_str.count(my_str[i]) > 1:
            my_str = my_str[:i] + my_str[i + 1:]
    return my_str

############## Tests ##############

@pytest.mark.parametrize("impl", [remove_dup_chars, remove_dup_chars2])
def test_remove_dup_chars(impl):
	assert impl("AaBbCc") == "AaBbCc"
	assert impl("aaabbbccc") == "abc"
	assert impl(None) == ""