import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw


def load_font():
    return {
        "京": cv2.imread("res/ne000.png"),
        "津": cv2.imread("res/ne001.png"),
        "冀": cv2.imread("res/ne002.png"),
        "晋": cv2.imread("res/ne003.png"),
        "蒙": cv2.imread("res/ne004.png"),
        "辽": cv2.imread("res/ne005.png"),
        "吉": cv2.imread("res/ne006.png"),
        "黑": cv2.imread("res/ne007.png"),
        "沪": cv2.imread("res/ne008.png"),
        "苏": cv2.imread("res/ne009.png"),
        "浙": cv2.imread("res/ne010.png"),
        "皖": cv2.imread("res/ne011.png"),
        "闽": cv2.imread("res/ne012.png"),
        "赣": cv2.imread("res/ne013.png"),
        "鲁": cv2.imread("res/ne014.png"),
        "豫": cv2.imread("res/ne015.png"),
        "鄂": cv2.imread("res/ne016.png"),
        "湘": cv2.imread("res/ne017.png"),
        "粤": cv2.imread("res/ne018.png"),
        "桂": cv2.imread("res/ne019.png"),
        "琼": cv2.imread("res/ne020.png"),
        "渝": cv2.imread("res/ne021.png"),
        "川": cv2.imread("res/ne022.png"),
        "贵": cv2.imread("res/ne023.png"),
        "云": cv2.imread("res/ne024.png"),
        "藏": cv2.imread("res/ne025.png"),
        "陕": cv2.imread("res/ne026.png"),
        "甘": cv2.imread("res/ne027.png"),
        "青": cv2.imread("res/ne028.png"),
        "宁": cv2.imread("res/ne029.png"),
        "新": cv2.imread("res/ne030.png"),
        "A": cv2.imread("res/ne100.png"),
        "B": cv2.imread("res/ne101.png"),
        "C": cv2.imread("res/ne102.png"),
        "D": cv2.imread("res/ne103.png"),
        "E": cv2.imread("res/ne104.png"),
        "F": cv2.imread("res/ne105.png"),
        "G": cv2.imread("res/ne106.png"),
        "H": cv2.imread("res/ne107.png"),
        "J": cv2.imread("res/ne108.png"),
        "K": cv2.imread("res/ne109.png"),
        "L": cv2.imread("res/ne110.png"),
        "M": cv2.imread("res/ne111.png"),
        "N": cv2.imread("res/ne112.png"),
        "P": cv2.imread("res/ne113.png"),
        "Q": cv2.imread("res/ne114.png"),
        "R": cv2.imread("res/ne115.png"),
        "S": cv2.imread("res/ne116.png"),
        "T": cv2.imread("res/ne117.png"),
        "U": cv2.imread("res/ne118.png"),
        "V": cv2.imread("res/ne119.png"),
        "W": cv2.imread("res/ne120.png"),
        "X": cv2.imread("res/ne121.png"),
        "Y": cv2.imread("res/ne122.png"),
        "Z": cv2.imread("res/ne123.png"),
        "0": cv2.imread("res/ne124.png"),
        "1": cv2.imread("res/ne125.png"),
        "2": cv2.imread("res/ne126.png"),
        "3": cv2.imread("res/ne127.png"),
        "4": cv2.imread("res/ne128.png"),
        "5": cv2.imread("res/ne129.png"),
        "6": cv2.imread("res/ne130.png"),
        "7": cv2.imread("res/ne131.png"),
        "8": cv2.imread("res/ne132.png"),
        "9": cv2.imread("res/ne133.png")
    }


class Draw:
    _font = load_font()
    _bg = [
        cv2.resize(cv2.imread("res/green_bg_0.png"), (480, 140)),
        cv2.resize(cv2.imread("res/green_bg_1.png"), (480, 140))
    ]

    def __call__(self, plate, bg=0):
        if len(plate) != 8:
            return None
        try:
            fg = self._draw_fg(plate)
            return cv2.cvtColor(cv2.bitwise_and(fg, self._bg[bg]), cv2.COLOR_BGR2RGB)
        except KeyError:
            print("ERROR: Invalid character")
            return None
        except IndexError:
            print("ERROR: Invalid background index")
            return None

    def _draw_char(self, ch):
        return cv2.resize(self._font[ch], (43 if ch.isupper() or ch.isdigit() else 45, 90))

    def _draw_fg(self, plate):
        img = np.array(Image.new("RGB", (480, 140), (255, 255, 255)))
        offset = 15
        img[25:115, offset:offset+45] = self._draw_char(plate[0])
        offset = offset + 45 + 9
        img[25:115, offset:offset+43] = self._draw_char(plate[1])
        offset = offset + 43 + 49
        for i in range(2, len(plate)):
            img[25:115, offset:offset+43] = self._draw_char(plate[i])
            offset = offset + 43 + 9
        return img


if __name__ == "__main__":
    draw = Draw()
    plate = draw("京AD12345", 0)
    plt.subplot(2, 1, 1)
    plt.imshow(plate)
    plate = draw("京A12345F", 1)
    plt.subplot(2, 1, 2)
    plt.imshow(plate)
    plt.show()
