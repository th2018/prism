import arcpy
from arcpy.sa import *
for yr in xrange(2010,2021+1):
    for day in xrange(yr*10000+801, yr*10000+830):
        input=r"C:\Users\taohuang\Downloads\prism-main\yr\PRISM_tmax_stable_4kmD2_"+str(day)+"_bil.bil"
        output=r"C:\Users\taohuang\Downloads\prism-main\yr\PRISM_tmax_stable_4kmD2_"+str(day)+".dbf"
        ZonalStatisticsAsTable("USGS West Mnts gages","GAGE_ID",input,output,"DATA","ALL")
