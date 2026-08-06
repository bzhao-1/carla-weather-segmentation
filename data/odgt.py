# create odgt files for training and validation for custom dataset 

import argparse
import cv2
import json
import os

def odgt(img_path):
    seg_path = img_path.replace('images','annotations')
    seg_path = seg_path.replace('.jpg','.png')
    
    if os.path.exists(seg_path):
        img = cv2.imread(img_path)
        h, w, _ = img.shape

        odgt_dic = {}
        odgt_dic["fpath_img"] = img_path
        odgt_dic["fpath_segm"] = seg_path
        odgt_dic["width"] = w
        odgt_dic["height"] = h
        return odgt_dic
    else:
        # print('the corresponded annotation does not exist')
        # print(img_path)
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create ODGT manifests from an image/annotation dataset")
    parser.add_argument("--data-dir", default="data", help="directory containing images/ and annotations/")
    parser.add_argument("--output-dir", default=None, help="manifest output directory (defaults to --data-dir)")
    args = parser.parse_args()

    modes = ['training', 'validation'] # customized
    saves = ['Carla1_training.odgt', 'Carla1_validation.odgt']
    base_dir = os.path.abspath(args.data_dir)
    output_dir = os.path.abspath(args.output_dir or args.data_dir)
    os.makedirs(output_dir, exist_ok=True)

    for i, mode in enumerate(modes):
        save = saves[i]
        dir_path = os.path.join(base_dir, 'images', mode)
        img_list = os.listdir(dir_path)
        img_list.sort()
        img_list = [os.path.join(dir_path, img) for img in img_list]

        odgtPath = os.path.join(output_dir, save)
        with open(odgtPath, mode='wt', encoding='utf-8') as myodgt:
            for i, img in enumerate(img_list):
                a_odgt = odgt(img)
                if a_odgt is not None:
                    myodgt.write(f'{json.dumps(a_odgt)}\n')
