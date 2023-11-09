from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link, on_progress_callback=progress_func)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("um erro ocorreu")
    print("Download Completo com Sucesso")


link = input("YouTube URL: ")
Download(link)

