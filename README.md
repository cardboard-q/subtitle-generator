# subtitle-generator
easy way to parse a text file to generate png subtitles

- current iteration has hard-coded text paths and customization values

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

## Adjust font size, margin, or background color
|variable | description | example |
| - | - | - |
| font_size | size of the font | 40 |
| margin | distance from edge to text in pixels | 40 |
| background_rgba  | 8-bit color values for 3-channel color with alpha | (0,0,0, 220) |

## Data setup
once a path to a translation text is linked, please ensure that it is in the following format:

```
Original text <language A>
Translated text <language B>

Different text <language A>
Translated different text <language A>

.
.
.
```

## Run program
In the terminal from this directory, just run:

    `python subtitles.py`
