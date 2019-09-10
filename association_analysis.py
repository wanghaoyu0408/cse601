import numpy as np
import math
import re
from collections import Counter


def filter_data(x):
    if x == 'Up':
        return 1
    else:
        return 0


def generate_combination(input_, stable_set_):
    output = []
    input_.sort()
    for i in range(len(input_)):
        for j in range(i+1, len(input_)):
              temp1  = set(input_[i])|set(input_[j])
              if len(input_[0]) == 1:
                  temp2 = list(temp1)
                  temp2.sort()
                  output.append(temp2)
              else:
                  if input_[i][-1] == input_[j][-1]:
                      temp2 = list(temp1)
                      temp2.sort()
                      output.append(temp2)
#    if len(input_[0]) == 1:
#        for i in input_:
#            for j in stable_set_:
#                if j[0] not in i:
#                    temp = i+j
#                    temp.sort()
#                    output.append(temp)
#    else:
#        for i in range(len(input_)):
#            for j in range(i+1, len(input_)):
#               temp1  = set(input_[i])|set(input_[j])
#               if len(temp1) == len(input_[0])+1:
#                   temp2 = list(temp1)
#                   temp2.sort()
#                   output.append(temp2)
    return output


#def computing_support(input_, feature_, threshold):
def filter_feature(input_, feature_, threshold):
    output = []
    for i in input_:
        support_score = 0
        for j in feature_:
            support_score += set(i) < set(j)
        if support_score > threshold:
            output.append(i)
    return output


#def filter_feature(input_, feature_, threshold):
#    score = computing_support(input_, feature_)
#    for i, idx in enumerate(score):
#        if i < threshold:
#            input_.remove(input_[idx])
#    return input_


feature = []
label = []
association_set = []
feature_ = []
stable_set = []
with open(r'D:\\associationruletestdata.txt', 'r') as f:
#with open('D:\\testdata', 'r') as f:
    while f:
        line = f.readline()
        line = re.split('\n|\t', line)
        line.remove('')
        if line:
            feature_.append(['G'+str(itera)+'_'+i for itera,i in enumerate(line)])
            feature_this = map(filter_data, line[:-1])
            feature.append(list(feature_this))
            label.append(line[-1])
        else:
            break


feature = np.array(feature)
support_ratio = 0.5
support_num = math.ceil(len(label)*support_ratio)
feature_sum = np.sum(feature, 0)
idx = feature_sum > support_num
label = Counter(label)
for i in label:
    if label[i] >= support_num:
        association_set.append([i])
        stable_set.append([i])
print('a')
for iteration, num in enumerate(idx):
    if num:
        association_set.append(['G'+str(iteration)+'_'+'Up'])
        stable_set.append(['G'+str(iteration)+'_'+'Up'])
    else:
        association_set.append(['G'+str(iteration)+'_' + 'Down'])
        stable_set.append(['G'+str(iteration)+'_' + 'Down'])
print('b')
init = stable_set
for i in range(len(stable_set)-1):
    f = generate_combination(init, stable_set)
    print('c')
    init = filter_feature(f, feature_, support_num)
    print('d')
    if init:
        association_set += init
    else:
        break
print(association_set)