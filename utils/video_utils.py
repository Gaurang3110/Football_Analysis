import cv2

def read_video(path, resize_width=None, max_frames=None):
    cap = cv2.VideoCapture(path)
    frames = []
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if resize_width is not None and frame.shape[1] > resize_width:
            aspect_ratio = frame.shape[0] / frame.shape[1]
            resized_height = int(resize_width * aspect_ratio)
            frame = cv2.resize(frame, (resize_width, resized_height))

        frames.append(frame)
        frame_count += 1

        if max_frames is not None and frame_count >= max_frames:
            break

    cap.release()
    return frames

def save_video(output_video_frames , output_video_path):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, 24.0, (output_video_frames[0].shape[1], output_video_frames[0].shape[0]))
    for frame in output_video_frames:
        out.write(frame)
    out.release()





