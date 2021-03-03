#!/bin/bash

echo "Installing dependencies for lab3"

sudo apt-get update
sudo apt-get install -y python3
sudo apt-get install -y python-pip
pip3 install numpy
sudo pip3 install numpy
pip3 install scipy
sudo pip3 install scipy
pip3 install matplotlib
sudo pip3 install matplotlib
pip3 install networkx
sudo pip3 install networkx
pip3 install jupyter
sudo pip3 install jupyter
