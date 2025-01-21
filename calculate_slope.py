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

# function to calculate slope
def calculate_slope(point1, point2):
    x1, y1 = point1['xy']
    x2, y2 = point2['xy']
    elevation1 = point1['elevation']
    elevation2 = point2['elevation']

    dist = math.sqrt((x2-x2)**2 + (y2-y1)**2)

    slope = (elevation2-elevation1)/dist
    return slope, dist

# upstream
upstream_slope, upstream_distance = calculate_slope(upstream_points[0], upstream_points[1])
print("upstream slope: {:.5f} ".format(upstream_slope))


# downstream
downstream_slope, downstream_distance = calculate_slope(downstream_points[0], downstream_points[1])
print("downstream slope: {:.5f} ".format(downstream_slope))
