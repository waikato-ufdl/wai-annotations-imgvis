# wai-annotations-imgvis
Image visualization plugins for the wai.annotations library.

The manual is available here:

https://ufdl.cms.waikato.ac.nz/wai-annotations-manual/

## Plugins
### ADD-ANNOTATION-OVERLAY-IC
Adds the image classification label on top of images passing through.

#### Domain(s):
- **Image Classification Domain**

#### Options:
```
usage: add-annotation-overlay-ic [--font-color FONT_COLOR] [--font-family FONT_FAMILY] [--font-size FONT_SIZE] [--position TEXT_PLACEMENT]

optional arguments:
  --font-color FONT_COLOR
                        the RGB color triplet to use for the font.
  --font-family FONT_FAMILY
                        the name of the TTF font-family to use, note: any hyphens need escaping with backslash.
  --font-size FONT_SIZE
                        the size of the font.
  --position TEXT_PLACEMENT
                        the position of the label (X,Y).
```

### ADD-ANNOTATION-OVERLAY-OD
Adds object detection overlays to images passing through.

#### Domain(s):
- **Image Object-Detection Domain**

#### Options:
```
usage: add-annotation-overlay-od [--fill] [--fill-alpha FILL_ALPHA] [--font-family FONT_FAMILY] [--font-size FONT_SIZE] [--force-bbox] [--label-key LABEL_KEY] [--labels LABELS] [--num-decimals NUM_DECIMALS] [--outline-alpha OUTLINE_ALPHA] [--outline-thickness OUTLINE_THICKNESS] [--text-format TEXT_FORMAT] [--text-placement TEXT_PLACEMENT] [--vary-colors]

optional arguments:
  --fill                whether to fill the bounding boxes/polygons
  --fill-alpha FILL_ALPHA
                        the alpha value to use for the filling.
  --font-family FONT_FAMILY
                        the name of the TTF font-family to use, note: any hyphens need escaping with backslash.
  --font-size FONT_SIZE
                        the size of the font.
  --force-bbox          whether to force a bounding box even if there is a polygon available
  --label-key LABEL_KEY
                        the key in the meta-data that contains the label.
  --labels LABELS       the comma-separated list of labels of annotations to overlay, leave empty to overlay all
  --num-decimals NUM_DECIMALS
                        the number of decimals to use for float numbers in the text format string.
  --outline-alpha OUTLINE_ALPHA
                        the alpha value to use for the outline.
  --outline-thickness OUTLINE_THICKNESS
                        the line thickness to use for the outline, <1 to turn off.
  --text-format TEXT_FORMAT
                        template for the text to print on top of the bounding box or polygon, '{PH}' is a placeholder for the 'PH' value from the meta-data or 'label' for the current label; ignored if empty.
  --text-placement TEXT_PLACEMENT
                        comma-separated list of vertical (T=top, C=center, B=bottom) and horizontal (L=left, C=center, R=right) anchoring.
  --vary-colors         whether to vary the colors of the outline/filling regardless of label
```

## IMAGE-VIEWER-IC
Displays images.

### Domain(s):
- **Image Classification Domain**

### Options:
```
usage: image-viewer-ic [--delay DELAY] [--position POSITION] [--size SIZE] [--title TITLE]

optional arguments:
  --delay DELAY        the delay in milli-seconds between images, use 0 to wait for keypress, ignored if <0
  --position POSITION  the position of the window on screen (X,Y)
  --size SIZE          the maximum size for the image: WIDTH,HEIGHT
  --title TITLE        the title for the window
```

# IMAGE-VIEWER-IS
Displays images.

### Domain(s):
- **Image Segmentation Domain**

### Options:
```
usage: image-viewer-is [--delay DELAY] [--position POSITION] [--size SIZE] [--title TITLE]

optional arguments:
  --delay DELAY        the delay in milli-seconds between images, use 0 to wait for keypress, ignored if <0
  --position POSITION  the position of the window on screen (X,Y)
  --size SIZE          the maximum size for the image: WIDTH,HEIGHT
  --title TITLE        the title for the window
```

## IMAGE-VIEWER-OD
Displays images.

### Domain(s):
- **Image Object-Detection Domain**

### Options:
```
usage: image-viewer-od [--delay DELAY] [--position POSITION] [--size SIZE] [--title TITLE]

optional arguments:
  --delay DELAY        the delay in milli-seconds between images, use 0 to wait for keypress, ignored if <0
  --position POSITION  the position of the window on screen (X,Y)
  --size SIZE          the maximum size for the image: WIDTH,HEIGHT
  --title TITLE        the title for the window
```
