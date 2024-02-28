import freetype
import rectpack
import png


def main():
    chars_to_pack = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_=+`~[{]}\\;:'\",<.>/?"

    img_w, img_h = 100, 100
    img_data = [255, 0, 0] * img_w * img_h

    def write_bitmap(buf, rows, width, pitch, x, y):
        for i in range(rows):
            img_off = (img_w * 3 * (y + i)) + (3 * x)
            buf_off = (pitch * i)
            img_data[img_off:img_off+width] = buf[buf_off:buf_off+width]

    face = freetype.Face("res/FiraCode-Regular.ttf")
    face.set_char_size(12*64)

    packer = rectpack.newPacker(mode=rectpack.PackingMode.Online, rotation=False)
    packer.add_bin(img_w, img_h)

    for i, c in enumerate(chars_to_pack):
        face.load_char(c, freetype.FT_LOAD_RENDER | freetype.FT_LOAD_FORCE_AUTOHINT | freetype.FT_LOAD_TARGET_LCD)
        
        bitmap = face.glyph.bitmap
        width = bitmap.width
        rows = bitmap.rows
        pitch = bitmap.pitch
        success = packer.add_rect(width // 3 + 1, rows + 1, i)
        if not success:
            print('no room!')
            continue
        _, x, y, w, h, rid = packer.rect_list()[-1]
        if rid != i:
            print('bwuh??')
            continue
        y = (img_h - y) - h # rectpack assumes bottom left corner
        write_bitmap(bitmap.buffer, rows, width, pitch, x, y)

    png.from_array([img_data[(i*3*img_w):(i*3*img_w)+img_w*3] for i in range(img_h)], 'RGB').save('test_atlas.png')


if __name__ == "__main__":
    main()