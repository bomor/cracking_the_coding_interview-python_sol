# 1.1

def has_all_unique_chars(my_str):
    return len(my_str) == len(set(my_str))

# OR (if an additional data structure can be used)

def has_all_unique_chars2(my_str):
    ch_list = sorted(my_str.lower())
    for i in xrange(len(ch_list) - 1):
        if ch_list[i] == ch_list[i + 1]:
            return False
    return True

# OR (if string contains only letters)

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

##############################################################

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

##############################################################

# 1.4

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

##############################################################

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

##############################################################

# 1.6
def rotate_90(m):
    m_size = len(m)
    for layer in xrange(m_size / 2):
        for i in xrange(m_size - (2 * layer) - 1):
            tmp = m[layer][layer + i]
            m[layer][layer + i] = m[m_size - 1 - layer - i][layer]
            m[m_size - 1 - layer - i][layer] = m[m_size - 1 - layer][m_size - 1 - layer - i]
            m[m_size - 1 - layer][m_size - 1 - layer - i] = m[layer + i][m_size - 1 - layer]
            m[layer + i][m_size - 1 - layer] = tmp

##############################################################

# 1.7

def set_zero(m):
    zero_rows = set()
    zero_cols = set()
    m_rows = len(m)
    m_cols = len(m[0])
    for r in xrange(m_rows):
        for c in xrange(m_cols):
            if m[r][c] == 0:
                zero_rows.add(r)
                zero_cols.add(c)
    # instead of running all the matrix
    for r in zero_rows:
        for c in xrange(m_cols):
            m[r][c] = 0
    for c in zero_cols:
        for r in xrange(m_rows):
            m[r][c] = 0
    print m

##############################################################

# 1.8 (A method called "is_substring" is given)

def is_rotation(s1, s2):
    if len(s1) == len(s2):
        con_s2 = s2 + s2
        return is_substring(s1, con_s2)
    return False
