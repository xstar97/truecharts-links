#!/bin/bash

# Clone the repository from GitHub into a temporary directory
git clone --depth=1 https://github.com/xstar97/go-littlelinks-generator.git .

# Run the littlelink-generator with the specified parameters
go run cmd/main.go --assets-path assets/ --config links.json
