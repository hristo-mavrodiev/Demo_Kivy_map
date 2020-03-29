from pyproj import Proj, transform

inProj = Proj('epsg:3857')
outProj = Proj('epsg:4326')
x1, y1 = -11705274.6374, 4826473.6922
x2, y2 = transform(inProj, outProj, x1, y1)
print (x2, y2)
