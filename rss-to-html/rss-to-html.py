import feedparser
import argparse
import os
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

script_dir = os.path.dirname(os.path.abspath(__file__))

parser = argparse.ArgumentParser(description="Get latest entry of rss feed")
parser.add_argument("rss_url", help="URL of the RSS feed")
parser.add_argument("-p", "--output-path", dest="output_path", help="Path to save the outputs, default is relative", default=script_dir)


args = parser.parse_args()

global rss_url
rss_url = args.rss_url
output_path = args.output_path


def fetch_rss_feed(url, num_entries=1):
    try:
        # Parse the RSS feed
        feed = feedparser.parse(url)

        # Get the latest entries
        entries = feed.entries[:num_entries]

        # Iterate through the entries and create the Markdown list
        for entry in entries:
            title = entry.title
            url = entry.link
            content = entry.description
            date = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %z")
            date_str = date.strftime("%Y-%m-%d %H:%M:%S %Z")

            # Create a Markdown list item
            feed_item = {
                "title": title,
                "url": url,
                "date": date_str,
                "content": content
            }

        return feed_item

    except Exception as e:
        return f"Error: {e}"

def convert_html(feed_content):
    environment = Environment(loader=FileSystemLoader(os.path.join(script_dir, "templates")))
    template = environment.get_template("default-email-template.html.j2")
    content = template.render(
        article_title = feed_content['title'],
        article_url = feed_content['url'],
        article_content = feed_content['content'],
        article_date = feed_content['date'],
    )
    return content

def write_output(file, content):
    with open(os.path.join(output_path, file), "w") as output_file:
        output_file.write(content)

if __name__ == "__main__":
    rss_content = fetch_rss_feed(rss_url)
    html_content = convert_html(rss_content)
    feed_title = rss_content['title']
    feed_url = rss_content['url']
    feed_content = html_content
    write_output('title.txt', feed_title)
    write_output('url.txt', feed_url)
    write_output('content.txt', feed_content)
