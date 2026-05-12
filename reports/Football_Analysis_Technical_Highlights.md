# Football Analysis Technical Highlights

- End-to-end sports analytics video pipeline implemented in Python.
- Custom-trained YOLO detector saved as models/best.pt.
- Team assignment built from KMeans clustering on jersey color crops.
- Camera motion compensation implemented with Lucas-Kanade optical flow.
- Perspective transform maps player movement into approximate field coordinates.
- Speed and cumulative distance are rendered directly onto output frames.
- Per-video stub caching reduces repeated detector and motion computation.