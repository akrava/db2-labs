from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from lxml import etree

if __name__ == '__main__':
    print("Lab#1")
    process = CrawlerProcess(get_project_settings())
    process.crawl('football')
    process.crawl('moyo')
    process.start()
    print("finished")
    print("Task #1")
    tree = etree.parse("task1.xml")
    el = tree.xpath("//page")
    for e in el:
        name = e.xpath("./@url")
        n = e.xpath("count(fragment[@type='image'])")
        print(name, n)

    print("Task #2")

