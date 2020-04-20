# subtitle-generator
easy way to parse a text file to generate png subtitles

# Installation
## Install PIL
    `pip install Pillow`
## Declare paths
the top of the python script requires paths to the desired files

|variable | description | example |
| - | - | - |
|path_to_translation | wants a .txt file with text separated my new lines alternating language | `translation.txt`
|folder_to_save | wants a directory path to save to. If it does not exist, then it will be created. | `./subtitles/` |
|font_path| wants a path to a unicode font (opentype or freetype)| `/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc` |

## Run program
In the terminal from this directory, just run:

    `python subtitles.py`
