import os
import requests
from bs4 import BeautifulSoup
import markdownify


def ensure_path(path: str):
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def get_content_as_markdown(url: str) -> tuple[str, list[dict[str, str]]]:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")

    main_content = soup.find("main").find("div", {"class": "content"})

    if not main_content:
        raise ValueError("Could not find main content on the page")

    return markdownify.markdownify(str(main_content), heading_style="ATX")


def save(content: str, folder_path: str):
    ensure_path(folder_path)
    md_path = os.path.join(folder_path, f"README.md")
    with open(md_path, "w", encoding="utf-8") as file:
        file.write(content)


def main():
    url = "https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview"
    output_path = "out/app-insights-overview"
    try:
        markdown = get_content_as_markdown(url)
        save(markdown, output_path)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
