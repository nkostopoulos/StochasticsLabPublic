#!/bin/bash

echo "Installing dependencies for lab1"

sudo apt-get update
sudo apt-get install -y python-pip
pip install numpy
sudo pip install numpy
pip install matplotlib
sudo pip install matplotlib
pip install sklearn
sudo pip install sklearn
pip install pandas
sudo pip install pandas
sudo apt-get install -y python-tk
