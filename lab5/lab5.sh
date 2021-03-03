#!/bin/bash

echo "Installing dependencies for lab1"

sudo apt-get update
sudo apt-get install -y python
sudo apt-get install -y python-pip
pip install numpy
sudo pip install numpy
pip install gym==0.12.1
sudo pip install gym==0.12.1
pip install networkx
sudo pip install networkx
sudo apt-get install -y python-matplotlib
