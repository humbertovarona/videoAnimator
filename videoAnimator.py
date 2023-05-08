m moviepy.editor import *

def create_video(image_dir, image_type, video_filename, duration, video_quality = 2740):
    image_files = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith('.' + image_type)]
    image_files.sort()
    frames = [ImageClip(image_file).set_duration(duration) for image_file in image_files]
    full_video_filename = os.path.join(image_dir, video_filename)
    video = concatenate_videoclips(frames)
    video.write_videofile(full_video_filename, fps=1 / duration, bitrate=f"{video_quality}k")
    
