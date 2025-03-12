from pytube import YouTube
import os

def progress_callback(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    percent_complete = (total_size - bytes_remaining) / total_size * 100
    tqdm.write(f"Downloading: {percent_complete:.2f}%")

def download_video(url, save_path, resolution="highest", audio_only=False):
    try:
        yt = YouTube(url)

        if audio_only:
            stream = yt.streams.filter(only_audio=True).first()
        else:
            if resolution == "highest":
                stream = yt.streams.get_highest_resolution()
            else:
                stream = yt.streams.filter(res=resolution, progressive=True).first()

        if stream:
            stream.download(output_path=save_path)
            return f"Download complete: {os.path.join(save_path, stream.default_filename)}"
        else:
            return "No suitable stream found."

    except Exception as e:
        return f"Error: {str(e)}"

def download_playlist(url, save_path):
    try:
        playlist = Playlist(url)
        for video in playlist.videos:
            video.streams.get_highest_resolution().download(output_path=save_path)
        return "Playlist Download Complete!"
    except Exception as e:
        return f"Error: {str(e)}"
