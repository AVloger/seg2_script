import os
import sys
import argparse
import json
import shutil

import video
from segmentation_utils import *


def pose_estimation(openpose, out_folder, video_path, model_name, model_folder):
    video_name = video_path.split('/')[-1].split('.')[0]
    video_dir = video_path.split('/')[-2]
    output_snippets_dir = os.path.join(out_folder,'openpose_estimation/{}/{}/{}'.format(model_name, video_dir,video_name))
    output_sequence_dir = os.path.join(out_folder,'packed/{}'.format(video_dir))
    if not os.path.exists(output_sequence_dir):
        os.makedirs(output_sequence_dir)
    output_sequence_path = '{}/{}.json'.format(output_sequence_dir, video_name)
    # pose estimation
    openpose_args = dict(
        video=video_path,
        write_json=output_snippets_dir,
        display=0,
        render_pose=0,
        model_pose=model_name,
        model_folder=model_folder)
    command_line = openpose + ' '
    command_line += ' '.join(['--{} {}'.format(k, v) for k, v in openpose_args.items()])
    shutil.rmtree(output_snippets_dir, ignore_errors=True)
    os.makedirs(output_snippets_dir)
    LOGGER.info(command_line)
    os.system(command_line)
    # pack openpose ouputs

    # video_obj = video.get_video_frames(video_path)
    # height, width, _ = video_obj[0].shape
    video_info = json_pack(
        output_snippets_dir, video_name)
    with open(output_sequence_path, 'w') as outfile:
        json.dump(video_info, outfile)
    if len(video_info['data']) == 0:
        LOGGER.info('Can not find pose estimation results of %s'%(video_name))
        return
    else:
        LOGGER.info('%s Pose estimation complete.'%(video_name))

def main():
    parser = argparse.ArgumentParser(description='Skating Data Converter.')
    # region arguments yapf: disable
    parser.add_argument('--openpose',
        default='/openpose/build',
        help='Path to openpose')
    parser.add_argument(
        '--data_path', default='/openpose/data/x77',help="Path to dataset")
    parser.add_argument(
        '--out_folder', default='/openpose/output_77',help="Path to save files")
    parser.add_argument(
        '--model_folder', default='/openpose/models',help="Path to model folder")
    arg = parser.parse_args()
    openpose = '{}/examples/openpose/openpose.bin'.format(arg.openpose)
    p = 'segmentation'
    root = os.listdir(arg.data_path)
    root.sort(key=lambda x: int(x[1:3]))
    for files in root:
        files_path = os.path.join(arg.data_path,files)
        pose_estimation(openpose, arg.out_folder, files_path, "BODY_25", arg.model_folder)


    # root.sort(key=lambda x: int(x[1:]))
    # for dir in root:
    #     dir_path = os.path.join(arg.data_path,dir)
    #     dir_list = os.listdir(dir_path)
    #     dir_list.sort(key=lambda x: int(x[1:3]))
    #     dir_list = dir_list[-3:]
    #     for files in dir_list:
    #         files_path = os.path.join(dir_path,files)
    #         pose_estimation(openpose, arg.out_folder, files_path, "BODY_25", arg.model_folder)

if __name__ == '__main__':
    main()
