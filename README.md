# Text_recognition
The code demonstrates the use of the pytesseract library in Python for text recognition from an image. 

In the first part of the code, the image is read and its dimensions are determined using the `shape` function from the OpenCV (cv2) library. The `image_to_boxes` function from pytesseract is then used to get the bounding boxes of each character in the image. These bounding boxes are then drawn on the image using the `rectangle` function from cv2 and labeled using the `putText` function.

In the second part of the code, the `image_to_data` function from pytesseract is used to get the bounding boxes and text for each word in the image. These boxes are then drawn on the image and labeled as in the first part.

Finally, the `image_to_string` function from pytesseract is used to get the entire text from the image, which is printed to the console.

# RESULT
<img src="https://github.com/asadbek002/Camera_Calibaration/blob/master/result_screenshot.jpg](https://github.com/asadbek002/Text_recognition/blob/main/result.png)" width="500" height="300">
