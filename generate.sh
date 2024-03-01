#!/bin/bash

# Clone the repository from GitHub into a temporary directory
git clone https://github.com/xstar97/go-littlelinks-generator.git temp

cp temp/output/littlelink-generator ./
# Run the go-littlelinks-generator project
./littlelink-generator --asset-path "assets/" --config "links.json"

# Clean up temporary directory
rm -rf temp
