from flask import Flask
import daf_yomi
import datetime
app = Flask(__name__)

@app.route('/')
def hello_world():
    return build()




def build():
    todays_date = datetime.datetime.today().date().strftime("%A, %B %d, %Y")
    msg1 = "%s" % (todays_date)
    mesechta, daf = daf_yomi.todays_daf()
    msg2 = "TODAY -----> %s, daf %s" % (mesechta,daf)
    mesechta, daf = daf_yomi.daf_for_delta(1)
    msg3 = "Yesterday -> %s, daf %s" % (mesechta,daf)
    mesechta, daf = daf_yomi.daf_for_delta(7)
    msg4 = "7 days ----> %s, daf %s" % (mesechta,daf)
    mesechta, daf = daf_yomi.daf_for_delta(30)
    msg5 = "30 days ---> %s, daf %s" % (mesechta,daf)
    mesechta, daf = daf_yomi.daf_for_delta(30 * 3)
    msg6 = "3 months --> %s, daf %s" % (mesechta,daf)
    mesechta, daf = daf_yomi.daf_for_delta(30 * 6)
    msg7 = "6 months --> %s, daf %s" % (mesechta,daf)
    mesechta, daf = daf_yomi.daf_for_delta(30 * 12)
    msg8 = "1 year ----> %s, daf %s" % (mesechta,daf)
    return c() + msg1 + n() + msg2 + n() + msg3 + n() + msg4 + n() + msg5 + n() + msg6 + n() + msg7 + n() + msg8 + cf()


def n():
    return "</br>"

def c():
    return "<code>"

def cf():
    return "</code>"
