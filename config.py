# api_id = 11468489
# api_hash = 'a6741d6acd4709f9c866b3d8bfc50e4f'
from telethon import Button

sizes = {
    "144p":(256,144),
    "240p":(426 ,240),
    "360p":(480,360),
    "480p":( 720 , 480),
    "720p":(1280 ,720),
    "1080p":(1920 , 1080)

}

api_id = 10008026
api_hash = "902f2165d6076ea281fc889175052d3f"
keyboard = [
    [
        Button.inline("144p",data="144p"),
        Button.inline("240p", data="240p")
    ],
    [
        Button.inline("360p", data="360p"),
        Button.inline("480p", data="480p")
    ],
    [
        Button.inline("720p",data="720p"),
        Button.inline("1080p",data="1080p"),
    ]
]