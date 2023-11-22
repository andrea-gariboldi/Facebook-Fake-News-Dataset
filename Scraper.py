{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9ae1290e-3a45-40d6-9bc7-78fd75a55a0e",
   "metadata": {},
   "outputs": [],
   "source": [
    "from facebook_scraper import *\n",
    "import time\n",
    "import datetime\n",
    "import random\n",
    "import json\n",
    "print(\"Libraries imported\")\n",
    "\n",
    "#convert the date to String (JSON-supported date format)\n",
    "def dateToString(dict):\n",
    "    dict[\"time\"] = dict[\"time\"].strftime('%d/%m/%Y')\n",
    "    dict[\"fetched_time\"] = dict[\"fetched_time\"].strftime('%d/%m/%Y')\n",
    "\n",
    "set_cookies(\"cookies.txt\") #login cookies\n",
    "\n",
    "with open('dataset.json', 'a') as file: \n",
    "    while True:\n",
    "        try:\n",
    "            for post in get_posts('PageName', pages=10,start_url=start_url, extra_info = True, options={\"posts_per_page\": 100}):\n",
    "                wait = random.randint(50, 60)\n",
    "                time.sleep(wait)\n",
    "                try:\n",
    "                    dateToString(post)\n",
    "                except Exception:\n",
    "                    break\n",
    "                try:\n",
    "                    json.dump(post, file, indent=4)\n",
    "                    file.write(',')\n",
    "                    file.write('\\n')\n",
    "                    print(\"Inserted \" + post['post_id'])\n",
    "                except Exception as e:\n",
    "                    print(\"There was an error by inserting \", post[\"post_id\"])\n",
    "                    print(e)\n",
    "                    break\n",
    "            break\n",
    "        except exceptions.TemporarilyBanned:\n",
    "            print(\"Too much scraping, sleeping for 10m\")\n",
    "            time.sleep(600)\n",
    "file.close()          \n",
    "print(\"Done scraping\") "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
