import imageio
from argparse import ArgumentParser
from tqdm import tqdm
import os
from copy import deepcopy

parser = ArgumentParser()
parser.add_argument("--root", help="path to video folder")

args = parser.parse_args()

video_folders = os.listdir(args.root)

copied_video_folders = deepcopy(video_folders)

# 删除以“_processed”结尾的文件夹
for folder in copied_video_folders:
    if folder.endswith('_processed'):
        video_folders.remove(folder)


for i, folder in enumerate(video_folders):
    """处理每个文件夹"""
    print('process folder{0}:{1}'.format(i, folder))
    folder = os.path.join(args.root, folder)
    out_folder = folder+'_processed'
    print('out_folder is {}'.format(out_folder))
    out_folder = os.path.join(args.root, out_folder)
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)

    # 获取输出文件夹中已处理完毕的视频的名字
    existed_video = os.listdir(out_folder)

    # 获取视频文件夹的MP4视频
    video_name = os.listdir(folder)
    for video in tqdm(video_name):
        # 处理过的视频就不要处理了
        if video in existed_video:
            continue
        video_out_folder = os.path.join(out_folder, video)
        # 创建每个视频的文件夹
        if not os.path.exists(video_out_folder):
            os.mkdir(video_out_folder)
        reader = imageio.get_reader(os.path.join(folder, video))
        for i, frame in enumerate(reader):
            imageio.imsave(os.path.join(video_out_folder, str(i).zfill(7)+'.png'), frame
