#!/bin/bash

# Set compiler and flags
CXX=g++
CXXFLAGS="-Wall -g"  # Adjust flags as needed

# Define apps directory
APPS_DIR="apps"

# Build directory (absolute path)
BUILD_DIR="/path/to/root/build"  # Replace with actual path

# Check if apps directory exists
if [ ! -d "$APPS_DIR" ]; then
  echo "Error: Directory '$APPS_DIR' not found!"
  exit 1
fi

# Check if build directory exists
if [ ! -d "$BUILD_DIR" ]; then
  echo "Creating build directory: $BUILD_DIR"
  mkdir -p "$BUILD_DIR"
fi

# Compile all .cpp files in apps directory
for file in "$APPS_DIR"/*.cpp; do
  # Extract filename without extension
  filename="${file%.*}"

  # Compile the file
  $CXX $CXXFLAGS -c "$file" -o "$APPS_DIR/$filename.o"

  # Check for compilation errors (optional)
  if [ $? -ne 0 ]; then
    echo "Error: Compilation failed for '$file'"
    exit 1
  fi

  # Move the compiled file to build directory
  mv "$APPS_DIR/$filename.o" "$BUILD_DIR/$filename.o"

  # Check if move was successful (optional)
  if [ $? -ne 0 ]; then
    echo "Error: Moving '$filename.o' to build directory failed!"
    exit 1
  fi
done

echo "Compiled all C++ files in '$APPS_DIR'"
echo "Object files placed in: $BUILD_DIR"
