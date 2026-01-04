def decrypt(key, ciphertext):
    round_keys = expand_key(key)  # round_keys[0..10]

    # 1) ciphertext -> state
    state = bytes2matrix(ciphertext)

    # 2) initial AddRoundKey with last round key
    add_round_key(state, round_keys[N_ROUNDS])

    # 3) rounds 9..1
    for r in range(N_ROUNDS - 1, 0, -1):
        inv_shift_rows(state)
        sub_bytes(state, inv_s_box)
        add_round_key(state, round_keys[r])
        inv_mix_columns(state)

    # 4) final round (round 0), no inv_mix_columns
    inv_shift_rows(state)
    sub_bytes(state, inv_s_box)
    add_round_key(state, round_keys[0])

    # 5) state -> plaintext bytes
    return matrix2bytes(state)

