### PARAMETER FILE ###
import torch
import os


###MODEL

#There are a lot of ways to load up a model in pytorch, just do whatever you need to do here such that there is a variable 'model' in this file pointing to a working feed-forward CNN
from model_classes import cifar_CNN_prunned
model = cifar_CNN_prunned()
model.load_state_dict(torch.load('./models/cifar_prunned_0.816_state_dict.pt'))


###IMAGE PATHS

input_img_path =  './image_data/cifar10/input_images'   #Set this to the system path for the folder containing input images you would like to see network activation maps for.
rank_img_path = './image_data/cifar10/ranking_images'       #Set this to a path with subfolders, where each subfolder contains a set of images. Subgraph ranks will be based on these subfolders. 

output_folder = 'cifar10_prunned'     #name of folder you want prep model to output to. Not a path here, just a name, it will appear as a folder under prepped_models/. 
									  #When you launch the visualization tool you will do so with respect to this folder name

###IMAGE PREPROCESSING

from torchvision import transforms

#preprocess = None     # Set this to None or False if you dont want your input images to be preprocessed. Or set this to a torchvision transform, as in the example below. If you use
					  # a transform to load your test data set when training your model, put that in below.

preprocess =   transforms.Compose([
								 transforms.Resize((32,32)),
                                 transforms.ToTensor(),
                                 transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
                             	 ])

#GPU
cuda = True       #use GPU acceleration

#LOSS
criterion = torch.nn.CrossEntropyLoss()   #this should be set to whatever loss function was used to train your model

#AUX (these params arent super important but you might want to change them)
num_workers = 4     #num workers argument in dataloader
seed = 2            #manual seed
batch_size = 200    #batch size for feeding rank image set through model (input image set is sent through all at once)






#Clean up (YOU DONT NEED TO EDIT ANYTHING BELOW THIS LINE)

input_img_path =  os.path.abspath(input_img_path)
rank_img_path = os.path.abspath(rank_img_path)


