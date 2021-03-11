import operator
import numpy as np
from openpyxl import load_workbook

load_wb = load_workbook("./law_data/law_data.xlsx")
load_ws = load_wb['sheet1']

values = []
output = []
law_dict = {}
num_row = 17143 # number of rows of excel file

i=0
for row in load_ws.rows:
    i +=1
    if i == num_row :
        break

    row_value = []
    for cell in row:
        if cell.value != None :
            row_value.append(cell.value)
    values.append(row_value)

for j in range(len(values)) :
    if str(type(values[j][0])) == "<class 'int'>" :
        del values[j][0]
        output.append(values[j])
    else :
        output[-1].extend(values[j])

# filtering error data (blank etc..)
idx = 0
while True :
    if idx == len(output) :
        break
    if len(output[idx]) % 2 == 1 :
        del output[idx]
        idx-=1
    idx+=1

# preprocessing data
for i in range(len(output)) :
    t_len = int(len(output[i])/2)

    for j in range(t_len) :
        pre = str(output[i][2*j])
        post = str(output[i][2*j+1]).split(', ')
        for k in range(len(post)) :
            if post[k][-2] == "의" :
                post[k] = post[k][0:-2]

            final = pre+' '+post[k]
            if final in law_dict :
                law_dict[final] += 1 # count+1
            else :
                law_dict[final] = 1 # new

law_list = list(law_dict.keys()) # list of whole laws used in all cases
law_num = len(law_list) # number of whole laws used in all cases

# code for checking whether our clustering is done in right way
"""
f1=open('./law_index.txt','w')
for i in range(len(law_list)) :
    line = str(i)+"."+law_list[i]+"\n"
    f1.write(line)
f1.close()
"""

np_law_list = np.array(law_list)
np.save('law_list',np_law_list)

distance_matrix = []

# initiate distance matrix uniformly (The distance between all laws is 1.)
for i in range(law_num) :
    tmp = []
    for j in range(law_num) :
        if i==j :
            tmp.append(0.0)
        else :
            tmp.append(1.0)
    distance_matrix.append(tmp)

distance_matrix = np.array(distance_matrix) # initiated distance matrix

# update distance matrix
for i in range(len(output)) :
    t_len = int(len(output[i])/2)

    for j in range(t_len) :
        case_law = [] # list for saving laws used in same case
        do_monitor = False

        pre = str(output[i][2*j])
        post = str(output[i][2*j+1]).split(', ')
        for k in range(len(post)) :
            if post[k][-2] == "의" :
                post[k] = post[k][0:-2]
            final = pre+' '+post[k]
            case_law.append(final)

            # code for checking whether our clustering is done in right way    
            if final == "문화재보호법 제2조" :
                do_monitor = True

        # code for checking whether our clustering is done in right way
        if do_monitor :
            print("="*30);print(case_law);print("="*30)

        if len(case_law)==1 :
            continue

        ## shorten distance between laws used in same case (multiply 0.5)
        idx_list = []
        for k in range(len(case_law)) :
            idx_list.append(law_list.index(case_law[k]))

        for n1 in idx_list :
            for n2 in idx_list :
                if n1 == n2 :
                    continue
                distance_matrix[n1][n2] = distance_matrix[n1][n2]/2

# save custom metric as binary file
np.save('law_data/custom_metric',distance_matrix)