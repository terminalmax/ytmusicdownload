import youtube_dl


def run(video_url):
    video_info = youtube_dl.YoutubeDL().extract_info(
        url=video_url, download=False
    )
    filename = f"{video_info['title']}.mp3"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': f"./output/{filename}",
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))


# URLS!
music = ['https://www.youtube.com/watch?v=jzc6VLu4AFY',
         'https://www.youtube.com/watch?v=9A0x7ljF1zs',
         'https://www.youtube.com/watch?v=vgd0bhAufXo']

notdownloaded = []

for url in music:
    try:
        run(url)
    except:
        notdownloaded.append(url)

print(f"Not downloaded : {notdownloaded}")
