from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs
import re
def get_id_of_videos(home_link):
    #home_link = "https://www.youtube.com/user/zeemusiccompany/videos"
    html = uReq(home_link)
    #beutified_page = bs(html.read(),"html.parser")
    html_result = html.read().decode()
    print(html.read().decode())
    """ Getting video links """
    #v = re.findall(r"watch\?v=(\S{11})",beutified_page.decode())
    v = re.findall(r"watch\?v=(\S{11})",html_result)
    return v
#print(len(v))
#print(v[0])
#link = "https://www.youtube.com/watch?v="+v[0]
#print(link)