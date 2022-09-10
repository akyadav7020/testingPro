from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs
from get_video_link_from_home import get_id_of_videos
from pro import youtubescraper
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests

app = Flask(__name__)
def main():
    ch_link = "https://www.youtube.com/user/zeemusiccompany/videos"
    video_id = get_id_of_videos(ch_link)
    for i in range(3):
        video_link,title, thumbnail_url = youtubescraper(video_id[i])
        print(str(i+1)+". "+title)
        print(video_link)
        print(thumbnail_url)

main()

def test():
    #print(link)
    specific_video_page = uReq(link)
    soup = bs(specific_video_page, 'html.parser').body#.decode()
    #print(soup)
    div_bs4 = soup.find('ytd-app')#, id="watch7-content")
    print(type(div_bs4))
    print(div_bs4)





