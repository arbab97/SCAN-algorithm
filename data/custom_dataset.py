"""
Author: Wouter Van Gansbeke, Simon Vandenhende
Licensed under the CC BY-NC 4.0 license (https://creativecommons.org/licenses/by-nc/4.0/)
"""
import numpy as np
import torch
from torch.utils.data import Dataset
""" 
    AugmentedDataset
    Returns an image together with an augmentation.
"""
class AugmentedDataset(Dataset):
    def __init__(self, dataset, standard_transformer):
        super(AugmentedDataset, self).__init__()
        transform = dataset.transform
        dataset.transform = None
        self.dataset = dataset
        
        if isinstance(transform, dict):
            self.image_transform = transform['standard']
            self.augmentation_transform = transform['augment']

        else:
            self.image_transform = standard_transformer
            self.augmentation_transform = transform

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, index):
        sample = self.dataset.__getitem__(index)
        image = sample['image']
        path=sample['path']
##
       # sample['image'] = self.image_transform(image)
        sample_image=image
        for t in self.image_transform.transforms:
            if (str(t).find("batsnet_transformation")!=-1):
                sample_image = t( sample_image, path)
            else:
                sample_image = t(sample_image)
        sample['image']=sample_image
##
        #sample['image_augmented'] = self.augmentation_transform(image)
        augmented_image=image
        for t in self.augmentation_transform.transforms:
            if (str(t).find("batsnet_transformation")!=-1):
                augmented_image = t( augmented_image, path)
            else:
                augmented_image = t(augmented_image)        
        sample['image_augmented'] =augmented_image

        return sample


""" 
    NeighborsDataset
    Returns an image with one of its neighbors.
"""
class NeighborsDataset(Dataset):
    def __init__(self, dataset, indices, num_neighbors=None):
        super(NeighborsDataset, self).__init__()
        transform = dataset.transform
        
        if isinstance(transform, dict):
            self.anchor_transform = transform['standard']
            self.neighbor_transform = transform['augment']
        else:
            self.anchor_transform = transform
            self.neighbor_transform = transform
       
        dataset.transform = None
        self.dataset = dataset
        self.indices = indices # Nearest neighbor indices (np.array  [len(dataset) x k])
        if num_neighbors is not None:
            self.indices = self.indices[:, :num_neighbors+1]
        assert(self.indices.shape[0] == len(self.dataset))

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, index):
        output = {}
        anchor = self.dataset.__getitem__(index)
        
        neighbor_index = np.random.choice(self.indices[index], 1)[0]
        neighbor = self.dataset.__getitem__(neighbor_index)

       # anchor['image'] = self.anchor_transform(anchor['image'])
        temp=anchor['image']
        for t in self.anchor_transform.transforms:
            if (str(t).find("batsnet_transformation")!=-1):
                temp = t( temp, anchor["path"])
            else:
                temp = t(temp) 
        anchor['image']=temp

        #neighbor['image'] = self.neighbor_transform(neighbor['image'])
        temp=neighbor['image']
        for t in self.neighbor_transform.transforms:
            if (str(t).find("batsnet_transformation")!=-1):
                temp = t( temp, anchor["path"])
            else:
                temp = t(temp) 
        neighbor['image']=temp

        output['anchor'] = anchor['image']
        output['neighbor'] = neighbor['image'] 
        output['possible_neighbors'] = torch.from_numpy(self.indices[index])
        output['target'] = anchor['target']
        
        return output
