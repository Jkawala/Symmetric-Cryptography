def sub_bytes(s, sbox=s_box):
    return [[sbox[byte] for byte in row] for row in s]
print(sub_bytes(state, sbox=inv_s_box))
