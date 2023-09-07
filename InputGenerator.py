import random

def  build_random_input(sample_number, file_in):
    nodes = 1
    nodes = (sample_number + 1) * 5
    file_in.write(str(nodes) + ' ')
    k = str(random.randint(0, (nodes * nodes) - nodes))
    file_in.write(k + ' ')
    file_in.write(str(random.randint(0, nodes - 1)) + ' ')
    file_in.write(str(random.randint(0, nodes - 1)) + ' ')
    file_in.write(str(random.randint(0, nodes - 1)) + ' ')
    file_in.write(str(random.randint(0, nodes - 1)) + ' ')
    file_in.write('\n')
    sum = 0
    for i in range(nodes):
        row = ""
        for j in range(nodes):
            edge = str(random.randint(0, 1))
            if(edge == '1'):
                sum += 1
            if(sum >= ((nodes * nodes) - nodes) - int(k) or i == j):
                edge = '0'
            row += edge 
            row += " "
        if(i != (nodes - 1)):
            row += "\n"
        file_in.write(row)
    file_in.close()

for i in range(40):
    file_now = open(f'Inputs/inputs{i}.txt', 'w')
    build_random_input(i, file_now)