## Vehicle Detection and Tracking

**Vehicle Detection Project**

The goals / steps of this project are the following:

* Perform a Histogram of Oriented Gradients (HOG) feature extraction on a labeled training set of images and train a classifier Linear SVM classifier
* Optionally, you can also apply a color transform and append binned color features, as well as histograms of color, to your HOG feature vector.
* Note: for those first two steps don't forget to normalize your features and randomize a selection for training and testing.
* Implement a sliding-window technique and use your trained classifier to search for vehicles in images.
* Run your pipeline on a video stream (start with the test_video.mp4 and later implement on full project_video.mp4) and create a heat map of recurring detections frame by frame to reject outliers and follow detected vehicles.
* Estimate a bounding box for vehicles detected.

[//]: # (Image References)
[image1]: ./writeup_images/image1.png
[image2]: ./writeup_images/image2.png
[image3]: ./writeup_images/image3.png
[image4]: ./writeup_images/image4.png
[image5]: ./writeup_images/image5.png
[image6]: ./writeup_images/image6.png
[image7]: ./writeup_images/image7.png
[video1]: ./project_video_out.mp4



## [Rubric](https://review.udacity.com/#!/rubrics/513/view) Points
### Here I will consider the rubric points individually and describe how I addressed each point in my implementation.

---
### Writeup / README

#### 1. Provide a Writeup / README that includes all the rubric points and how you addressed each one.  You can submit your writeup as markdown or pdf.  [Here](https://github.com/udacity/CarND-Vehicle-Detection/blob/master/writeup_template.md) is a template writeup for this project you can use as a guide and a starting point.

You're reading it!

### Histogram of Oriented Gradients (HOG)

#### 1. Explain how (and identify where in your code) you extracted HOG features from the training images.

The code for this step is contained in the 6th code cell of the Jupyter Notebook.

I started by reading in all the `vehicle` and `non-vehicle` images from the dataset.  Here is an example of one of each of the `vehicle` and `non-vehicle` images:

![alt text][image1]

I then explored different color spaces and different `skimage.hog()` parameters (`orientations`, `pixels_per_cell`, and `cells_per_block`).  I grabbed random images from each of the two classes and displayed them to get a feel for what the `skimage.hog()` output looks like.

Here is an example using the `YCrCb` color space and HOG parameters of `orientations=8`, `pixels_per_cell=(8, 8)` and `cells_per_block=(2, 2)`:


![alt text][image2]

#### 2. Explain how you settled on your final choice of HOG parameters.

I tried various combinations of different HOG parameters.  `RGB` color space did not work well.  `YCrCb` and `LUV` both produced good results.  I ended up going with all 3 channels of YCrCb because it worked the best.  I noticed minimal improvement by upping the recomended number of orientations from 9 to 12, but no better results from 12 to 15.  Aside from that;
8 pixels per cell and 2 cells per block yielded good enough accuracy, so I did not change them.

#### 3. Describe how (and identify where in your code) you trained a classifier using your selected HOG features (and color features if you used them).

The code for this step is contained in the 8th and 9th code cells of the Jupyter Notebook.

I trained a linear SVM using HOG, spatial, and color histogram features.  I chose to use the color based features to try and maximize the accuracy of the SVM.  (Although I was able to achieve better than 90% accuracy using HOG features only.).  About 8,000 images were used to train the SVM.  For each image, the 3 feature vectors (spatial, histogram, and HOG) were concatenated to form a single vector.  The single feature vectors were then scaled using the `StandardScaler()` from the scikit-learn library.  80% of the total data was used to train while 20% was set aside for testing.  The trained SVM had an accuracy of 99.69%.  The trained SVM and other parameters were saved in a pickle file (`svc_data.p`) for easy re-use of previously trained SVMs.

### Sliding Window Search

#### 1. Describe how (and identify where in your code) you implemented a sliding window search.  How did you decide what scales to search and how much to overlap windows?

The code for this step is contained in the 10th code cell of the Jupyter Notebook.

I decided to search each image/frame using only 2 different sets of `scale`, `ymin`, and `ymax` values.  Adding more seemed to increase the number of false-positives found to the point where they became very difficult to filter out.  I tried scale sizes ranging from 0.9-1.5 (by 0.1s) and determined that 1.4 seemed to work the best. A 75% overlap amount seemed to work well; I did not try other overlap amounts.

![alt text][image3]

#### 2. Show some examples of test images to demonstrate how your pipeline is working.  What did you do to optimize the performance of your classifier?

Here are some examples of my pipeline on some test images.  To optimise the performance of the classifier, I added another scale of 1.5 mainly to increase the number of detections for each car which allowed me to increase the heat map threshold which helped filter out false-positives.  I experimented with more `scale` layers but ultimately decided to stay with two.

![alt text][image4]
---

### Video Implementation

#### 1. Provide a link to your final video output.  Your pipeline should perform reasonably well on the entire project video (somewhat wobbly or unstable bounding boxes are ok as long as you are identifying the vehicles most of the time with minimal false positives.)
Here's a [link to my video result](./project_video_out.mp4)


#### 2. Describe how (and identify where in your code) you implemented some kind of filter for false positives and some method for combining overlapping bounding boxes.

The code for this step is contained in the 11th code cell of the Jupyter Notebook.

I used a heatmap to add 'weight' to each overlapping detection.  False positives were filtered out of the heatmap by adding a minimum heat threshold of 2.  The detected cars were recorded over time (from frame to frame) using methods from the `Vehicle` class.  Areas in the video that were detected over several frames were weighed more heavily in the final output bounding boxes.  The `scipy.ndimage.measurements.label()` method was used to combine 'hot spots' into single bounding boxes.

Here's an example showing the heatmaps from a series of frames of video, the result of `scipy.ndimage.measurements.label()` and the bounding boxes then overlaid on the last frame of video:

### Here are six frames and their corresponding heatmaps:

![alt text][image5]

### Here is the output of `scipy.ndimage.measurements.label()` on the integrated heatmap from all six frames:
![alt text][image6]

### Here the resulting bounding boxes are drawn onto the last frame in the series:
![alt text][image7]


---

### Discussion

#### 1. Briefly discuss any problems / issues you faced in your implementation of this project.  Where will your pipeline likely fail?  What could you do to make it more robust?

One difficulty I faced was dealing with slow extracting/SVM training times.  To help speed the process along, I added the ability to store trained SVMs in a pickled file.  That way I could train several different versions of the SVM, each one using different parameters, and then easily and quickly re-use the different versions without having to waste time.

My pipeline will likely fail by producing too many false positives.  This might be helped by adding more `scale` layers that are individually more strict, but that together still produce enough detections to find and keep all the cars in the video.  Also, recording and inferring more information about each detection might help.
