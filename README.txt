This software contains a module to convert an image to RGB pixels.

System Requirement
==================
Tested on Mac OSX 10.11.4.

Python requirement
==================
Pyton 2.7
Requires models- PIL (pip install PIL)


Package Contents
================
`image2pixels.py`: contains image_to_pixels module

Input Format
============
An image file in any valid format. For example- everest.jpg, food.png

Output Format
=============
An array of size (height, width, 3) for JPEG or JPG.
An array of size (height, width, 3) for PNG if the metadata[‘alpha’] is false else array of size (height, width, 4).

To Run
======
Type the following command:
`python image2pixels.py`


Questions/Comments:
 email: dipendra.jha@eecs.northwestern.edu