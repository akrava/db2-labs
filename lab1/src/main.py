from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from lxml import etree
import os
import webbrowser


def cleanup():
    try:
        os.remove("task1.xml")
        os.remove("task2.xml")
        os.remove("task2.xhtml")
    except OSError:
        pass


def scrap_data():
    process = CrawlerProcess(get_project_settings())
    process.crawl('football')
    process.crawl('moyo')
    process.start()


def task1():
    print("Task #1")
    root = etree.parse("task1.xml")
    pages = root.xpath("//page")
    print("Number of graphical documents for scrapped documents:")
    for page in pages:
        url = page.xpath("@url")[0]
        count = page.xpath("count(fragment[@type='image'])")
        print("%s: %d" % (url, count))


def task2():
    print("Task #2")
    transform = etree.XSLT(etree.parse("task2.xsl"))
    result = transform(etree.parse("task2.xml"))
    result.write("task2.xhtml", pretty_print=True, encoding="UTF-8")
    print("XHTML page will be opened in web-browser...")
    webbrowser.open('file://' + os.path.realpath("task2.xhtml"))


if __name__ == '__main__':
    print("Lab #1")
    print("Cleanup files...", end='', flush=True)
    cleanup()
    print("done")
    print("Scrapping data from sites...", end='', flush=True)
    scrap_data()
    print("finished")
    while True:
        print("-" * 45)
        print("Input number of task to execute, or something else to exit:")
        print("1. Task #1")
        print("2. Task #2")
        print("> ", end='', flush=True)
        number = input()
        if number == "1":
            task1()
        elif number == "2":
            task2()
        else:
            break
    print("Exiting...")
