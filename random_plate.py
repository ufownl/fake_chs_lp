import random
if __name__ == "__main__":
    import black_plate
    import blue_plate
    import yellow_plate
    import green_plate
else:
    from . import black_plate
    from . import blue_plate
    from . import yellow_plate
    from . import green_plate


class Draw:
    _draw = [
        black_plate.Draw(),
        blue_plate.Draw(),
        yellow_plate.Draw(),
        green_plate.Draw()
    ]
    _provinces = ["皖", "沪", "津", "渝", "冀", "晋", "蒙", "辽", "吉", "黑", "苏", "浙", "京", "闽", "赣", "鲁", "豫", "鄂", "湘", "粤", "桂", "琼", "川", "贵", "云", "藏", "陕", "甘", "青", "宁", "新"]
    _alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    _ads = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def __call__(self):
        draw = random.choice(self._draw)
        candidates = [self._provinces, self._alphabets]
        if type(draw) == green_plate.Draw:
            candidates += [self._ads] * 6
            return draw("".join([random.choice(c) for c in candidates]), random.randint(0, 1))
        else:
            candidates += [self._ads] * 5
            return draw("".join([random.choice(c) for c in candidates]))


if __name__ == "__main__":
    import math
    import argparse
    import matplotlib.pyplot as plt

    parser = argparse.ArgumentParser(description="Generate a green plate.")
    parser.add_argument("--num", help="set the number of plates (default: 9)", type=int, default=9)
    args = parser.parse_args()

    draw = Draw()
    rows = math.ceil(args.num / 3)
    cols = min(args.num, 3)
    for i in range(args.num):
        plate = draw()
        plt.subplot(rows, cols, i + 1)
        plt.imshow(plate)
        plt.axis("off")
    plt.show()
