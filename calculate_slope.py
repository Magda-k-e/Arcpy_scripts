import arcpy

# create a new shapefile from a shapefile with 4 points (2 upstream and 2 downstream) and include elevation attribute from the DEM

arcpy.env.workspace = r"C:\GIS\project"

# points file is a shapefile which contains the selected 4 points
points_file = "points_file.shp"
dem = "dem_file.tif"
points_elevation = "points_elevation.shp"
arcpy.sa.ExtractValuesToPoints(points_file, dem, points_elevation)

# list to store the coordinates and elevation of the points
points = []
# get the coordinates and the elevation of the points 
with arcpy.da.SearchCursor(points_file, ['SHAPE@XY', 'RASTERVALU']) as cursor:
    for row in cursor:
        points.append({'xy': row[0], 'elevation': row[1]})
        
#list the points
upstream_points = points[:2] 
downstream_points = points[2:]
