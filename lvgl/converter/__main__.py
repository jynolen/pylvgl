import argparse
from pathlib import Path
from lvgl.lvgl_enum import OuputFormat, ColorFormat, CreateOutputFormat
from lvgl.converter import SmartConverter



def main():
    parser = argparse.ArgumentParser(prog=__file__)
    parser.add_argument('--dithering', action='store_true')
    parser.add_argument('--output_c', action='store_true')
    parser.add_argument('--output_format', action=CreateOutputFormat, choices=CreateOutputFormat.choices, default=OuputFormat.RGB_332.value)
    parser.add_argument('--color_format', type=ColorFormat, choices=ColorFormat, default=ColorFormat.True_Color)
    parser.add_argument('file', type=Path)
    smart = SmartConverter(parser.parse_args())
    smart.perform()


if __name__ == "__main__":
    main()