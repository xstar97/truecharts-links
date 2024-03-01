#!/bin/bash

# Clone the repository from GitHub into a temporary directory
git clone https://github.com/xstar97/go-littlelinks-generator.git temp

# Run the go-littlelinks-generator project
go run temp/cmd/main.go --assets-path assets/ --config links.json

# Copy the build directory to the root directory
cp -r temp/build /build

# Clean up temporary directory
rm -rf temp
