# 1.1 we assume that lowercase<ch> is the same char as uppercase<ch>. If not - <.lower> can be deleted
import pytest
def has_all_unique_chars(my_str):
    return len(my_str.lower()) == len(set(my_str.lower()))

# OR (if an additional data structure can be used)

def has_all_unique_chars2(my_str):
    ch_list = sorted(my_str.lower())
    for i in xrange(len(ch_list) - 1):
        if ch_list[i] == ch_list[i + 1]:
            return False
    return True
	
# OR (If string contains only letters, and lowercase<ch> is the same char as uppercase<ch>)

def has_all_unique_chars3(my_str):
    is_char_showed = [False] * 25
    for ch in my_str.lower():
        if is_char_showed[ord(ch) - 97]:
            return False
        is_char_showed[ord(ch) - 97] = True
    return True

# OR

def has_all_unique_chars4(my_str):
    lower_str = my_str.lower()
    for i in xrange(len(lower_str) - 1):
        for j in xrange(i + 1, len(lower_str)):
            if lower_str[i] == lower_str[j]:
                return False
    return True
	
############## Tests ##############

@pytest.mark.parametrize("impl", [has_all_unique_chars, has_all_unique_chars2, has_all_unique_chars3, has_all_unique_chars4])
def test_has_all_unique_chars(impl):
	assert not impl("ababab")
	assert impl("abcd")
	assert impl("")
	assert not impl("aaaaa")
	assert not impl("AaBbCc")