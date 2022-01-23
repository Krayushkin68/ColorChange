# ColorChange
Application for determining the primary colors of the image and replacing them with the selected ones.
## Idea
The idea is to replace the main color palette of the image with the given colors.
## Implementation
Implemented by determining a given number of primary colors of the image using the k-means method, followed by random replacement of several of the primary colors with the specified ones, by shifting their color tone in the HSV model in a given direction (to preserve color transitions).
## Used technologies
*Language*: Python

*Libraries*: PySide2, numpy, opencv-python
## Example
![color_change](https://user-images.githubusercontent.com/71232265/150681953-a1117587-7e22-43ed-afad-1c735f4a1a56.gif)
