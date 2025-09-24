# ⚽ Football Player Tracking and Analysis using YOLO

This project focuses on tracking football players, referees, and the ball in match videos using a trained YOLOv5 object detection model. It enhances analysis by combining several computer vision techniques to extract useful metrics and insights from game footage.

---

## 🔧 How to Set Up and Run the Code

1.  **Install Requirements** Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    (Make sure you have Python 3.x installed.)

2.  **Prepare Your Folders**

    * Create a folder named `models/`
    * Create folders named `input_videos/` and `output_videos/`

3.  **Add Your Input Video**

    * Place your football match video inside the `input_videos/` folder.

4.  **Train the YOLOv5 Model**

    * Open and run the notebook:
        ```bash
        training/football_training_yolo_v5.ipynb
        ```
    * It will generate `best.pt` model file. (As seen in `image_46ca9d.png`, this involves training the model with specified `batch_size` and `epochs`, and using `validation_data` for monitoring performance.)

5.  **Move the Trained Model**

    * Place `best.pt` inside the `models/` directory.

6.  **Run the Main Script**

    ```bash
    python main.py
    ```
    The processed output video will be saved in the `output_videos/` folder.

---

## 📄 Dependencies or Environment Requirements

* Python 3.x
* YOLOv5
* OpenCV
* NumPy
* Matplotlib
* Pandas
* Supervision
* scikit-learn (for KMeans clustering)

---

## 🧠 Project Approach and Methodology

### Detection
Used YOLOv5 to detect:
* Players
* Referees
* Football

### Team Classification
KMeans clustering on jersey colors for team assignment.

### Ball Possession Calculation
Analyzed frame-by-frame ball proximity to estimate team-wise possession.

### Camera Motion Estimation
Applied Optical Flow (Lucas-Kanade) to compensate for moving camera.

### Real-World Mapping
Perspective transformation to convert pixels to meters.

### Player Metrics
Calculated:
* Speed
* Distance covered
    for each player.

---

## 🛠 Techniques Tried and Outcomes

* **YOLOv5** for object detection.
* **KMeans Clustering** for team identification.
* **Optical Flow (Lucas-Kanade)** for camera motion compensation.
* **Homography / Perspective Transformation** for real-world mapping.
* **Custom Tracker** for frame-wise identity matching and stats.

### Model Evaluation Metrics
* **Root Mean Squared Error (RMSE):** Calculated after model prediction to evaluate regression performance. (Example shown in `image_46c6ff.png` with a reported RMSE of `0.888`.)
* **Mean Absolute Percentage Error (MAPE):** Another metric used to assess prediction accuracy. (Example shown in `image_46c6db.png` with a reported MAPE of `0.271`.)
* **Model Loss Plotting:** Visualizing the training and validation loss over epochs to monitor model convergence and identify overfitting (`image_46c6db.png`).

---

## 🚧 Challenges Encountered

* Jersey color clustering sensitive to lighting conditions.
* Optical flow required careful tuning for smooth stabilization.
* Maintaining identity in crowded scenes was difficult. (As per `image_07dbde.png`, specific instructions include "Assign player IDs based on the initial few seconds" and "Maintain the same ID for players when they re-enter the frame later in the video (near the goal event)", simulating real-time re-identification and tracking.)
* Limited labeled data affected model generalization.

---

## 🚀 Future Work

With additional time/resources:

* Add advanced tracking algorithms like Deep SORT or ByteTrack.
* Use semantic segmentation for better player segmentation.
* Enhance ball possession logic based on player proximity and control.
* Build an interactive dashboard for visualization and analysis.

---

## 📦 Dataset


 [Roboflow Football Players Detection Dataset](https://universe.roboflow.com/ds/your-dataset-link-here) 

---

## ✨ Key Features

* **Object Detection** – YOLOv5 to detect players, referees, and the ball.
* **Team Classification** – KMeans based on t-shirt colors.
* **Ball Possession Estimation** – Match-time statistics for both teams.
* **Camera Motion Estimation** – Optical Flow tracking.
* **Real-World Mapping** – Perspective transform to measure in meters.
* **Performance Metrics** – Speed and distance for each player.

### User-Based Movie Recommendation System (Conceptual Integration)
(While the core project is about football tracking, some provided images (`image_46bbb6.png`, `image_46b8f0.png`, `image_46b819.png`, `image_46b4f3.png`, `image_46b457.png`) suggest a secondary or conceptual component related to movie recommendations. This section outlines how such a system, if part of the broader project or an example of a related skill, would function.)
* **User Preferences Input:** Allows a new user to rate a selection of initial movies (e.g., 'Mrs. Doubtfire', 'Dumb & Dumber', 'Ace Ventura: Pet Detective', 'Home Alone') to establish their taste (`image_46bbb6.png`).
* **Finding Similar Users:** Identifies other users who have rated common movies, providing a count of such users (e.g., `1466` as seen in `image_46b8f0.png`).
* **Similarity Calculation:** Sorts users by the count of common movies and calculates Pearson Correlation Coefficient to determine similarity between the new user and existing users based on their shared ratings (`image_46b819.png`).
* **Top Similar Users:** Identifies and ranks top similar users based on their similarity index (`image_46b819.png`).
* **Weighted Rating Aggregation:** Merges similar user data with movie ratings and calculates a 'Weighted Rating' for each movie by multiplying the user's rating by their similarity index (`image_46b4f3.png`).
* **Recommendation Generation:** Computes an average recommendation score for movies based on weighted ratings and recommends movies with high scores (e.g., an average score of `5`), sampling a specified number of recommendations (`image_46b457.png`).

---

## 🧰 Tech Stack

* Python 3.x
* YOLOv5 (Ultralytics)
* OpenCV
* NumPy
* Matplotlib
* Pandas
* Supervision
* scikit-learn (KMeans)
