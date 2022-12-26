import arcpy
import os
from arcpy.sa import *
folder=r'C:\Users\taohuang\Downloads\prism-main20221226\prism-main'
for yr in xrange(2012,2022+1):
    for day in xrange(yr*10000+701, yr*10000+930+1):
#        input=os.path.join( r"C:\Users\taohuang\Downloads\prism-main",str(yr),  "PRISM_tmax_stable_4kmD2_"+str(day)+"_bil.bil")
        input=os.path.join( folder,str(yr),  "PRISM_tmax_stable_4kmD2_"+str(day)+"_bil.bil")
        output=os.path.join( folder,"output", "PRISM_tmax_stable_4kmD2_"+str(day)+".dbf")
#        output=os.path.join( r"C:\Users\taohuang\Downloads\prism-main","output", "PRISM_tmax_stable_4kmD2_"+str(day)+".dbf")
        ZonalStatisticsAsTable("bas_nonref_WestXeric","GAGE_ID",input,output,"DATA","ALL")
