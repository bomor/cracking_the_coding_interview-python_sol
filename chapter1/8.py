# 1.8 (A method called "is_substring" is given)

def is_rotation(s1, s2):
    if len(s1) == len(s2):
        con_s2 = s2 + s2
        return is_substring(s1, con_s2)
    return False
	
def is_substring(s1, s2):
	return s1 in s2
	
############## Tests ##############

def test_is_rotation():
	assert is_rotation("apple", "pleap")
	assert not is_rotation("apple", "ppale")