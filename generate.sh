#!/bin/bash

# Clone the repository from GitHub
git clone --depth=1 https://github.com/xstar97/go-littlelinks-generator.git

# Navigate into the cloned directory
cd go-littlelinks-generator

# Build the project
go build

# Copy the littlelink-generator executable to the parent directory
cp littlelink-generator ..

# Navigate back to the parent directory
cd ..

# Run the littlelink-generator with the specified parameters
./littlelink-generator --assets-path assets --config links.json
