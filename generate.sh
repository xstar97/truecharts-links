#!/bin/bash

# Clone the repository from GitHub into the current directory
git clone https://github.com/xstar97/go-littlelinks-generator.git .

# Copy the files from the output directory to the parent directory
cp -r output/* ./

# Run the littlelink-generator with the specified parameters
./littlelink-generator --assets-path assets --config links.json
