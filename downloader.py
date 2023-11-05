from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link, on_progress_callback=progress_func)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)

