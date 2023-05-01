from bs4 import BeautifulSoup
import requests
import schedule
import email_alert
import time
import json


def check_showing(movie_name):
    receiver_email = ['dominator2rule@gmail.com','shisantchhetri90@gmail.com','shisant@prixa.org']
    
    now_showing_url="https://api.qfxcinemas.com/api/public/NowShowing"
    now_showing_html_content = requests.get(now_showing_url, verify=False).text
    nowshowing = json.loads(now_showing_html_content)
    now_showing_movies = [movie['name'].lower() for movie in nowshowing['data']]
    
    comming_soon_url="https://api.qfxcinemas.com/api/public/ComingSoon"
    comming_soon_html_content = requests.get(comming_soon_url, verify=False).text
    commingsoon = json.loads(comming_soon_html_content)
    comming_soon_movies = [movie['name'].lower() for movie in commingsoon['data']]
    
    
    print(f'now_showing_movies: {now_showing_movies}')
    
    print(f'comming_soon_movies: {comming_soon_movies}')
        
    if movie_name in now_showing_movies:
        for email in receiver_email:
            email_alert.send_email(email)
    elif movie_name in comming_soon_movies:
        print('Doctor Strange in the Multiverse of Madness is still Pending')
    else:
        print("No Doctor Strange available in the cinema")
            
            
            
def job():
    movie_name = 'doctor strange in the multiverse of madness'
#     movie_name = 'mantra'
    print("Checking if movie is avialable....")
    check_showing(movie_name)
    

schedule.every(10).minutes.do(job)


while True:
    # running all pending tasks/jobs
    schedule.run_pending()
    time.sleep(20)