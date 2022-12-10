#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 22:04:23 2020

@author: ceran
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 18:51:58 2020

@author: ceran
"""

import glob, os


dataset_path = '/Users/furkanceran/Desktop/images'

# Percentage of images to be used for the test set


counter=0


 
for pathAndFilename in glob.iglob(os.path.join(dataset_path, "*.jpg")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    
        # Create and/or truncate train.txt and test.txt
    try:
        ceran=("/Users/furkanceran/Desktop/images/"+str(title)+".txt")
            
        file_train = open(ceran,'r') 

        
        melis=file_train.readlines()
        #print(melis)
    except:
        os.remove(("/Users/furkanceran/Desktop/images/"+str(title)+".jpg")) 
        print("silindi")
    