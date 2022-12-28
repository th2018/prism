import arcpy
import os
from arcpy.sa import *
from itertools import chain

folder=r'C:\Users\taohuang\Downloads\prism-main20221226\prism-main'
for yr in xrange(2012,2022+1):
    for day in xrange(yr*10000+701, yr*10000+929+1):
        vinput=os.path.join(  folder,str(yr),  "PRISM_vpdmax_stable_4kmD2_"+str(day)+"_bil.bil")
        voutput=os.path.join( folder,"output", "PRISM_vpdmax_stable_4kmD2_"+str(day)+".dbf")
        ZonalStatisticsAsTable("bas_nonref_WestXeric","GAGE_ID",vinput,voutput,"DATA","ALL")
        
