import arcpy
import os
from arcpy.sa import *
#for unit in ["g","i"]:
    #input=os.path.join( r"C:\Users\taohuang\Downloads\prism-main",str(yr),  "PRISM_tmax_stable_4kmD2_"+str(day)+"_bil.bil")
#    input=os.path.join( r"C:\Users\taohuang\Downloads\NHDPlusV21_MS_10U_10"+unit+"_HydroDem_02\NHDPlusMS\NHDPlus10U\NHDPlusHydrodem10"+unit+"\hydrodem")
#    output=os.path.join( r"C:\Users\taohuang\Downloads\prism-main\NHDPlusV21_MS_10U_10"+unit+"_HydroDem_02"+".dbf")
#    ZonalStatisticsAsTable("bas_ref_all_three_states_st","GAGE_ID",input,output,"DATA","ALL")

#NHDPlusV21_CO_14_14b_HydroDem_01\NHDPlusCO\NHDPlus14\NHDPlusHydrodem14b
#input=os.path.join( r"C:\Users\taohuang\Downloads\NHDPlusV21_CO_14_14b_HydroDem_01\NHDPlusCO\NHDPlus14\NHDPlusHydrodem14b\hydrodem")
#output=os.path.join( r"C:\Users\taohuang\Downloads\prism-main\NHDPlusHydrodem14b.dbf")
#ZonalStatisticsAsTable("bas_ref_all_three_states_st","GAGE_ID",input,output,"DATA","ALL")

#C:\Users\taohuang\Downloads\NHDPlusV21_PN_17_17b_HydroDem_01\NHDPlusPN\NHDPlus17\NHDPlusHydrodem17b
#C:\Users\taohuang\Downloads\NHDPlusV21_PN_17_17a_Hydrodem_01\NHDPlusPN\NHDPlus17\NHDPlusHydrodem17a

for unit in ["a","b"]:
    input=os.path.join( r"C:\Users\taohuang\Downloads\NHDPlusV21_PN_17_17"+unit+"_HydroDem_01\NHDPlusPN\NHDPlus17\NHDPlusHydrodem17"+unit+"\hydrodem")
    output=os.path.join( r"C:\Users\taohuang\Downloads\prism-main\NHDPlusV21_PN_17_17"+unit+"_HydroDem_01"+".dbf")
    ZonalStatisticsAsTable("bas_ref_all_three_states_st","GAGE_ID",input,output,"DATA","ALL")
