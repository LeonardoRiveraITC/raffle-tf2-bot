#! python3
#! refinedmetal.py
import shelve
shelfFile = shelve.open('refinedmetal')
print(shelfFile ['refined'])
shelfFile.close()
