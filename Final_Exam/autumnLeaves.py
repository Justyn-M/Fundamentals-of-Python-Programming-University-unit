from matplotlib.path import Path
#%matplotlib inline

############# this code makes a leaf shaped marker - do not edit #############
def makeLeaf():
    verts = [
        (1,-1), #lower right
        (-1,-1), #lower left 
        (-1,1), #upper left 
        (1,1), #upper right
        (1,-1), #lower right
        ]

    codes = [
        Path.MOVETO, #begin the figure in the lower right
        Path.CURVE3, #start a 3 point curve with the control point in lower left
        Path.LINETO, #end curve in the upper left
        Path.CURVE3, #start a new 3 point curve with the upper right as a control point
        Path.LINETO, #end curve in lower right
        ]

    path = Path(verts,codes)
    return path
############# this code makes a leaf shaped marker - do not edit #############