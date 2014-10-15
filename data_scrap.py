import urllib2
from BeautifulSoup import BeautifulSoup
import re
import os
import csv


def dataExtract(fish_url):
    try:
        page = urllib2.urlopen(fish_url)
    except:
        return

    html_doc = page.read()
    soup = BeautifulSoup(html_doc)

    
    areatable = soup.find('table',{'id':'ctrl_leaderboard_dgContestLeaders'})
    d = {}
    def chunks(l, n):
        return [l[i:i+n] for i in range(0, len(l), n)]

    a = chunks([i.text for i in areatable.findAll('td')], 8)
    
    t = 1

    while t:
       with open('testme.csv', 'a') as csvfile:
          spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
          spamwriter.writerow(a[t])
       t = t + 1
       if(t==50):
          t = 0

fish_url = 'http://contests.covers.com/sportscontests/leaders.aspx?sportID=2'
dataExtract(fish_url)
