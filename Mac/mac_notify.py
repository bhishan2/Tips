#!python
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 17, 2017 Thu
"""
Applescript to display notifications.

osascript -e 'tell app "System Events" to display alert "Hello World"'  # best
osascript -e 'display notification "This program finished." with title "Nofification"'
osascript -e 'display notification "message" with title "Nofification" subtitle "subtitle"'
display notification "message" sound name "default"
osascript -e 'tell app "System Events" to display dialog "Hello World"'
osascript -e 'tell app "Finder" to display dialog "Hello World"'
"""


# Imports
import subprocess
import time

def mac_notify(msg):
    """Using desktop notifications in macos.

    ..note::

      To keep the notification button until you close it chage the
      system preferences of the notifications.
      System Preferences > Nofitications > Script Editor > Check all and choose alert

    ..code::

      osascript -e 'display notification "msg" with title "Notification" subtitle "subtitle"'

    """
    subtitle = time.ctime()
    notif = r'''
    osascript -e 'display notification "{}" with title "Notification" subtitle "{}"'
    '''.format(msg,subtitle)
    subprocess.call(notif,shell=True)


def main():
    msg = "Program ended"
    mac_notify(msg)


if __name__ == "__main__":
    main()
