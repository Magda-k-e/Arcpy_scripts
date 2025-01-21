import arcpy

# create a new shapefile from a shapefile with 4 points and include elevation attribute from the DEM

arcpy.env.workspace = r"C:\GIS\project"

points_file = "points_file.shp"
dem = "dem_file.tif"
points_elevation = "points_elevation.shp"
arcpy.sa.ExtractValuesToPoints(points_file, dem, points_elevation)


