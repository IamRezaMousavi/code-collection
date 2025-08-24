"""Created on Tue May  4 09:20:01 2021

@author: Mohammad
"""

from notifypy import Notify


def sendNotif(message, title, appname='Python', icon=None, audio=None):
    notif = Notify(
        default_notification_title=title,
        default_notification_application_name=appname,
        default_notification_icon=icon,  # png
        default_notification_audio=audio,  # wav
    )
    notif.send()


message = 'Hello my KING.'
sendNotif(message, 'Me')

# Edited on Sat May 29 20:51:00 2021
