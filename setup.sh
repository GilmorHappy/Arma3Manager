#!/usr/bin/env bash
set -e

# Ensure multiverse repository is enabled and i386 architecture is available
sudo apt-get update
sudo apt-get install -y software-properties-common
sudo dpkg --add-architecture i386
sudo add-apt-repository -y multiverse
sudo apt-get update

# Install required packages including steamcmd and Python
sudo apt-get install -y python3 python3-pip steamcmd lib32gcc-s1

# Install Python dependencies for the manager
sudo pip3 install --upgrade -r requirements.txt

echo "Installation complete"
