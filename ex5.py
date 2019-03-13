import random

comp1 = [2 for i in range(1, 20)]
print("List chua N so 2", comp1)

copm2 = [value for value in range(1, 100) if ( value % 3 == 0) or (value % 5 == 0)]
print("List so chia het cho 3 or 5", copm2)

comp3 = [6 * str(value) for value in range(1, 21, 2)]
print("List dang so le lap 6 lan", comp3)

comp4 = [random.randrange(100) for _ in range(0, 20)]
print("List chua N so nguyen ngau nhien", comp4)

'''List chua N so 2 [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
List so chia het cho 3 or 5 [3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24, 25, 27, 30, 33, 35, 36, 39, 40, 42, 45, 48, 50, 51, 54, 55, 57, 60, 63, 65, 66, 69, 70, 72, 75, 78, 80, 81, 84, 85, 87, 90, 93, 95, 96, 99]
List dang so le lap 6 lan ['111111', '333333', '555555', '777777', '999999', '111111111111', '131313131313', '151515151515', '171717171717', '191919191919']
List chua N so nguyen ngau nhien [11, 31, 12, 81, 13, 69, 48, 39, 77, 52, 47, 33, 74, 56, 84, 83, 51, 49, 10, 35] '''