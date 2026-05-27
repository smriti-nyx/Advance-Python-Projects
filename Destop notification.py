###from  plyer import notification
#notification.notify(
   # title = "Hello Sera! ",
   # message = "Your first desktop works. ",
  #  timeout = 5 #
###

import os

os.system("""
    osascript -e 'display notification "Your first desktop notification works!" with title "Hello Sera!"'
""")