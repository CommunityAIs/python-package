import torch
import torch.nn as nn

def loadnn(
    model:str, *,
    path:str="./models",
    eval:bool=True,
):
    model: nn.Module = torch.load(f"{path}/{model}/nn.ai")
    if eval:
        model.eval()
    else:
        model.train()
    
    return model