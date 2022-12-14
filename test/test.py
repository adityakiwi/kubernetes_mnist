from PIL import Image
import os
from flask import Flask, json, request
import time
import argparse 
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.optim.lr_scheduler import StepLR


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.dropout1 = nn.Dropout(0.25)
        self.dropout2 = nn.Dropout(0.5)
        self.fc1 = nn.Linear(9216, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout1(x)
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.dropout2(x)
        x = self.fc2(x)
        output = F.log_softmax(x, dim=1)
        return output

def test(image):
    model = Net().to('cpu')
    model.load_state_dict(torch.load('/models/mnist.pth'))
    model.eval()
    image = image.to('cpu')
    output = model(image)
    index = output.data.numpy().argmax()
    return str(index)


def transform():
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
        ])
    return transform

api = Flask(__name__)

@api.route('/test', methods=['POST'])
def get_result():
    res = {}
    file = request.files['image']
    if not file:
        res['result'] = 'no image'
    else:
        res['result'] = 'done'
        image = Image.open(file.stream).convert('L')
        transform_obj = transform()
        image  = transform_obj(image)
        image = image.unsqueeze(0)
        ans = test(image)
        res['Predicted Digit'] = ans

    return json.dumps(res)

api.run(host='0.0.0.0', port=5000)

def main():
    img = Image.open("img_4.png")
    img = transform(img)
    img = img.unsqueeze(0)
    ans = test(img)
    print(ans)
main()