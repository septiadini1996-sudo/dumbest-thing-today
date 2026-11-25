import os

LINE = (
    "My agent read 46,000 characters of competition rules, twice, and "
    "cross-checked all forty checks \u2014 to enter a competition whose "
    "entire entry is this sentence."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
