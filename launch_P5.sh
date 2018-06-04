#!/bin/bash

# This script will activate the P5 conda environment and launch
# the P5_advanced_lane_finding.ipynb jupyter notebook:

cd "/home/ty/Udacity/T1/P5_vehicle_detection_and_tracking"
source "/home/ty/anaconda3/bin/activate" P5
jupyter notebook P5_vehicle_detection_and_tracking.ipynb

