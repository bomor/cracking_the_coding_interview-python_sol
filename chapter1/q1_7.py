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


# Tests

def test_set_zero():
    m = matrix_before_set()
    set_zero(m)
    assert m == matrix_after_set()


def matrix_before_set():
    return [[0, 1, 2, 3],
            [4, 5, 6, 0],
            [8, 9, 10, 11],
            [12, 13, 14, 15]]


def matrix_after_set():
    return [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 9, 10, 0],
            [0, 13, 14, 0]]
