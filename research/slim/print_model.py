import tensorflow as tf
from tensorflow.python.tools.inspect_checkpoint import print_tensors_in_checkpoint_file

import os

# simple version for working with CWD
# print(len([name for name in os.listdir('/mnt/sda1/parasites/eggs_9/A.lumbricoides') if os.path.isfile(name)]))

# path joining version for other paths
# DIR = '/mnt/sda1/leaves'
# for dtname in sorted(os.listdir(DIR)):
#     print('\n')
#     print('*' * 30)
#     print(dtname)
#     print('*' * 30)
#     totalSamples = 0
#     classes = os.path.join(DIR, dtname)
#     for c in sorted(os.listdir(classes)):
#         l = os.path.join(classes, c)
#         samples = len([name for name in os.listdir(l) if os.path.isfile(os.path.join(l, name))])
#         print(c + ',' + str(samples))
#         totalSamples += samples
#     print('## Total Samples ' + str(totalSamples))
#

if __name__ == '__main__':
    print(os.path.exists('/mnt/sda1/labels_*.txt'))