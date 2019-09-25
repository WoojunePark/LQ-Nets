nbit = 3
bit_dims = [nbit, 1]
num_levels = 2 ** nbit

init_level_multiplier = []
for i in range(0, num_levels):
    level_multiplier_i = [0. for j in range(nbit)]
    # = [0. 0.]
    print(f"level_multiplier_i is {level_multiplier_i}")
    level_number = i
    # = 0, 1, 2, 3
    print(f'for i={i}, level_number is {level_number}.')
    for j in range(nbit):
        level_multiplier_i[j] = float(level_number % 2)
        level_number = level_number // 2
        print(f'for j={j}, level_multiplier_i[j] is {level_multiplier_i[j]}, level_number is {level_number}')
        # level_multiplier_0[0] = float(0 % 2) = 0.
        # level_multiplier_0[1] = float(0 % 2)
        # level_number = 1

        # level_multiplier_1[0] = float(1 % 2) = 1.
        # level_multiplier_1[1] = float(1 % 2)
        # level_number = 0

        # level_multiplier_2[0] = float(0 % 2) = 0.
        # level_multiplier_2[1] = float(0 % 2)
        # level_number = 0

        # level_multiplier_3[0] = float(0 % 2) = 1.
        # level_multiplier_3[1] = float(0 % 2)
        # level_number = 0
    init_level_multiplier.append(level_multiplier_i)
    print(f'current init_level_multiplier is {init_level_multiplier}')
    print("-------------------")

print(f'final init_level_multiplier is {init_level_multiplier}')

# nbit = 2
# level_multiplier_i is [0.0, 0.0]
# for i=0, level_number is 0.
# for j=0, level_multiplier_i[j] is 0.0, level_number is 0
# for j=1, level_multiplier_i[j] is 0.0, level_number is 0
# current init_level_multiplier is [[0.0, 0.0]]
# -------------------
# level_multiplier_i is [0.0, 0.0]
# for i=1, level_number is 1.
# for j=0, level_multiplier_i[j] is 1.0, level_number is 0
# for j=1, level_multiplier_i[j] is 0.0, level_number is 0
# current init_level_multiplier is [[0.0, 0.0], [1.0, 0.0]]
# -------------------
# level_multiplier_i is [0.0, 0.0]
# for i=2, level_number is 2.
# for j=0, level_multiplier_i[j] is 0.0, level_number is 1
# for j=1, level_multiplier_i[j] is 1.0, level_number is 0
# current init_level_multiplier is [[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]]
# -------------------
# level_multiplier_i is [0.0, 0.0]
# for i=3, level_number is 3.
# for j=0, level_multiplier_i[j] is 1.0, level_number is 1
# for j=1, level_multiplier_i[j] is 1.0, level_number is 0
# current init_level_multiplier is [[0.0, 0.0], [1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]
# -------------------
# final init_level_multiplier is [[0.0, 0.0], [1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]


# nbit = 3
# level_multiplier_i is [0.0, 0.0, 0.0]
# for i=0, level_number is 0.
# for j=0, level_multiplier_i[j] is 0.0, level_number is 0
# for j=1, level_multiplier_i[j] is 0.0, level_number is 0
# for j=2, level_multiplier_i[j] is 0.0, level_number is 0
# current init_level_multiplier is [[0.0, 0.0, 0.0]]
# -------------------
# level_multiplier_i is [0.0, 0.0, 0.0]
# for i=1, level_number is 1.
# for j=0, level_multiplier_i[j] is 1.0, level_number is 0
# for j=1, level_multiplier_i[j] is 0.0, level_number is 0
# for j=2, level_multiplier_i[j] is 0.0, level_number is 0
# current init_level_multiplier is [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]]
# -------------------
# level_multiplier_i is [0.0, 0.0, 0.0]
# for i=2, level_number is 2.
# for j=0, level_multiplier_i[j] is 0.0, level_number is 1
# for j=1, level_multiplier_i[j] is 1.0, level_number is 0
# for j=2, level_multiplier_i[j] is 0.0, level_number is 0
# current init_level_multiplier is [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]
# -------------------
# level_multiplier_i is [0.0, 0.0, 0.0]
# for i=3, level_number is 3.
# for j=0, level_multiplier_i[j] is 1.0, level_number is 1
# for j=1, level_multiplier_i[j] is 1.0, level_number is 0
# for j=2, level_multiplier_i[j] is 0.0, level_number is 0
# current init_level_multiplier is [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 1.0, 0.0]]
# -------------------
# level_multiplier_i is [0.0, 0.0, 0.0]
# for i=4, level_number is 4.
# for j=0, level_multiplier_i[j] is 0.0, level_number is 2
# for j=1, level_multiplier_i[j] is 0.0, level_number is 1
# for j=2, level_multiplier_i[j] is 1.0, level_number is 0
# current init_level_multiplier is [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
# -------------------
# level_multiplier_i is [0.0, 0.0, 0.0]
# for i=5, level_number is 5.
# for j=0, level_multiplier_i[j] is 1.0, level_number is 2
# for j=1, level_multiplier_i[j] is 0.0, level_number is 1
# for j=2, level_multiplier_i[j] is 1.0, level_number is 0
# current init_level_multiplier is [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 1.0]]
# -------------------
# level_multiplier_i is [0.0, 0.0, 0.0]
# for i=6, level_number is 6.
# for j=0, level_multiplier_i[j] is 0.0, level_number is 3
# for j=1, level_multiplier_i[j] is 1.0, level_number is 1
# for j=2, level_multiplier_i[j] is 1.0, level_number is 0
# current init_level_multiplier is [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 1.0], [0.0, 1.0, 1.0]]
# -------------------
# level_multiplier_i is [0.0, 0.0, 0.0]
# for i=7, level_number is 7.
# for j=0, level_multiplier_i[j] is 1.0, level_number is 3
# for j=1, level_multiplier_i[j] is 1.0, level_number is 1
# for j=2, level_multiplier_i[j] is 1.0, level_number is 0
# current init_level_multiplier is [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 1.0], [0.0, 1.0, 1.0], [1.0, 1.0, 1.0]]
# -------------------
# final init_level_multiplier is [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 1.0], [0.0, 1.0, 1.0], [1.0, 1.0, 1.0]]

# range(0, max value w/ n-bits, 1)
# ... in reverse bit order
