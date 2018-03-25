# Drawing Diamond

for i in range(5):
    ones = abs(10*(i//3) - 2*(i+1) + 1)
    zeros = int((5 - ones)/2)
    print('0'*zeros + '1'*ones + '0'*zeros)