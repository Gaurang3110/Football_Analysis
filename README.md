This project focuses on tracking football players, referees, and the ball in match videos using a trained YOLOv5 object detection model. It enhances analysis by combining several computer vision techniques to extract useful metrics and insights from game footage.

Football Player Tracking and Analysis using YOLO -:

This project focuses on tracking football players, referees, and the ball in match videos using a trained YOLOv5 object detection model. It enhances analysis by combining several computer vision techniques to extract useful metrics and insights from game footage.

Players are automatically assigned to teams based on their jersey colors using KMeans clustering for pixel segmentation. With this, the system calculates each team’s ball possession percentage during the match.

To account for camera movement, optical flow is used to estimate frame-by-frame motion, ensuring accurate tracking of player positions. Perspective transformation is applied to map the field in real-world dimensions, enabling measurement of movement in meters instead of pixels.

Finally, the project calculates key performance metrics for each player, such as speed and total distance covered. These insights can be used for sports analytics, coaching, and performance review.

This end-to-end solution combines detection, tracking, classification, and real-world measurement — making it suitable for beginners and experienced developers alike.

Roboflow dataset used for training yolov5 - https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc/dataset/1

Key Features-:

Object Detection: YOLOv5 is used to detect players, referees, and the ball.

Team Classification: KMeans clustering segments t-shirt colors to assign players to teams.

Ball Possession: Calculates team-wise ball acquisition percentage during the match.

Camera Motion Estimation: Optical Flow estimates camera movement for better tracking accuracy.

Real-World Measurement: Perspective transformation enables movement tracking in meters.

Performance Metrics: Computes each player's speed and total distance covered.

Tech Stack -: Python 3.x

YOLOv5 (via Ultralytics)

OpenCV

NumPy

Matplotlib

Pandas

Supervision

KMeans (via scikit-learn)
