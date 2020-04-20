from PIL import Image, ImageDraw, ImageFont
import os

def main():
    path_to_translation = '/home/cardboard/dev/subtitle-generator/translation.txt'
    folder_to_save = '/home/cardboard/dev/subtitle-generator/example_subtitles'
    font_path = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'

    with open(path_to_translation, 'r') as f:
        split_text = [line for line in f.readlines()
                        if len(line) > 0 and line != '\n']
        if not os.path.isdir(folder_to_save):
            os.mkdir(folder_to_save)
        for i in range(0, len(split_text), 2):
            write_subtitle(folder_to_save, font_path, str(1 + int(i/2)),split_text[i],split_text[i+1])

def write_subtitle(s, fp, idx, eng, ja):
    font_size = 40
    margin = font_size
    background_rgba = (0, 0, 0, 220)

    text = ja.replace('\n','')  + '\n' + eng.replace('\n','')

    # build a plate for text with arbitrarily large size (will crop at the end)
    plate = Image.new('RGBA', (5000,5000), background_rgba)

    # insert your favorite unicode font (opentype or truetype)
    font = ImageFont.truetype(fp, font_size)

    # write the text
    draw = ImageDraw.Draw(plate)
    draw.text((margin, margin), text, align="center", font=font, fill=(255, 255, 255, 255))

    # get size of font
    text_x, text_y = draw.textsize(text, font=font)

    # crop based on margins and text size
    box = (0 , 0, text_x+2*margin, text_y+2*margin)
    plate.crop(box).save(os.path.join(s, r'{}_{}.png'.format(idx.zfill(4), eng[:32].replace(' ','_'))))

if __name__ == '__main__':
  main()
