#use the scrapy libray
import scrapy
#spider name become TASK6
class TASK6(scrapy.Spider):
    #Attributes (name and url)
    name = "Task6"
    #url to the webserver spicyx
    start_urls = ['http://192.168.126.148/spicyx/']
    #method
    def parse(self,response): #to get response from the website
        # look for img and src and print inside of src
        for every_line in response.css('img'):
            #yield is to print out Image link
            yield {
                'Image link is': every_line.xpath('@src').extract_first(),
            }
