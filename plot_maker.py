import os 
import matplotlib.pyplot as plt


directory_path = "./Times"
files = os.listdir(directory_path)
for file in files:
    file_now = open(directory_path + f"/{file}", 'r')
    file_content = file_now.read()
    lines = file_content.split('\n')
    now = 5   
    x_list = []
    y_list = []
    for line in lines:
        if(line == ''):
            break 
        num1, num2 = line.split(' ')
        num1 = int(num1)
        num2 = float(num2)
        x_list.append(num1)
        y_list.append(num2)

    plt.plot(x_list, y_list)
    plt.xlabel("number of nodes")
    plt.ylabel("time of execution")
    plt.title(f"plot time of execution for {file}")
    plt.savefig(f"Plots/{file}.jpg")
    plt.show()