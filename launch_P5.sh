#!/bin/bash

# This script will activate the P5 conda environment and launch
# the P5_advanced_lane_finding.ipynb jupyter notebook:


# Determine if the platform is Linux or macOS
platform='unknown'
platform=`uname -s`

# Save correct paths based on platform
if [[ "$platform" == 'Linux' ]]; then
   platform='linux'
   project_dir="/home/ty/Udacity/T1/P5_vehicle_detection_and_tracking"
   conda_activate="/home/ty/anaconda3/bin/activate"

elif [[ "$platform" == 'Darwin' ]]; then
   platform='darwin'
   project_dir="/Users/ty/Udacity/T1/P5_vehicle_detection_and_tracking"
   conda_activate="/Users/ty/anaconda3/bin/activate"
   
fi

# # Print out path variables
# echo $platform
# echo $project_dir
# echo $conda_activate

# Go to the project directory
cd $project_dir

# Activate the "P5" anaconda environment
source $conda_activate P5

# Launch the P5 jupyter notebook
jupyter notebook P5_vehicle_detection_and_tracking.ipynb

