import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFont, ImageDraw


class Draw:
    _font = [
        ImageFont.truetype("res/eng_92.ttf", 125),
        ImageFont.truetype("res/zh_cn_92.ttf", 90)
    ]
    _bg = cv2.resize(cv2.imread("res/yellow_bg.png"), (440, 140))

    def __call__(self, plate):
        if len(plate) != 7:
            return None
        fg = self._draw_fg(plate)
        return cv2.cvtColor(cv2.bitwise_and(fg, self._bg), cv2.COLOR_BGR2RGB)

    def _draw_char(self, ch):
        img = Image.new("RGB", (45 if ch.isupper() or ch.isdigit() else 90, 140), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        draw.text(
            (0, 0 if ch.isupper() or ch.isdigit() else 6), ch,
            fill = (0, 0, 0),
            font = self._font[0 if ch.isupper() or ch.isdigit() else 1]
        )
        if img.width > 45:
            img = img.resize((45, 140))
        return np.array(img)

    def _draw_fg(self, plate):
        img = np.array(Image.new("RGB", (440, 140), (255, 255, 255)))
        offset = 15
        img[0:140, offset:offset+45] = self._draw_char(plate[0])
        offset = offset + 45 + 12
        img[0:140, offset:offset+45] = self._draw_char(plate[1])
        offset = offset + 45 + 34
        for i in range(2, len(plate)):
            img[0:140, offset:offset+45] = self._draw_char(plate[i])
            offset = offset + 45 + 12
        return img


if __name__ == "__main__":
    draw = Draw()
    plate = draw("京A12345")
    plt.imshow(plate)
    plt.show()
