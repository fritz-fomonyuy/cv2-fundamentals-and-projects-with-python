import cv2

image_path = r"/home/agent-47/Pictures/IMG_20230102_165433_607.jpg"
image = cv2.imread(image_path)
"""add image in working space then display 
image """
# cv2.imshow("sample-image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

directory=r"/home/agent-47/Pictures/pic.jpg"
cv2.imwrite(directory,image)
print("image saved succesfully")