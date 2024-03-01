#!/bin/bash

# Clone the repository from GitHub into a temporary directory
git clone --depth=1 https://github.com/xstar97/go-littlelinks-generator.git temp_dir

# Copy the files from the output directory to the current directory
cp -r temp_dir/output/* /

# Run the littlelink-generator with the specified parameters
./littlelink-generator --assets-path assets/ --config links.json

# Clean up temporary directory
rm -rf temp_dir