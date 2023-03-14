import sys
import torch
from IPython.display import display
from libraries.datamodule import vocab
from torchvision.transforms import ToTensor
from libraries.lit_comer import LitCoMER as tra
import torchvision.transforms as transforms
import sympy
from PIL import Image
import PIL.ImageOps    

import matplotlib.pyplot as plt

def predict(image_name):
    ckpt = 'epoch=151-step=57151-val_ExpRate=0.6365.ckpt'
    model = tra.load_from_checkpoint(ckpt)
    model = model.eval()
    device = torch.device("cpu")
    model = model.to(device)

    img = Image.open("img.png")
    transform=transforms.Grayscale()
    img=transform(img)
    display(img)
    img = PIL.ImageOps.invert(img)
    img = ToTensor()(img)

    img=img[:3]



    mask = torch.zeros_like(img, dtype=torch.bool)
    hyp = model.approximate_joint_search(img.unsqueeze(0), mask)[0]
    pred_latex = vocab.indices2label(hyp.seq)

    return(pred_latex)

argument = sys.argv
predict_val=predict(argument[1])
print("\n")
print(predict_val)
