import argparse
import converter

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert midi files to flipper zero fmf (flipper music file) format")
    parser.add_argument("-i", "--input", help="Input midi file path", required=True)
    parser.add_argument("-o", "--output", help="Output fmf file path", required=True)
    args = parser.parse_args()
    
    converter.midi_to_fmf(args.input, args.output)
