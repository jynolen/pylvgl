import argparse
import sys
from pathlib import Path
from lvgl.lvgl_enum import OuputFormat, CreateOutputFormat
from lvgl.deconverter.deconverter import Deconverter

def main():
    parser = argparse.ArgumentParser(prog=__file__)
    parser.add_argument('--output_format', action=CreateOutputFormat, choices=CreateOutputFormat.choices, default=OuputFormat.RGB_565.value)
    parser.add_argument('--output_file', type=Path)
    parser.add_argument('file', type=Path)
    args = parser.parse_args()
    deconverter = Deconverter(args.file, args.output_format)
    deconverter.perform(args.output_file)

if __name__ == "__main__":
    main()