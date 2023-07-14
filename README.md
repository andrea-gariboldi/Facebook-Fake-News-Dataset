# Facebook Fake News Dataset
This is a dataset composed of 4934 posts taken from Facebook. Facebook Scraper (https://pypi.org/project/facebook-scraper/) was used to retrieve the data.
It is divided into two parts to make it easier to divide between news taken from reliable and unreliable pages.
## Data Source
This is the list of Facebook pages whence the posts are taken.
### Reliable Pages
- FactCheck.org (https://www.facebook.com/factcheck.org) 
- PolitiFact (https://www.facebook.com/politifact) 
- snopes.com (https://www.facebook.com/snopes) 
- RealClearPolitics (https://www.facebook.com/realclearpolitics)
- The New York Times (https://www.facebook.com/nytimes)
- The Guardian (https://www.facebook.com/theguardian) 
- The Wall Street Journal (https://www.facebook.com/WSJ)
- Daily Mail (https://www.facebook.com/DailyMail) 
- USA Today (https://www.facebook.com/usatoday) 
- BBC News (https://www.facebook.com/bbcnews)
- The Independent (https://www.facebook.com/TheIndependentOnline)
- Metro (https://www.facebook.com/MetroUK)

### Unreliable Pages
- The Onion (https://www.facebook.com/TheOnion) 
- The Daily Mash (https://www.facebook.com/thedailymash) 
- ClickHole (https://www.facebook.com/clickhole/) 
- NewsThump (https://www.facebook.com/NewsThump) 
- Waterford Whispers News (https://www.facebook.com/WhispersNews) 
- The Beaverton (https://www.facebook.com/TheBeaverton) 
- The Shovel (https://www.facebook.com/TheShovelAU) 
- The Babylon Bee (https://www.facebook.com/TheBabylonBee)
- The Chaser (https://www.facebook.com/thechaser)
- The Betoota Advocate (https://www.facebook.com/betootaadvocate) 
- The Poke (https://www.facebook.com/PokeHQ)
- Weekly World News(https://www.facebook.com/weeklyworldnews)
- GomerBlog (https://www.facebook.com/GomerBlog)

## File type and Post structure
The files are in JSON format.
Each post will be like: 

`{
    "post_id": "10161293017194497",
    "text": "THEONION.COM\nOminous New Report Just Lists Places To Hide",
    "post_text": "",
    "shared_text": "THEONION.COM\nOminous New Report Just Lists Places To Hide",
    "original_text": null,
    "time": "02/05/2023",
    "timestamp": 1683041406,
    "image": null,
    "image_lowquality": "https://external-mxp2-1.xx.fbcdn.net/emg1/v/t13/11897892201848054075?url=https%3A%2F%2Fi.kinja-img.com%2Fgawker-media%2Fimage%2Fupload%2Fc_fill%2Cf_auto%2Cfl_progressive%2Cg_center%2Ch_675%2Cpg_1%2Cq_80%2Cw_1200%2F1bc2ccfb6ea317f202484e462e4d5fcf.jpg&fb_obo=1&utld=kinja-img.com&stp=c0.5000x0.5000f_dst-jpg_flffffff_p476x249_q75&ccb=13-1&oh=06_AbH2WtP5pj6MI1s-kCedv7_KHNd0IVNCgn-0xKJlJuxy_Q&oe=645328FA&_nc_sid=6ac203",
    "images": [],
    "images_description": [],
    "images_lowquality": [
        "https://external-mxp2-1.xx.fbcdn.net/emg1/v/t13/11897892201848054075?url=https%3A%2F%2Fi.kinja-img.com%2Fgawker-media%2Fimage%2Fupload%2Fc_fill%2Cf_auto%2Cfl_progressive%2Cg_center%2Ch_675%2Cpg_1%2Cq_80%2Cw_1200%2F1bc2ccfb6ea317f202484e462e4d5fcf.jpg&fb_obo=1&utld=kinja-img.com&stp=c0.5000x0.5000f_dst-jpg_flffffff_p476x249_q75&ccb=13-1&oh=06_AbH2WtP5pj6MI1s-kCedv7_KHNd0IVNCgn-0xKJlJuxy_Q&oe=645328FA&_nc_sid=6ac203"
    ],
    "images_lowquality_description": [
        null
    ],
    "video": null,
    "video_duration_seconds": null,
    "video_height": null,
    "video_id": null,
    "video_quality": null,
    "video_size_MB": null,
    "video_thumbnail": null,
    "video_watches": null,
    "video_width": null,
    "likes": null,
    "comments": 7,
    "shares": 8,
    "post_url": "https://facebook.com/TheOnion/posts/10161293017194497",
    "link": "https://bit.ly/41TE5OX?fbclid=IwAR0p9g8CC8HyiLz_ZiBIAPVVhgqmegw2qGJpYtIFzVsYZPGD0eKHpZ7RmB4",
    "links": [
        {
            "link": "/story.php?story_fbid=pfbid09CRhiYQWa1MM7qf9jdSmpd8cpzK7tUFDj1KxusYP7cpV8XdTfamZ9mTbbu3Auwm6l&id=20950654496&eav=AfYBvYeQ1_1nxuIeU7FkKK-TGFmXbxqxDMC4arFb6bZ-vfnFYds5gDPmNAcovS9HqtU&m_entstream_source=timeline&__tn__=%2As%2As-R&paipv=0",
            "text": ""
        },
        {
            "link": "https://lm.facebook.com/l.php?u=https%3A%2F%2Fbit.ly%2F41TE5OX%3Ffbclid%3DIwAR0p9g8CC8HyiLz_ZiBIAPVVhgqmegw2qGJpYtIFzVsYZPGD0eKHpZ7RmB4&h=AT24f_5wemx2-vpVuNDB90yhgYLS8f57yhHNN0-QzI3tqibMvrWtPUhS23pa75FPIpJHRPuGhzf5hwxIx_u1EauEsGyLi6dh3IItLWj1YYCf8L0IF9NBQQFzNs1fvrHSySoirR2ibfbiz6umVlN8rITqHtCM7T08fRwWiC4O5Pzl",
            "text": ""
        }
    ],
    "user_id": "20950654496",
    "username": "The Onion",
    "user_url": "https://facebook.com/TheOnion/?__tn__=C-R&paipv=0&eav=AfZ8PVrtft0bjWYDDS9ShmFJMM0_tMguQD0eBlhRnQsu60ivb5fUz-hE7hDoPTjDX3s",
    "is_live": false,
    "factcheck": null,
    "shared_post_id": null,
    "shared_time": null,
    "shared_user_id": null,
    "shared_username": null,
    "shared_post_url": null,
    "available": true,
    "comments_full": null,
    "reactors": [],
    "w3_fb_url": "https://www.facebook.com/TheOnion/posts/10161293017194497",
    "reactions": {
        "like": 40,
        "love": 1,
        "ahah": 15,
        "wow": 2,
        "hug": 3
    },
    "reaction_count": 61,
    "with": null,
    "page_id": "20950654496",
    "sharers": null,
    "image_id": null,
    "image_ids": [],
    "was_live": false,
    "fetched_time": "02/05/2023"
}`

For each post is saved a lot of information, the main characteristics are :
- post_id: uniquely identifies each post;
- username: name of the page that posted;
- text: post’s text;
- time: post publication date;
- reaction_count: total number of reaction (do we really need it? Consider it can be calculated as a sum of each reaction);
- reaction: JSON object containing the values of each reaction;
- shares: number of post shares;
- comments: number of post comments;
