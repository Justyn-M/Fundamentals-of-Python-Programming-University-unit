#
# csvlayouts.py - supporting files for importing CSV map layouts
#

from csv import reader

def import_csv_layout(path):
    terrain_map = []
    with open(path) as maplayout:
        layout = reader(maplayout,delimiter = ',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map

def importFolder(path):
    surfaceList = []

    for _,__,imgFiles in walk(path):
        for image in imgFIles:
            fullPath = path + '/' + image
            surfaceImage = pygame.image.load(fullPath).convert_alpha()
            surfaceList.append(surfaceImage)

# import_csv_layout('/home/justyn/FOP/Assignment/csv_files/map_Barriers.csv')
