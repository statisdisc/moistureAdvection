import sys
import os
import numpy as np

os.system( "./Allrun" )

folder_xyz = os.path.join(sys.path[0], "moistureAdvection")
os.system( "rm -rf {}".format(folder_xyz) )
os.makedirs( folder_xyz )

times = range(0,1820,20)
    
for time in times:
    folder_time_xyz = os.path.join(folder_xyz, str(time))
    if not os.path.exists( folder_time_xyz ):
        os.makedirs( folder_time_xyz )
    
    folder_time = os.path.join(sys.path[0], str(time))
    os.system( "cp {} {}/".format( os.path.join(folder_time,"*.xyz"), folder_time_xyz ) )
        
os.system( "cp -r {}/ $DROPBOX/PhD/2020/".format(folder_xyz) )