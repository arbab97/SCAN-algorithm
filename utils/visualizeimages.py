<<<<<<< HEAD

temp_path="/media/ausserver4/DATA/Code/experiments/audio data analysis/audio-clustering/plots/spectrograms/batsnet_train/1/20150623_213547.wav.png"
from PIL import Image
img=None
with open(temp_path, 'rb') as f:
        img = Image.open(f).convert('RGB')


#default for Tensor
import numpy as np;import matplotlib.pyplot as plt;plt.imshow( np.moveaxis(img.numpy(), 0,2));plt.show()

#default for numpy array
import numpy as np;import matplotlib.pyplot as plt;plt.imshow(img);plt.show()

=======
import numpy as np;import matplotlib.pyplot as plt;plt.imshow( np.moveaxis(inspect['image_augmented'].numpy(), 0,2))
>>>>>>> db23360031c529a04f0a144b63e5f3fe49feb44f
