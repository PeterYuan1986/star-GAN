import SimpleITK as sitk
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from utils import *
import argparse
import matplotlib

matplotlib.use('Agg')

def parse_args():
    desc = "Tensorflow implementation of StarGAN_v2"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--result_dir', type=str, default='results',
                        help='Directory name to save the sample or test images')
    return parser.parse_args()

def image_to_tf(filename):
    itk_img = sitk.ReadImage(filename)
    itk_img = resize(itk_img, 80,80,80,1)  ###peter
    x = sitk.GetArrayFromImage(itk_img)
    x_decode = tf.convert_to_tensor(x,dtype='float32')
    return preprocess_fit_train_image(x_decode)
#

def showNii(img):
    itk_img = sitk.ReadImage(img)
    img = sitk.GetArrayFromImage(itk_img)
    for i in range(0,img.shape[0],10):
        plt.imshow(img[i, :, :], cmap='gray')
        plt.show()

# itk_img = resize(itk_img, 80,80,80)  ###peter
# x = sitk.GetArrayFromImage(itk_img)
# # y = np.expand_dims(x, axis=3)
# # print(y.shape)
# t = tf.constant([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]])
# # print('sas',t.shape)
#
# import nibabel as nib
# def image_to_tf(filename):
#     itk_img = sitk.ReadImage(filename)
#     print(itk_img.GetSize())
#     itk_img = resize(itk_img, 200,200,200)  ###peter
#     x = sitk.GetArrayFromImage(itk_img)
#     new_image = nib.Nifti1Image(x, affine=np.eye(4))
#     nib.save(new_image, './test.nii')
#
#
# xx='co20130204_101449T1mprages003a1001.nii'
# image_to_tf(xx)
"""main"""
def main():
    args = parse_args()
    img=args.result_dir
    print (img)
    img='ref_0002000.nii'
    showNii(img)

if __name__ == '__main__':
    main()