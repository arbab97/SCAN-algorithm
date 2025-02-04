"""
Authors: Wouter Van Gansbeke, Simon Vandenhende
Licensed under the CC BY-NC 4.0 license (https://creativecommons.org/licenses/by-nc/4.0/)
"""
import os


class MyPath(object):
    @staticmethod
    def db_root_dir(database=''):
        db_names = {'cifar-10', 'stl-10', 'cifar-20', 'imagenet', 'imagenet_50', 'imagenet_100', 'imagenet_200', 'batsnet'}
        assert(database in db_names)

        if database == 'cifar-10':
            return '/media/ausserver4/DATA/Code/experiments/SCAN ALGO/Unsupervised-Classification'
        
        elif database == 'cifar-20':
            return '/path/to/cifar-20/'

        elif database == 'stl-10':
            return '/media/ausserver4/DATA/Code/experiments/SCAN ALGO/Unsupervised-Classification'
        
        elif database in ['imagenet', 'imagenet_50', 'imagenet_100', 'imagenet_200']:
            return '/path/to/imagenet/'
        
        elif database in ['batsnet']:
            return '/media/ausserver4/DATA/Code/experiments/audio data analysis/audio-clustering/plots/spectrograms'
        else:
            raise NotImplementedError
