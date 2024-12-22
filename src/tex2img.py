import sys
import os.path
import argparse
from util.texconvert import tex_to_png

parser = argparse.ArgumentParser(
    description="Unpacks a Rotwood Klei TEX file (and XML atlas) to PNG images.",
)
parser.add_argument('tex_path', help="TEX texture file")
parser.add_argument('-A', '--auto-atlas', help="Automatically find and use the XML atlas matching the texture file name", action="store_true", dest="auto_atlas")
parser.add_argument('-a', '--atlas', help="XML atlas file, the result unpacked images will be placed in a new directory", dest="atlas_path")
args = parser.parse_args()

tex_path = args.tex_path
auto_atlas = args.auto_atlas
print(auto_atlas)
atlas_path = None
if auto_atlas:
    atlas_path = os.path.splitext(tex_path)[0]+".xml"
else:
    atlas_path = args.atlas_path

failed = False
if not os.path.isfile(tex_path):
    print("tex does not exist")
    failed = True
if (atlas_path != None) and (not os.path.isfile(atlas_path)):
    print("atlas does not exist")
    atlas_path = None
if failed: exit(1)

tex_to_png(tex_path=tex_path, atlas_path=atlas_path)
