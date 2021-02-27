import praw
import time
import os


def bot_login():
    return praw.Reddit(username='legalise-bot',
                       password='removed_for_security',
                       client_id='^',
                       client_secret='^^',
                       user_agent="legalise-bot by /u/ddgsanc")


def run_bot(r, comments):
    for comment in r.subreddit('legaliseireland').comments(limit=1000):
        if "!legalise" in comment.body and comment.id not in comments and comment.author != r.user.me():
            print("String with \"!legalise\" found in comment " + comment.id)
            comment.reply("Legalise it! Send [this](https://docs.google.com/document/d/1q9KcfsHnu6Km_gkUSYUI6_t2mHqHIVHEnsVLgjv06xM/edit) to your TDs, make sure to edit to into your own words! \n\n [Cannabis Normalisation Ireland](http://www.norml.ie/)  \n\n [People Before Profit are major proprietors for legalisation currently](https://www.pbp.ie/policies/drugs-policy/) \n\n [Cork Cannabis Activist Network](https://twitter.com/Cork_CAN) \n\n [The effect of cannabis on the economy of the US](https://www.jec.senate.gov/public/_cache/files/bf473de9-98bb-4465-a310-de992926409a/national-cannabis-economy-final.pdf) \n\n [Info on our currently very restrictive medical cannabis programme](https://www.gov.ie/en/publication/90ece9-medical-cannabis-access-programme/) \n\n [Does legalising cannabis reduce crime?](https://reason.org/wp-content/uploads/does-legalizing-marijuana-reduce-crime.pdf) \n\n [COVID-19 and cannabis](https://growgroupplc.com/covid-19-and-cannabis-black-market-supply-is-more-dangerous-to-patients-than-ever/) \n\n [EU Drug markets report 2019](https://www.emcdda.europa.eu/publications/joint-publications/eu-drug-markets-report-2019_en) \n\n [Colorado, with roughly the same population as Ireland, passes 1 billion in state revenue](https://www.cnbc.com/2019/06/12/colorado-passes-1-billion-in-marijuana-state-revenue.html) \n\n ------------------------------------------ \n\n Lets all try our best to get this beautiful plant legalised once and for all!")
            print("Replied to comment " + comment.id)

            comments.append(comment.id)

            with open("comments_replied_to.txt", "a") as f:
                f.write(comment.id + "\n")

    print("Search Completed.")

    print(comments)

    print("Sleeping for 10 seconds...")
    # Sleep for 10 seconds...
    time.sleep(10)


def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments = f.read()
            comments = comments.split("\n")

    return comments


reddit = bot_login()
comments_replied_to = get_saved_comments()
print(comments_replied_to)

while True:
    run_bot(reddit, comments_replied_to)
