import math

import arcpy

arcpy.env.workspace = r"C:\Files\arcpy_project"

# Get mean height value from DEM

dem_path = "basin_dem.tif"
mean_height_result = arcpy.GetRasterProperties_management(dem_path, "MEAN")
mean_height = float(mean_height_result.getOutput(0))
print("Mean height: ", mean_height)

# Get maximum flow length from raster flow length file

flow_path = "flow_len.tif"
length_result = arcpy.GetRasterProperties_management(flow_path, "MAXIMUM")
max_len = float(length_result.getOutput(0))
print("Max flow length is: ", max_len)

# Get Area from polygon shapefile

polygon_path = "basin.shp"
with arcpy.da.SearchCursor(polygon_path, ["Area"]) as cursor:
    for row in cursor:
        area_value = row[0]
        print("Area", area_value)


# Function for calculating time of concentration Tc in hours using the Giandotti formula

def calculate_time_concentration(area, length):
    area_km = area/1000000
    length_km = length/1000
    time_concentration = (4 * math.sqrt(area_km) + 1.5*length_km)/(0.8 * (mean_height-0))
    return time_concentration


time_conc = calculate_time_concentration(area_value, max_len)
print("time of concentration is ", time_conc, "hrs")

