import glob
import os
import random
import numpy


if __name__ == '__main__':
    samples = os.listdir('final_dataset/groundtrue')
    splits = 'final_dataset/splits'
    total = len(samples)
    radio = 0.7
    offset = int(total*radio)
    for i in range(5):
        random.shuffle(samples)
        train_set = samples[:offset]
        test_set = samples[offset:]
        train_path = os.path.join(splits,'train.split{}.bundle'.format(i))
        test_path = os.path.join(splits, 'test.split{}.bundle'.format(i))
        with open(train_path, 'w') as f:
            for line in train_set:
                f.write(line + '\n')
            f.close()
        with open(test_path, 'w') as f:
            for line in test_set:
                f.write(line + '\n')
            f.close()
    print("sucessful")