import numpy as np
import os
import sys
import matplotlib.pyplot as plt
import re

def plot_hog(myDictionary):
    pos = np.arange(len(myDictionary.keys()))
    ax = plt.axes()
    width = 1.0
    plt.bar(myDictionary.keys(), myDictionary.values(), facecolor = 'lightskyblue')
    plt.xticks(pos, myDictionary.keys(), rotation=90, fontsize=20)
    plt.show()
def valiation(data_path,valid_path):
    root = os.listdir(data_path)
    sum =0
    for player in root:
        data = os.path.join(data_path,player)
        valid = os.path.join(valid_path,'{}.npy'.format(player[:-4]))

        with open(data,'r') as f:
            data = f.readlines()
            length = len(data)
            a = np.load(valid)
            if length == a.shape[0]:
                print("Yes")
            elif abs(length - a.shape[0])<5:
                sum += 1
                print('Small Errors')
                print(valid)
                print(length)
                print(a.shape[0])
            elif abs(length - a.shape[0])>=5:
                sum += 1
                print('Big Errors')
                print(valid)
                print(length)
                print(a.shape[0])
            else:
                print("Error")
                print(valid)
                print(length)
                print(a.shape[0])
                sys.exit()
    print(sum)
def revaliation(data_path,valid_path):
    root = os.listdir(valid_path)
    for player in root:
        data = os.path.join(valid_path,player)
        valid = os.path.join(data_path,'{}.txt'.format(player[:-4]))
        with open(valid,'r') as f:
            valid = f.readlines()
            length = len(valid)
            a = np.load(data)
            if length == a.shape[0]:
                print("Yes")
            elif abs(length - a.shape[0])<100:
                print('May be Errors')
                print(valid)
                print(length)
                print(a.shape[0])
            else:
                print("Error")
                print(valid)
                print(length)
                print(a.shape[0])
                sys.exit()
    print("revaliation sucessful")
if __name__ == '__main__':
    data_path = "groundtrue"
    valid_path = "final_dataset/finish"
    # valiation(data_path, valid_path)
    # revaliation(data_path, valid_path)
    # print('sucessful')
    root = os.listdir(data_path)
    dict = {}

    for player in root:
        data = os.path.join(data_path,player)
        valid = os.path.join(valid_path,'{}.npy'.format(player[:-4]))
        with open(data,'r') as f:
            for line in f:
                if line[:-1]!='None' and line!=last :
                    dict[line[:-1]] = dict.get(line[:-1], 0) + 1
                last = line
            f.close()
    Sort = False
    with open('mapping.txt','w') as f:
        if Sort:
            sort = sorted(dict.keys())
            for line in sort:
                f.write('{}\n'.format(line))
            f.close()
        else:
            # only character
            redict = {}
            for key in dict:
                result = re.sub(r'[0-9]+', '', key)
                redict[result] = redict.get(result,0)+dict.get(key,0)

            sort = sorted(dict.items(),key=lambda item:item[1],reverse=True)
            f.write('{} {}\n'.format(str(0), 'None'))
            for i,line in enumerate(sort):
                a = line[0]
                b = i+1
                f.write('{} {}\n'.format(str(b),a))
            f.close()
    # plot_hog(dict)
    print(len(dict.keys()))


