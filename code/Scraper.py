from facebook_scraper import *
import time
import datetime
import random
import json
print("Libraries imported")

#convert the date to String (JSON-supported date format)
def dateToString(dict):
    dict["time"] = dict["time"].strftime('%d/%m/%Y')
    dict["fetched_time"] = dict["fetched_time"].strftime('%d/%m/%Y')

set_cookies("cookies.txt") #login cookies

with open('dataset.json', 'a') as file: 
    while True:
        try:
            for post in get_posts('PageName', pages=10,start_url=start_url, extra_info = True, options={"posts_per_page": 100}):
                wait = random.randint(50, 60)
                time.sleep(wait)
                try:
                    dateToString(post)
                except Exception:
                    break
                try:
                    json.dump(post, file, indent=4)
                    file.write(',')
                    file.write('\n')
                    print("Inserted " + post['post_id'])
                except Exception as e:
                    print("There was an error by inserting ", post["post_id"])
                    print(e)
                    break
            break
        except exceptions.TemporarilyBanned:
            print("Too much scraping, sleeping for 10m")
            time.sleep(600)
file.close()          
print("Done scraping") 
