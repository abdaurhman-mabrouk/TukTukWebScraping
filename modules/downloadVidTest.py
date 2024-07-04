import yt_dlp


# URL of the video from any supported platform
videoUrl = input("Enter The Video URL: ")

# The Video Save Path
savePath = input("Enter The Video Path: ")


def download_video(url, save_path="."):
    ydl_opts = {
        "format": "best",  # Download the best quality format available
        "outtmpl": f"{save_path}/%(title)s.%(ext)s",  # Save the file in the specified path
        "postprocessors": [
            {
                "key": "FFmpegVideoConvertor",
                "preferedformat": "mp4",  # Convert to mp4 after download
            }
        ],
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("Download completed!")
    except Exception as e:
        print(f"Error: {e}")


# Call The Function to Download The Video
download_video(videoUrl, savePath)
