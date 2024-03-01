#!/bin/bash

# Clone the repository from GitHub
git clone --depth=1 https://github.com/xstar97/go-littlelinks-generator.git ..


# Copy the littlelink-generator executable to the parent directory
cp output/littlelink-generator ..

# Run the littlelink-generator with the specified parameters
./littlelink-generator --assets-path assets --config links.json
