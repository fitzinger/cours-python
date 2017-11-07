# -*- coding: utf-8 -*-

import time

secs = 10

while secs >= 0:
    print(str(secs))
    secs -= 1
    # La fonction time.sleep() ne fonctionne pas correctement
    # quand elle est utilisée dans un notebook.
    time.sleep(1)

print('Happy new year !')
