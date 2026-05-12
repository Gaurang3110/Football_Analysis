# Football Analysis Presentation Points

## 1. Problem
- Raw football videos are difficult to analyze manually frame by frame.

## 2. Solution
- This project automates detection, tracking, team assignment, possession estimation, and speed/distance overlays.

## 3. Core Pipeline
- Read video
- Detect objects with YOLO
- Track with ByteTrack
- Estimate camera motion
- Transform positions to pitch coordinates
- Compute speed, distance, and ball control
- Render annotated output video

## 4. Dataset
- Roboflow dataset URL: https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc/dataset/1
- Classes: ball, goalkeeper, player, referee

## 5. Technical Strengths
- Modular pipeline
- Uses standard CV/ML building blocks
- Supports per-video caching through stub pickle files

## 6. Current Limitations
- Memory-heavy on long videos
- Some hard-coded assumptions remain
- ByteTrack API warning in current supervision version