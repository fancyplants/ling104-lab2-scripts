import argparse
from log_to_csv import PRAAT_OUTPUT_ENCODING


# U+0009
UNICODE_TAB = "	"

# can read normal utf 8 bytes from generated csv
def read_file_into_str(file_name):
    with open(file_name, "r") as f:
        data = f.read()
    return data


def main():
    '''
    Important note: you must rewrite the log file in VERY SPECIFIC Praat UTF-16, Big Endian,
    or else Unicode is written in incorrect byte order and is not parsable
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    # there shouldn't be any commas in file other than the delimiters, so replace
    data = read_file_into_str(args.filename)
    replaced = data.replace(",", UNICODE_TAB)

    output_name = args.filename[: args.filename.index(".")] + ".txt"
    with open(output_name, "w+", encoding=PRAAT_OUTPUT_ENCODING) as f:
        f.write(replaced)


if __name__ == "__main__":
    main()
