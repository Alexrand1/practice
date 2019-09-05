def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    b = merge_sort(arr[:len(arr)//2])
    c = merge_sort(arr[len(arr) // 2:])
    return merge(b, c)


def merge(b, c):
    d = []
    i = 0
    j = 0
    k = 0
    while k < (len(c) + len(b))-1:
        if b[i] < c[j]:
            d.append(b[i])
            i += 1
            if i > len(b)-1:
                break
        elif b[i] > c[j]:
            d.append(c[j])
            j += 1
            if j > len(c)-1:
                break
        k += 1
    while i < len(b):
        d.append(b[i])
        i += 1
    while j < len(c):
        d.append(c[j])
        j += 1
    return d


arr = [9962, 1058, 598, 6541, 7164, 2012, 175, 2745, 2633, 9346, 3415, 7363, 7163, 9573, 9990, 7443, 1043, 6806, 1557, 3675, 7520, 4758, 8631, 8532, 6242, 5195, 8563, 5504, 7093, 5542, 5452, 6729, 4791, 6015, 8039, 2951, 6141, 7878, 1157, 3249, 259, 4436, 9078, 1085, 7362, 3323, 6645, 8270, 7626, 8141, 5959, 9465, 8385, 3684, 6185, 2618, 6522, 2643, 6787, 481, 7516, 7412, 3514, 1430, 1723, 8382, 3421, 1616, 1808, 5843, 939, 6638, 9236, 1617, 5821, 52, 8142, 5439, 2146, 5501, 2800, 5065, 8682, 7540, 4268, 1870, 1197, 3582, 1383, 5889, 6349, 8497, 8898, 246, 2131, 6360, 3856, 1554, 5510, 6031, 1953, 9736, 8513, 4777, 6716, 4106, 7502, 4443, 3518, 181, 8235, 9959, 5210, 9599, 8156, 5001, 9399, 453, 1790, 9502, 9131, 7751, 4330, 7491, 7655, 7334, 6329, 1275, 7335, 636, 4975, 8031, 866, 9247, 5351, 2615, 7364, 1056, 4539, 1343, 303, 2785, 4829, 442, 410, 825, 3186, 1553, 8853, 5265, 5108, 5844, 9639, 5600, 3070, 1858, 1821, 8185, 9922, 5627, 8451, 3949, 287, 5848, 9907, 4882, 7602, 8450, 8295, 371, 637, 7900, 8949, 9350, 8201, 6413, 9754, 6765, 1171, 5651, 3405, 7446, 9161, 4331, 1331, 3810, 9525, 8442, 6855, 7710, 521, 318, 651, 1777, 434, 8331, 9583, 7941, 5490, 2751, 3236, 645, 9774, 4734, 5111, 7531, 6582, 7224, 1202, 8689, 3602, 2206, 4989, 9246, 5904, 8271, 6194, 9766, 8129, 4118, 3803, 2141, 4921, 9712, 7783, 2359, 4040, 6321, 8445, 9793, 2780, 9074, 6900, 2133, 6003, 4490, 6793, 5601, 4341, 1227, 5084, 9197, 2440, 6220, 8249, 1789, 3234, 2366, 6944, 3585, 9541, 4111, 2254, 2851, 4697, 6667, 2570, 4378, 8737, 9861, 134, 8692, 8838, 3423, 991, 8279, 5667, 1468, 7823, 2768, 4475, 3451, 6434, 8272, 4899, 2572, 5172, 9284, 7330, 1184, 2255, 8029, 1511, 17, 1347, 1431, 1630, 4666, 4160, 8327, 9852, 1916, 4197, 7242, 4076, 4797, 679, 9690, 8993, 7059, 5004, 8840, 440, 2433, 270, 9092, 1437, 255, 4708, 7763, 8115, 1126, 8849, 4558, 6497, 9596, 491, 1588, 9702, 7485, 8980, 3092, 2232, 9821, 5474, 1634, 9225, 1090, 5924, 7410, 8398, 2369, 9961, 4061, 9258, 2891, 2194, 3326, 5216, 2176, 9282, 2510, 3308, 8547, 1226, 1955, 9283, 3090, 1523, 1088, 4474, 1883, 9096, 1773, 3376, 5717, 4370, 6714, 4210, 2846, 2069, 7023, 6803, 5462, 9848, 6285, 1861, 1180, 2878, 6542, 5757, 7733, 9139, 755, 1747, 6290, 6288, 5313, 9151, 1322, 3317, 5696, 4982, 1578, 2052, 9921, 9176, 3311, 3556, 9785, 3226, 5126, 5657, 7374, 9182, 5370, 1901, 6763, 8986, 4328, 1833, 9205, 8551, 8257, 8412, 7231, 6034, 9186, 5074, 5232, 2207, 7492, 7295, 6236, 758, 7985, 2563, 2379, 9238, 2662, 4228, 9661, 4885, 5948, 2985, 44, 5189, 8457, 6301, 989, 4211, 7904, 9010, 7382, 2110, 282, 6520, 9228, 8996, 152, 906, 1768, 7871, 8926, 5399, 2980, 8126, 4314, 9268, 6819, 6833, 1130, 4663, 4427, 59, 1643, 2517, 2084, 1326, 447, 6439, 1051, 6537, 2663, 753, 6010, 2017, 3060, 5970, 5142, 1352, 7098, 6102, 4075, 2090, 9242, 5935, 2008, 428, 4968, 6134, 230, 3751, 6789, 9805, 9995, 6883, 3606, 7014, 1133, 8320, 347, 467, 8939, 5686, 8645, 8678, 6746, 3669, 9442, 9088, 8136, 4879, 8881, 3958, 5622, 9114, 3522, 5854, 7609, 4420, 7768, 2363, 5098, 4294, 1969, 7171, 9905, 1872, 2331, 1141, 5534, 2961, 6259, 2391, 8315, 8166, 9594, 6925, 11, 2063, 1071, 3987, 2625, 9086, 102, 7925, 2718, 9667, 5048, 748, 9093, 196, 3616, 6614, 1985, 6559, 8524, 6117, 2087, 2022, 1119, 5146, 2925, 9491, 4567, 2155, 7087, 1709, 7133, 652, 7336, 2107, 5580, 4349, 7143, 3715, 4845, 3505, 7203, 6314, 5766, 770, 9424, 6757, 9529, 197, 7116, 9626, 5795, 8859, 5842, 8103, 3463, 9613, 6118, 9869, 5049, 6409, 6797, 8317, 4067, 9749, 9275, 5290, 95, 4223, 4834, 9479, 2365, 3387, 1581, 9486, 475, 7153, 1489, 8150, 4212, 3623, 1003, 9744, 5985, 1415, 2264, 5349, 8118, 7825, 6893, 6017, 356, 4525, 7037, 9609, 30, 8927, 9998, 9772, 4686, 3512, 7214, 1802, 5981, 165, 815, 759, 6309, 6186, 1495, 2971, 4725, 5772, 1398, 3298, 6200, 443, 7930, 8054, 796, 5283, 4440, 1006, 8897, 5840, 8865, 1770, 7879, 2921, 784, 7016, 5335, 5876, 8808, 7255, 4726, 3373, 2034, 4960, 5359, 7966, 5813, 1546, 7939, 1598, 4290, 3436, 9691, 4408, 7750, 3242, 8569, 525, 4094, 5251, 5665, 7139, 8666, 8902, 8747, 4633, 4208, 1149, 6283, 8528, 942, 6024, 9002, 739, 5396, 4554, 801, 885, 5271, 8843, 1448, 9794, 4688, 9591, 9940, 8158, 7200, 436, 4987, 1693, 5076, 592, 4723, 8008, 7929, 2859, 179, 2620, 3412, 412, 5023, 8447, 8036, 3864, 4409, 115, 5028, 4804, 3211, 5318, 7132, 6116, 8674, 4181, 3839, 4215, 3959, 3355, 1389, 4012, 1286, 9938, 6929, 2338, 7799, 7507, 8421, 8895, 725, 1174, 1792, 927, 426, 7686, 8240, 4511, 9732, 4999, 2939, 8656, 7687, 6889, 886, 2756, 1748, 1232, 432, 40, 1933, 6901, 9251, 5479, 4966, 9761, 6997, 7898, 58, 9250, 5885, 5655, 2509, 4438, 34, 3609, 9564, 9755, 5722, 8287, 3876, 7813, 8623, 8829, 1463, 3587, 406, 6231, 2316, 3741, 8586, 1577, 9819, 9836, 9784, 7653, 687, 4782, 343, 9050, 3738, 5420, 2434, 6389, 7346, 401, 6337, 6029, 9072, 1743, 9630, 6919, 7263, 6107, 8535, 2674, 6718, 1135, 6603, 7717, 824, 9815, 3152, 4861, 7201, 4098, 9560, 5658, 8887, 738, 1040, 5402, 5169, 809, 6999, 6567, 9415, 2587, 8083, 2312, 3645, 236, 338, 9458, 7169, 6904, 1004, 25, 3633, 709, 6739, 5994, 5716, 449, 7772, 3828, 2711, 5385, 9634, 3957, 8969, 4296, 6111, 683, 9757, 743, 7720, 4530, 3814, 6376, 4795, 19, 2521, 861, 5615, 2538, 1909, 5674, 9919, 8010, 1494, 6426, 6173, 1574, 6967, 3786, 763, 3492, 737, 2819, 8196, 2360, 7417, 1532, 8426, 9326, 6767, 3838, 1469, 1162, 1178, 7651, 664, 6565, 7778, 2867, 7060, 2737, 7818, 8099, 398, 3320, 7671, 4163, 6688, 6263, 2897, 3742, 9951, 6418, 953, 2419, 4587, 3178, 198, 5185, 3635, 7396, 9876, 368, 132, 1277, 8341, 9679, 1711, 7378, 4404, 2821, 3193, 7736, 931, 7454, 2378, 3968, 8209, 764, 221, 1405, 45, 3629, 6271, 9383, 8533, 9475, 2741, 8326, 2032, 8026, 4721, 304, 3594, 9183, 4915, 1456, 3085, 145, 9077, 9095, 1888, 3443, 143, 61, 6210, 4884, 3493, 4737, 823, 2213, 8268, 8439, 9030, 7964, 9272, 1942, 2871, 3550, 6163, 5128, 2900]

e = merge_sort(arr)
assert e == sorted(arr)
print(e)