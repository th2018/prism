import arcpy
import os
from arcpy.sa import *
from itertools import chain

folder=r'C:\Users\taohuang\Downloads\prism-main20221226\prism-main'

yr=2015

res = chain(range( yr*10000 + 701, yr*10000 + 731+1),range( yr*10000 + 801, yr*10000 + 831+1) )
    
for yr in range( yr ,2022+1):
    for day in res:
        vinput=os.path.join(  folder,str(yr),  "PRISM_vpdmax_stable_4kmD2_"+str(day)+"_bil.bil")
        voutput=os.path.join( folder,"output", "PRISM_vpdmax_stable_4kmD2_"+str(day)+".dbf")
        ZonalStatisticsAsTable("bas_nonref_WestXeric","GAGE_ID",vinput,voutput,"DATA","ALL")
        
