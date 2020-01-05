#! /usr/bin/env python

import daf_yomi
import datetime

mesechta, daf = daf_yomi.todays_daf()
todays_date = datetime.datetime.today().date().strftime("%A, %B %d, %Y")
msg = "%s" % (todays_date)
print(msg)

msg = "TODAY's daf  : %s, daf %s" % (mesechta,daf)
print(msg)

mesechta, daf = daf_yomi.daf_for_delta(1)
msg = "Yesterday    : %s, daf %s" % (mesechta,daf)
print(msg)

mesechta, daf = daf_yomi.daf_for_delta(7)
msg = "7  days ago  : %s, daf %s" % (mesechta,daf)
print(msg)

mesechta, daf = daf_yomi.daf_for_delta(30)
msg = "30 days ago  : %s, daf %s" % (mesechta,daf)
print(msg)

mesechta, daf = daf_yomi.daf_for_delta(30 * 3)
msg = "3 months ago : %s, daf %s" % (mesechta,daf)
print(msg)

mesechta, daf = daf_yomi.daf_for_delta(30 * 6)
msg = "6 months ago : %s, daf %s" % (mesechta,daf)
print(msg)

mesechta, daf = daf_yomi.daf_for_delta(30 * 12)
msg = "1 year ago   : %s, daf %s" % (mesechta,daf)
print(msg)

