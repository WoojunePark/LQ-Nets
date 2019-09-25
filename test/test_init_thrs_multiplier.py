# initialize threshold multiplier
init_thrs_multiplier = []
for i in range(1, num_levels):
    thrs_multiplier_i = [0. for j in range(num_levels)]
    thrs_multiplier_i[i - 1] = 0.5
    thrs_multiplier_i[i] = 0.5
    init_thrs_multiplier.append(thrs_multiplier_i)