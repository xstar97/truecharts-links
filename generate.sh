#!/bin/bash

# Clone the repository from GitHub into a temporary directory
git clone https://github.com/xstar97/go-littlelinks-generator.git temp

ls temp
cp temp/output/littlelink-generator ./
# Run the go-littlelinks-generator project
./littlelink-generator --asset-path "assets/" --config "links.json"

# Copy the build directory to the root directory
cp -r temp/build/* /build/*

# Clean up temporary directory
rm -rf temp
