# AI_motion_graphics
This Python application creates a video from a sequence of images and an optional audio file. The core functionality is defined in the create_video_with_music function, which generates a video using the MoviePy library.

# Key Components:
## Default Paths: 
The application sets default paths for the image folder and audio file.

## File Retrieval: 
The get_files function retrieves and sorts image files from the specified directory.

## Video Creation: 
The video is created by combining images and audio. If audio is muted, the video is generated without sound.

## Temporary File Handling: 
A temporary file is created to store the output video, ensuring that permissions issues are minimized.

## Web Interface: 
The main route (/) serves an HTML form where users can input paths for images and audio, specify frames per second, and choose whether to mute audio. Upon submission, the application processes the input and generates the video.

## Download Feature: 
A download link is provided for users to retrieve the created video file.

This application is useful for users looking to automate the process of creating videos from image sequences with audio accompaniment.
