#Final.py
###### By [DonnersYT](http://www.twitter.com/DonnersYT)
Python 3.X program to jump the GetFinal queue.

You will need to have  **Requests**,**PyOpenSSL** and **idna** installed for Python 3.X on your machine.


###Setup Instructions:
Run `git clone https://github.com/donnersyt/FinalCreditCard.git` in to
your terminal / command prompt.

After this, use `cd Final` to navigate to the folder.

Set up the config.json file...
* Find your Final invite code at [GetFinal](https://apply.getfinal.com)
* Optional: Enter a random domain for signups

To run, enter `python3 final.py`



### config.json:

* invite_code -
 * Set this to your Final invite code, which you can obtain from the Share links on [GetFinal](https://apply.getfinal.com).

* random_domain -
 * This is the domain that will be used for the signups which will push you in the front of the queue. You can have the choice to set this to anything random that you desire,**it is not very important**

###Future Changes:
* Threading to execute more signups
* Notifications via Slack(?)