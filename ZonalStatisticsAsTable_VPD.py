import arcpy
import os
from arcpy.sa import *
from itertools import chain

folder=r'C:\Users\taohuang\Downloads\prism-main20221226\prism-main'

res = chain(range(20140701,20140731+1),range(20140801,20140831+1) )
    
for yr in xrange(2014,2022+1):
    for day in res:
        vinput=os.path.join(  folder,str(yr),  "PRISM_vpdmax_stable_4kmD2_"+str(day)+"_bil.bil")
        voutput=os.path.join( folder,"output", "PRISM_vpdmax_stable_4kmD2_"+str(day)+".dbf")
        ZonalStatisticsAsTable("bas_nonref_WestXeric","GAGE_ID",vinput,voutput,"DATA","ALL")
        
