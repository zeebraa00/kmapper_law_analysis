import operator
import numpy as np
from openpyxl import load_workbook

load_wb = load_workbook("./law_data/law_data.xlsx")
load_ws = load_wb['sheet1']

values = []
output = []
law_dict = {}

i=0
for row in load_ws.rows:
    i +=1
    # if i == 17143 :
    if i == 500 :
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

## 오류 데이터 필터링
idx = 0
while True :
    if idx == len(output) :
        break
    if len(output[idx]) % 2 == 1 :
        del output[idx]
        idx-=1
    idx+=1

## 법 데이터 전처리 및 카운트
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

# print(law_dict)

law_list = list(law_dict.keys()) ## 판례에서 사용된 법 리스트 -> 인덱스 유지해야함
law_num = len(law_list) ## 판례에서 사용된 법 갯수

# for i in law_dict.items() :
#     print(i)

distance_matrix = []

## initiate distance matrix
for i in range(law_num) :
    tmp = []
    for j in range(law_num) :
        if i==j :
            tmp.append(0.0)
        else :
            tmp.append(1.0)
    distance_matrix.append(tmp)

distance_matrix = np.array(distance_matrix)

print(distance_matrix)

# update distance matrix
for i in range(len(output)) :
    t_len = int(len(output[i])/2)

    for j in range(t_len) :
        case_law = []
        pre = str(output[i][2*j])
        post = str(output[i][2*j+1]).split(', ')
        for k in range(len(post)) :
            if post[k][-2] == "의" :
                post[k] = post[k][0:-2]
            final = pre+' '+post[k]            
            case_law.append(final)

        n = len(case_law)
        if n==1 :
            continue
        ## shorten distance between laws
        idx_list = []
        for k in range(n) :
            idx_list.append(law_list.index(case_law[k]))
        print(idx_list)
        for n1 in idx_list :
            for n2 in idx_list :
                if n1 == n2 :
                    continue
                distance_matrix[n1][n2] = distance_matrix[n1][n2]/2

for i in range(len(distance_matrix)) :
    print(distance_matrix[i])

print(distance_matrix)