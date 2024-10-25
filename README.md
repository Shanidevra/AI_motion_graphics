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

# Setup Instructions

## Create a Project Directory: 
Create a new directory for your project:
## Create the Application File:
Create a new Python file (e.g., app.py) and copy the provided Flask code into this file.
## Configure Default Paths:
Update the default paths for the image folder and audio file in the code if necessary. Make sure these directories exist and contain valid images and audio files.
## Run the Application:
Open a terminal or command prompt in your project directory and run:
- python app.py
This will start the Flask development server.
## Access the Application: 
Open your web browser and navigate to http://127.0.0.1:5000/. You will see the video generator form.
## Use the Application: 
Fill in the form with the appropriate paths and options, then click "Create Video" to generate your video.

# Notes
Ensure that you have permission to read the image and audio files and write to the output location.
If you encounter any permission issues, consider changing the output file path to a directory where you have write access (e.g., your user’s Documents or Desktop folder).
