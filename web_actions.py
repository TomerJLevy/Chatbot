import webbrowser

web_searces = {"youtube" : 'https://www.youtube.com/results?search_query=%s',
               "google" : 'http://www.google.com/search?btnG=1&q=%s',
               "stackoverflow" : 'https://stackoverflow.com/search?q=%s', 
               "rtc" : "rtc.com", }
               
web_sites = {"sport" : 'https://www.sport5.co.il',
             "news" : 'https://www.ynet.co.il',
             "ynet" : 'https://www.ynet.co.il',
             "geektime" : 'https://www.geektime.co.il',
             "themarker" : 'https://www.themarker.co.il',
             "facebook" : 'https://www.facebook.com'}
             
web_actions = list(web_searces.keys()) + list(web_sites.keys())

def open_url(url):
    webbrowser.open_new_tab(url)

def search_url(url, search):
    open_url(url % search)
