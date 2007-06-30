import hippo
import os
import cairo
import gtk

from sugar.graphics import color
from sugar.graphics import font

from playtile import PlayTile

class PlayView(hippo.Canvas):
    def __init__(self, numtiles):
        hippo.Canvas.__init__(self)

        root = hippo.CanvasBox()
        root.props.orientation = hippo.ORIENTATION_HORIZONTAL

        tilebox = hippo.CanvasBox()
        tilebox.props.orientation = hippo.ORIENTATION_VERTICAL
        root.append(tilebox)
                        
        self.tiles = []
        
        tile_num = 0

        while tile_num < numtiles:
            if tile_num == 0 or ((tile_num)%4) == 0:
                box = hippo.CanvasBox()
                box.props.orientation = hippo.ORIENTATION_HORIZONTAL
                tilebox.append(box)
                
            tile = PlayTile(tile_num)                   
            self.tiles.append(tile)            
            box.append(tile)
        
            tile_num+=1        
            
        self.set_root(root)
        self.show()
            
    def flip(self, tile_num, obj, color):    
        tile = self.tiles[tile_num]
        tile.img_pixbuf = gtk.gdk.pixbuf_new_from_file(obj)
        tile.img_widget.set_from_pixbuf(tile.img_pixbuf)
        tile.props.background_color = color
        tile.emit_paint_needed(0, 0, -1, -1)
        
