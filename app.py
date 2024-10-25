from flask import Flask, request, send_file, Response
import os
import tempfile
from moviepy.editor import ImageSequenceClip, AudioFileClip

app = Flask(__name__)

# Default paths for images, audio, and video
DEFAULT_IMAGE_FOLDER = "C:/Users/sunny/OneDrive/Desktop/img fldr"
DEFAULT_AUDIO_FILE = "C:/Users/sunny/OneDrive/Desktop/WhatsApp Audio 2024-10-25 at 11.40.26_643c8c5c.mp3"

def get_files(folder_path, extensions):
    """Returns a sorted list of image file paths in the given folder."""
    return sorted(
        [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith(extensions)]
    )

def create_video_with_music(image_folder, audio_file, output_video, fps=1, mute_audio=False):
    """Creates a video from images in `image_folder` with optional `audio_file`."""
    images = get_files(image_folder, ('.png', '.jpg', '.jpeg'))
    
    if not images:
        return "No valid images found in the specified folder."
    
    # Check if output path is valid and has a valid extension
    if not output_video.endswith(('.mp4', '.mov', '.avi')):
        return "Error: Please provide a valid output video file path with a .mp4, .mov, or .avi extension."

    try:
        clip = ImageSequenceClip(images, fps=fps)

        if not mute_audio:
            # Load and set the audio file, checking its path first
            if not os.path.exists(audio_file):
                return f"Error: Audio file not found at {audio_file}"

            audio_clip = AudioFileClip(audio_file)
            final_clip = clip.set_audio(audio_clip)
            final_clip = final_clip.subclip(0, min(clip.duration, audio_clip.duration))
        else:
            final_clip = clip

        # Create a temporary file for the output video
        with tempfile.NamedTemporaryFile(suffix='.avi', delete=False) as temp_file:
            temp_file.close()  # Close the file so moviepy can write to it
            final_clip.write_videofile(temp_file.name, codec="libx264", audio_codec="aac")
            return temp_file.name  # Return the temporary file name

    except Exception as e:
        return f"Error creating video: {e}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get parameters from the form
        image_folder = request.form.get("image_folder", DEFAULT_IMAGE_FOLDER)
        audio_file = request.form.get("audio_file", DEFAULT_AUDIO_FILE)
        output_video = request.form.get("output_video", "temp_output.avi")  # Use temp file name if needed
        fps = int(request.form.get("fps", 1))
        mute_audio = request.form.get("mute_audio") == "yes"

        # Create the video
        result = create_video_with_music(image_folder, audio_file, output_video, fps=fps, mute_audio=mute_audio)
        
        # Provide download link if video is successfully created
        if result.endswith('.avi'):
            return Response(
                f"<h1>Video created successfully: {result}</h1><a href='/download?file={result}'>Download Video</a>",
                mimetype="text/html"
            )
        else:
            return Response(f"<h1>{result}</h1><a href='/'>Go Back</a>", mimetype="text/html")

    return Response(f"""
        <h1>Video Generator</h1>
        <form method="POST" action="/">
            <label>Image Folder Path:</label><br>
            <input type="text" name="image_folder" value="{DEFAULT_IMAGE_FOLDER}"><br><br>

            <label>Audio File Path:</label><br>
            <input type="text" name="audio_file" value="{DEFAULT_AUDIO_FILE}"><br><br>

            <label>Output Video Path:</label><br>
            <input type="text" name="output_video" value="temp_output.avi"><br><br>

            <label>Frames per Second (FPS):</label><br>
            <input type="number" name="fps" value="1"><br><br>

            <label>Mute Audio:</label><br>
            <select name="mute_audio">
                <option value="no">No</option>
                <option value="yes">Yes</option>
            </select><br><br>

            <button type="submit">Create Video</button>
        </form>
    """, mimetype="text/html")

@app.route("/download")
def download():
    video_file = request.args.get("file")
    return send_file(video_file, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
