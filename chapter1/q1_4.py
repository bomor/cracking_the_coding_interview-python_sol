import pytest


def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)


# OR
def are_anagrams2(s1, s2):
    if len(s1) != len(s2):
        return False
    ch_counter = [0] * 256
    for ch in s1:
        ch_counter[ord(ch)] += 1
    for ch in s2:
        if ch_counter[ord(ch)] == 0:
            return False
        ch_counter[ord(ch)] -= 1
    return all(v == 0 for v in ch_counter)


# Tests

@pytest.mark.parametrize("impl", [are_anagrams, are_anagrams2])
def test_are_anagrams(impl):
    assert impl("abcd", "badc")
    assert not impl("aaab", "aab")
    assert not impl("AaBb", "aabb")
