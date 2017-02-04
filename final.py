# final.py
# Created by @DonnersYT - www.github.com/donnersyt

import requests
import json
import random
import time
import string
import datetime

def log(event):
    print(datetime.datetime.now().strftime("%H:%M:%S") + " - " + str(event))
def main(kount):
    char_set = string.ascii_uppercase + string.digits
    randomstring = str(''.join(random.sample(char_set * 6, 6)))
    if kount == 0:
        log("Working...")
    s = requests.session()
    randemail = str(random.randint(1,99999999)) + str(random.getrandbits(128)) + str(random.randint(1,99999999)) + str(randomstring) + "@" + str(randdomain)
    postDict = {
        "signup[email]":randemail,
        "signup[share_hash]":invitecode,
        "subscribe":""
    }
    postRqst = s.post(posturl, data=postDict)
    if postRqst.status_code != 200:
        log("Failed creating this account " + str(postRqst.status_code))
    else:
        log("Success... " +str(kount+1) + "/" + str(numOfRefs))
        if (kount+1) == numOfRefs:
            time.sleep(2)

if __name__ == "__main__":
    posturl = "https://apply.getfinal.com/signups"
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
    except:
        log("config.json was not loaded.")
        quit()
    invitecode = config["setup"]["invite_code"]
    randdomain = config["setup"]["random_domain"]
    print("""


    Final.py loaded
    ----------------
    Invite Code: """+str(invitecode)+"""
    Email Domain: """+str(randdomain)+"""

    """)
    while True:
        try:
            numOfRefs = int(input("How many referrals would you like?  (use -1 for unlimited) :\t"))
            if numOfRefs == -1:
                numOfRefs = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            for kount in range(numOfRefs):
                main(kount)
        except ValueError:
            log("You must use an integer value for your referrals!")
            time.sleep(1)