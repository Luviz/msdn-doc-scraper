import argparse


class ArgumentParser:
    def __init__(self):
        self.help = {
            "url": "Url of MSDN document",
            "output": "the output path, the out put is a folder and the markdown will be in README.md",
        }

        self.parser = argparse.ArgumentParser(
            description="Scrapes an msdn documentation and converts to a markdown file"
        )

        parser_mode = self.parser.add_argument_group("Mode")

        parser_mode.add_argument(
            "-u",
            "--url",
            help=self.help["url"],
        )

        parser_mode.add_argument(
            "-o",
            "--output",
            help=self.help["output"],
            default="out/",
        )

    def parse_args(self):
        return self.parser.parse_args()
