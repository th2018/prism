import arcpy
from arcpy.sa import *
for day in xrange(20210801,20210831):
    input=r"C:\Users\taohuang\Downloads\prism-main\PRISM_tmax_stable_4kmD2_"+str(day)+"_bil.bil"
    print(input)
    output=r"C:\Users\taohuang\Downloads\prism-main\PRISM_tmax_stable_4kmD2_"+str(day)+".dbf"
    ZonalStatisticsAsTable("USGS West Mnts gages","GAGE_ID",input,output,"DATA","ALL")
