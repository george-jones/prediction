import urllib2
import sqlite3
from datetime import datetime
from HTMLParser import HTMLParser

class MyParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.in_title = False
        self.prob = None

    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.in_title = True                    

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            a = data.split(' ')
            if len(a) >= 2:
                self.prob = a[-2][0:-1]

def error(msg):
    print msg
                
def main():
    contracts = [
        { 'name': 'Romney', 'url': 'http://www.intrade.com/v4/markets/contract/?contractId=652757' },
        { 'name': 'Gingrich', 'url': 'http://www.intrade.com/v4/markets/contract/?contractId=654836' },
        { 'name': 'Paul', 'url': 'http://www.intrade.com/v4/markets/contract/?contractId=669534' },
        { 'name': 'Huntsman', 'url': 'http://www.intrade.com/v4/markets/contract/?contractId=658927' },
        { 'name': 'Santorum', 'url': 'http://www.intrade.com/v4/markets/contract/?contractId=690905' },
        { 'name': 'Perry', 'url': 'http://www.intrade.com/v4/markets/contract/?contractId=656777' },
    ]
    
    for i, c in enumerate(contracts):
        try:
            req = urllib2.urlopen(c['url'])
            d = req.read()
            a = d.split('\n')
            p = MyParser()
            for line in a:
                p.feed(line)
            if p.prob is not None:
                c['prob'] = p.prob
                print "%s:%s" % (c['name'], p.prob)
            else:
                error("Could not get data for contract: %s" % (c['name']))
                return
        except urllib2.HTTPError, e:
            error("HTTP Error: %s - %s" % (e.code, url))
            return
        except urllib2.URLError, e:
            error("URL Error: %s - %s" % (e.reason, url))
            return

    conn = sqlite3.connect('data.sl3')
    cur = conn.cursor()
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for i, c in enumerate(contracts):
        cur.execute("INSERT INTO p (name, dt, prob) VALUES (?, ?, ?)", (c['name'], dt, c['prob']))
    conn.commit()
    cur.close()

main()
