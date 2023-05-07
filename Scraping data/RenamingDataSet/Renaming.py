import os
import glob

folder = "C:/Users/dell/Videos/S4/Stage/car-damage-detective-master/app/Data/Data_3/shutterscrape-master/shutterscrape-master/"
for count, filename in enumerate(os.listdir(folder)):
    oldname = folder + filename   
    newname = folder + str(count + 1) + ".jpg"
    os.rename(oldname, newname)

# printing the changed names
print(glob.glob(folder + "*.*"))