def rotate_90(m):
    m_size = len(m)
    for layer in xrange(m_size / 2):
        for i in xrange(m_size - (2 * layer) - 1):
            tmp = m[layer][layer + i]
            m[layer][layer + i] = m[m_size - 1 - layer - i][layer]
            m[m_size - 1 - layer - i][layer] = m[m_size - 1 - layer][m_size - 1 - layer - i]
            m[m_size - 1 - layer][m_size - 1 - layer - i] = m[layer + i][m_size - 1 - layer]
            m[layer + i][m_size - 1 - layer] = tmp


# Tests

def test_rotate_90():
    m = matrix_4x4()
    rotate_90(m)
    n = [[0]]
    rotate_90(n)
    assert m == rotated_90_matrix_4x4()
    assert n == [[0]]
    rotate_90(m)
    rotate_90(m)
    rotate_90(m)
    assert matrix_4x4() == m


def matrix_4x4():
    return [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]


def rotated_90_matrix_4x4():
    return [[13, 9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4]]
