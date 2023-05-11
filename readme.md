# CITECORE RPI 2022-23: RF Sensing Postures without Cameras

# RPI 2022 Monitoring Human Pose with Radios: A Correlated Knowledge Fusion Distillation Approach 
This project has developed a first aged-care home-ready, RF-based posture tracking system to provide accurate data and analytics without cameras or sensors attached to the human body. It was developed by Deakin researchers led by CITECORE research center.  They have developed a correlated knowledge distillation system for realizing a hybrid RF and camera framework for privacy-preserving human activity detection using software-defined radios. Although monitoring patients is the primary inspiration for this work, the developed system has many potential applications outside of healthcare, including autonomous vehicles, smart agriculture, transportation, and educational environments. This repository aims use WiFi signals and camera for indoor localization. The camera is mainly used to help the machine learning model to learn how to extract pose coordinates from WiFi Channel State Information Data.
## Getting Started



### Dependencies

#### (Recommended) Install with conda
* Python 3.9.16
* PyTorch 1.13.1
* HDF5 1.10.6
* Matplotlib 3.6.2
* OpenCV 4.6.0

### Installing
```
# 1. First clone this repository: 
git clone https://github.com/deolsatish/RPI-Project.git

# 2. Create a conda virtual environment.
conda create -n rpi python=3.9.16 -y
conda activate rpi

# 3. Install PyTorch
conda install pytorch torchvision torchaudio pytorch-cuda=11.6 -c pytorch -c nvidia

```

### Executing program

To execute Programs:

```
# 1. Run WiSPPN_Test_PAM.ipynb on Jupyter Notebooks or other alternative
This piece of code tests the machine learning model with pre-trained models

# 2. Run WiSPPN_Train_ and_Test_PAM..py as a python file
This piece of code trains the machine learning model an saves the trained model

# 3. Run capture_cam on Jupyter Notebooks or other alternative
This piece of code saves a duration of video footage from your webcam with its timestamps for each frame in a Json file

# 4. Go to Alphapose project folder to run it, it will require a different python environment. 
Alphapose allows us to generate 18-keypoint pose coordinates from our video.


```

## Alphapose extracting pose coordinates from video



https://user-images.githubusercontent.com/52904167/223569808-1e6cac40-7675-4b55-8f96-e04939ab551a.mp4





## 18 Keypoints Person Pose annotations
![18keypointsdesc](https://user-images.githubusercontent.com/52904167/220470742-9ae63a54-8ab5-4e0d-8964-31bfa0b37503.png)


## Network Framework

![WiSPPN System Framework](https://user-images.githubusercontent.com/52904167/220470773-c100fe34-4fcf-4646-b695-413883ab043b.jpeg)

## A training example image
![3-128training_imag](https://user-images.githubusercontent.com/52904167/223571939-424c626c-e975-46f6-96c8-b85bde991c21.jpg)









