
def xtime(a: int) -> int:
    a &= 0xFF
    return (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else ((a << 1) & 0xFF)

def mix_single_column(col):
    t = col[0] ^ col[1] ^ col[2] ^ col[3]
    u = col[0]
    col[0] ^= t ^ xtime(col[0] ^ col[1])
    col[1] ^= t ^ xtime(col[1] ^ col[2])
    col[2] ^= t ^ xtime(col[2] ^ col[3])
    col[3] ^= t ^ xtime(col[3] ^ u)

def mix_columns(state):
    for col in state:
        mix_single_column(col)

def inv_mix_columns(state):
    for col in state:
        u = xtime(xtime(col[0] ^ col[2]))
        v = xtime(xtime(col[1] ^ col[3]))
        col[0] ^= u
        col[1] ^= v
        col[2] ^= u
        col[3] ^= v
    mix_columns(state)

def inv_shift_rows(state):
    # rotate row 1 right by 1
    state[0][1], state[1][1], state[2][1], state[3][1] = state[3][1], state[0][1], state[1][1], state[2][1]
    # rotate row 2 right by 2
    state[0][2], state[1][2], state[2][2], state[3][2] = state[2][2], state[3][2], state[0][2], state[1][2]
    # rotate row 3 right by 3 (left by 1)
    state[0][3], state[1][3], state[2][3], state[3][3] = state[1][3], state[2][3], state[3][3], state[0][3]

def matrix_to_bytes(state) -> bytes:
    # state is column-major
    return bytes(b for col in state for b in col)

def main():
    state = [
        [108, 106, 71, 86],
        [96, 62, 38, 72],
        [42, 184, 92, 209],
        [94, 79, 8, 54],
    ]

    inv_mix_columns(state)
    inv_shift_rows(state)

    flag_bytes = matrix_to_bytes(state)
    print(flag_bytes)                 # raw bytes
    print(flag_bytes.decode())        # as text

if __name__ == "__main__":
    main()
