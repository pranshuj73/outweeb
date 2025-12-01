import sys
from ingest import ingest_data


def main():
    if len(sys.argv) > 1 and sys.argv[1].lower() == "ingest":
        ingest_data(
            file_path="./data/anime_with_synopsis.csv",
            collection_name="outweeb"
        )
    else:
        print("hello world")


if __name__ == "__main__":
    main()
