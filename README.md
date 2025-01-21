# Arcpy script "time_of_concentration.py"
This script was developed with the ArcPy site package for use in Esri's ArcMap.
The following are required for input:
- the DEM .tif file of a basin
- the flow direction .tif file
- the basin polygon .shp file

## Features
- acquires the mean height value (H) in m of the basin from the DEM raster file
- the maximum flow length (L) in km from the flow direction file
- the area (A) in km^2 from the basin shapefile
- computes the time of concentration (Tc) in hours for a basin using the Giandotti formula:


![image](https://github.com/user-attachments/assets/5ba8a369-fd52-4522-9cef-49e4067eb8c2)

- After caclulating the time of concentration, it adds it as a new field in the attribute table of the basin shapefile.

# Arcpy script "calculate_slope.py"
This script was developed with the ArcPy site package for use in Esri's ArcMap. It calculates slope between points of a shapefile.
The following are required for input:
- a .shp points file
- a DEM raster file

## Features
- extracts the elevation from the DEM to the points .shp file
- lists the points with coordinates and elevation
- calculates and writes slope in a .txt file
