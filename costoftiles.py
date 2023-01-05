costOfTile = int(input("what is the cost of tiles "))
Width = int(input("what is the width "))
Height = int(input("what is the height "))
AreaofTIle = int(input("what is the area of one tile "))

AreaofLand = Width*Height
NumberofTiles = int(AreaofLand/costOfTile)
TotalCost = str(costOfTile*NumberofTiles)
NumberofTilesstr = str(NumberofTiles)

print("number of tiles needed= " +   NumberofTilesstr)
print("Money needed= " + TotalCost)