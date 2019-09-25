nbit = 3
num_levels = 2 ** nbit

# initialize threshold multiplier
init_thrs_multiplier = []
for i in range(1, num_levels):
    thrs_multiplier_i = [0. for j in range(num_levels)]
    print(f'for i={i}, initial thrs_multiplier_i is {thrs_multiplier_i}')
    thrs_multiplier_i[i - 1] = 0.5
    print(f'for i={i}, initial thrs_multiplier_i[i-1] is {thrs_multiplier_i[i - 1]}')
    thrs_multiplier_i[i] = 0.5
    print(f'for i={i}, initial thrs_multiplier_i[i] is {thrs_multiplier_i[i]}')
    init_thrs_multiplier.append(thrs_multiplier_i)
    print(f'current init_thrs_multiplier is {init_thrs_multiplier}')
    print('----------------')

print(f'final init_thrs_multiplier is {init_thrs_multiplier}')

# C:\ProgramData\Anaconda3\python.exe D:/GitHub/LQ-Nets/test/test_init_thrs_multiplier.py
# for i=1, initial thrs_multiplier_i is [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
# for i=1, initial thrs_multiplier_i[i-1] is 0.5
# for i=1, initial thrs_multiplier_i[i] is 0.5
# current init_thrs_multiplier is [[0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
# ----------------
# for i=2, initial thrs_multiplier_i is [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
# for i=2, initial thrs_multiplier_i[i-1] is 0.5
# for i=2, initial thrs_multiplier_i[i] is 0.5
# current init_thrs_multiplier is [[0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0]]
# ----------------
# for i=3, initial thrs_multiplier_i is [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
# for i=3, initial thrs_multiplier_i[i-1] is 0.5
# for i=3, initial thrs_multiplier_i[i] is 0.5
# current init_thrs_multiplier is [[0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0]]
# ----------------
# for i=4, initial thrs_multiplier_i is [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
# for i=4, initial thrs_multiplier_i[i-1] is 0.5
# for i=4, initial thrs_multiplier_i[i] is 0.5
# current init_thrs_multiplier is [[0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0]]
# ----------------
# for i=5, initial thrs_multiplier_i is [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
# for i=5, initial thrs_multiplier_i[i-1] is 0.5
# for i=5, initial thrs_multiplier_i[i] is 0.5
# current init_thrs_multiplier is [[0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0]]
# ----------------
# for i=6, initial thrs_multiplier_i is [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
# for i=6, initial thrs_multiplier_i[i-1] is 0.5
# for i=6, initial thrs_multiplier_i[i] is 0.5
# current init_thrs_multiplier is [[0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.0]]
# ----------------
# for i=7, initial thrs_multiplier_i is [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
# for i=7, initial thrs_multiplier_i[i-1] is 0.5
# for i=7, initial thrs_multiplier_i[i] is 0.5
# current init_thrs_multiplier is [[0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.5]]
# ----------------
# final init_thrs_multiplier is [[0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.5]]
#
# Process finished with exit code 0