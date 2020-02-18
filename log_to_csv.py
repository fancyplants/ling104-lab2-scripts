import argparse


# I dunno man, don't ask me lmao
# but it has to be this, or else the unicode doesn't parse correctly
PRAAT_OUTPUT_ENCODING = "utf-16-be"


def read_file_into_str(file_name):
    with open(file_name, "r", encoding=PRAAT_OUTPUT_ENCODING) as f:
        data = f.read()
    return data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    data = read_file_into_str(args.filename)
    replaced = data.replace("\t", ",")

    # output as CSV
    output_name = args.filename[: args.filename.index(".")] + ".csv"
    with open(output_name, "w+") as f:
        f.write(replaced)


if __name__ == "__main__":
    main()
