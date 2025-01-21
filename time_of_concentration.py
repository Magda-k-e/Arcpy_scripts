import math

import arcpy

arcpy.env.workspace = r"C:\Files\arcpy_project"

# Get mean height value from DEM

dem_path = "basin_dem.tif"
mean_height_result = arcpy.GetRasterProperties_management(dem_path, "MEAN")
mean_height = float(mean_height_result.getOutput(0))
print("Mean height: ", mean_height)



