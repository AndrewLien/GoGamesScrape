#!/bin/bash
#author
#date           : 20191211
#description    : Installation of Google Chrome and Chromedriver
#notes          : This script must be performed by the root user ubuntu on each server.
#=======================================================================================================================

# Setup
cd # These functions can't be performed at some restricted locations. cd to home is safe.
sudo apt-get install libxss1 libappindicator1 libindicator7 -y

# Download current GoogleChrome
sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# Install GoogleChrome
sudo dpkg -i google-chrome*.deb
sudo apt-get install -f -y
sudo apt-get install unzip

# Find current GoogleChrome version... This will be used to download a compatible ChromeDriver
# example output: "Google Chrome 59.0.3071.115"... only "59.0.3071" desired
X=`google-chrome --version`
Y=${X:14:2}
VERSION=`curl https://chromedriver.chromium.org/downloads | grep -om 1 "${Y}\.[0-9]*\.[0-9]*\.[0-9]*" | head -n 1`

# Install compatible ChromeDriver based on GoogleChrome version
sudo wget -N https://chromedriver.storage.googleapis.com/${VERSION}/chromedriver_linux64.zip
sudo unzip chromedriver_linux64.zip
sudo chmod +x chromedriver

# Move and link ChromeDriver to correct directories (PATH)
sudo mv -f chromedriver /usr/local/share/chromedriver
sudo ln -s -f /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s -f /usr/local/share/chromedriver /usr/bin/chromedriver

# Cleanup installation files
sudo rm LATEST_RELEASE_*
sudo rm google-chrome*.deb
sudo rm chromedriver_linux64.zip
