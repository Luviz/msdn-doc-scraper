

import scraper 
from argumentParser import ArgumentParser

parser = ArgumentParser()
args = parser.parse_args()

def main():
    url = args.url
    output_path = args.output
    try:
        markdown = scraper.get_content_as_markdown(url)
        scraper.save(markdown, output_path)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
