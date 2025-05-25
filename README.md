***FOOTBALL ANALYSIS***

This project focuses on tracking football players, referees, and the ball in match videos using a trained YOLOv5 object detection model. It enhances analysis by combining several computer vision techniques to extract useful metrics and insights from game footage.

***Football Player Tracking and Analysis using YOLO -:***

This project focuses on tracking football players, referees, and the ball in match videos using a trained YOLOv5 object detection model. It enhances analysis by combining several computer vision techniques to extract useful metrics and insights from game footage.

Players are automatically assigned to teams based on their jersey colors using KMeans clustering for pixel segmentation. With this, the system calculates each team’s ball possession percentage during the match.

To account for camera movement, optical flow is used to estimate frame-by-frame motion, ensuring accurate tracking of player positions. Perspective transformation is applied to map the field in real-world dimensions, enabling measurement of movement in meters instead of pixels.

Finally, the project calculates key performance metrics for each player, such as speed and total distance covered. These insights can be used for sports analytics, coaching, and performance review.

This end-to-end solution combines detection, tracking, classification, and real-world measurement — making it suitable for beginners and experienced developers alike.

Roboflow dataset used for training yolov5 - https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc/dataset/1

**Key Features-:**

Object Detection: YOLOv5 is used to detect players, referees, and the ball.

Team Classification: KMeans clustering segments t-shirt colors to assign players to teams.

Ball Possession: Calculates team-wise ball acquisition percentage during the match.

Camera Motion Estimation: Optical Flow estimates camera movement for better tracking accuracy.

Real-World Measurement: Perspective transformation enables movement tracking in meters.

Performance Metrics: Computes each player's speed and total distance covered.

**Tech Stack -:**

Python 3.x
YOLOv5 (via Ultralytics)
OpenCV
NumPy
Matplotlib
Pandas
Supervision


TO USE - 
1) create a models folder and also take input video
2) create a input_videos folder and put your input video there
3) Go to training\football_training_yolo_v5.ipynb and run that file
4) From there you will get best.pt model which is used in main
5) best.pt model is trained on Roboflow dataset given above on yolov5 model
6) then after doing the above steps - run the main.py file and your result will be stored into output_videos file



KMeans (via scikit-learn)
