#!/bin/bash

# Download the latest release zip file from GitHub
wget -q https://github.com/xstar97/go-littlelinks-generator/releases/latest/download/go-littlelinks-generator.zip

# Unzip the downloaded file into the root directory
unzip -q go-littlelinks-generator.zip -d .

# Copy the output/littlelink-generator to the current directory
cp /output/littlelink-generator .

# Run the littlelink-generator with the specified parameters
./littlelink-generator --assets-path assets/ --config links.json
