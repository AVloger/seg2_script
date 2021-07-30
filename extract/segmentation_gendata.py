import os
import sys
import pickle
import argparse

import numpy as np
from numpy.lib.format import open_memmap

from segmentation_feeder import Feeder_skating
import json

toolbar_width = 30

def print_toolbar(rate, annotation=''):
    # setup toolbar
    sys.stdout.write("{}[".format(annotation))
    for i in range(toolbar_width):
        if i * 1.0 / toolbar_width > rate:
            sys.stdout.write(' ')
        else:
            sys.stdout.write('-')
        sys.stdout.flush()
    sys.stdout.write(']\r')


def end_toolbar():
    sys.stdout.write("\n")
def feeder(sample_path,data_shape,num_person_out):
    with open(sample_path, 'r') as f:
        video_info = json.load(f)
    num_person_out = num_person_out
    num_person_in = data_shape[-1]
    # fill data_numpy
    data_numpy = np.zeros(data_shape)
    max = 0  ## the data of frme_index in json only means the fram_index of each points, but is not means the max_frames.
    for frame_info in video_info['data']:
        frame_index = frame_info['frame_index']
        if frame_index>=max:
            max = frame_index
        for m, skeleton_info in enumerate(frame_info["skeleton"]):
            if m >= num_person_in:
                break
            pose = skeleton_info['pose']
            score = skeleton_info['score']
            data_numpy[0, frame_index, :, m] = pose[0::2]
            data_numpy[1, frame_index, :, m] = pose[1::2]
            data_numpy[2, frame_index, :, m] = score
    #delete other frames

    data_numpy = data_numpy[:,:max+1,:,:]
    # centralization
    # data_numpy[0:2] = data_numpy[0:2] - 0.5
    data_numpy[0][data_numpy[2] == 0] = 0
    data_numpy[1][data_numpy[2] == 0] = 0

    # get & check label index
    # label = video_info['label_index']
    # assert (self.label[index] == label)

    # sort by score
    sort_index = (-data_numpy[2, :, :, :].sum(axis=1)).argsort(axis=1)
    for t, s in enumerate(sort_index):
        data_numpy[:, t, :, :] = data_numpy[:, t, :, s].transpose((1, 2,
                                                                   0))
    data_numpy = data_numpy[:, :, :, 0:num_person_out]
    data_numpy = np.squeeze(data_numpy,3).transpose((1,2,0))

    return data_numpy,max+1
def gendata(
        data_path,
        data_out_path,
        video_name,
        num_person_in=5,  #observe the first 5 persons
        num_person_out=1,  #then choose 1 persons with the highest score
        max_frame=15000,
        joins_count=25):

    data_in_shape = (3, max_frame, joins_count, num_person_in)
    data,frame_index = feeder(data_path,data_in_shape,num_person_out)

    data_out_shape = (frame_index, joins_count, 3)
    if not os.path.exists(data_out_path):
        os.makedirs(data_out_path)
    data_out = os.path.join(data_out_path,video_name)
    fp = open_memmap(
        data_out,
        dtype='float64',
        mode='w+',
        shape=data_out_shape)
    fp[0:data.shape[0],:,:] = data



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Skating-skeleton Data Converter.')
    parser.add_argument(
        '--data_path', default='/openpose/output_77/packed/x77',help="Path to dataset")
    parser.add_argument(
        '--out_folder', default='/openpose/output_77/finish',help="Path to save files")
    arg = parser.parse_args()
    root = os.listdir(arg.data_path)
    root.sort(key=lambda x: int(x[1:3]))
    for files in root:
        files_path = os.path.join(arg.data_path,files)
        video_name = 'n{}_{}.npy'.format('77',files[:3])
        data_out_path = arg.out_folder
        gendata(files_path, data_out_path,video_name)

    # for dir in root:
    #     dir_path = os.path.join(arg.data_path,dir)
    #     dir_list = os.listdir(dir_path)
    #     dir_list.sort(key=lambda x: int(x[1:3]))
    #     for files in dir_list:
    #         files_path = os.path.join(dir_path,files)
    #         video_name = 'n{}_{}.npy'.format(dir[1:],files[:3])
    #         data_out_path = arg.out_folder
    #         gendata(files_path, data_out_path,video_name)
    # data_path =  os.path.join(arg.out_folder,'packed/x38/p01.json')
    # data_out_path = os.path.join(arg.out_folder,'finish')
    # video_name = 'n38_p01.npy'
    # gendata(data_path, data_out_path,video_name)
    # a = np.load('/openpose/output/finish/n38_p01.npy')
    # print(a[2][0])
    # with open(data_path, 'r') as f:
    #     video_info = json.load(f)
    #     print(video_info['data'])