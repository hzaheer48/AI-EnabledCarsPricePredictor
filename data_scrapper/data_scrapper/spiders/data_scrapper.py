import scrapy
import csv

class Data_Scrapper(scrapy.Spider):
    name = 'data_scrapper'
    allowed_domains = ['pakwheels.com']
    start_urls = ['https://www.pakwheels.com/used-cars/search/-/']
    pages = 0
    header=['Name','Price','Model Year','Mileage','Engine Type','Transmission','Registered City','Color','Assembly','Body Type','Capacity']
    data = []
    def parse(self, response):
        if(self.pages==600):
            with open('pakwheels.csv', 'w', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(self.header)
                writer.writerows(self.data)
                exit()
        urls=response.xpath('//div[@class="search-title"]/a/@href').extract()
        for url in urls:
            comp_url='https://www.pakwheels.com'+url
            yield scrapy.Request(comp_url, callback=self.parse_car)
        next_page=response.xpath('//li[@class="next_page"]/a/@href').extract_first()
        if (next_page):
            self.pages+=1
            comp_url='https://www.pakwheels.com'+next_page
            yield scrapy.Request(comp_url, callback=self.parse)
    def parse_car(self,response):
        car_name=response.xpath('//h1/text()').extract_first()  
        car_price=response.xpath('//div[@class="price-box"]/strong/text()').extract_first()
        converting=response.xpath('//div[@class="price-box"]/strong/span/text()').extract_first()
        if (converting=='lacs'):
            car_price=float(car_price.strip().split('PKR')[1])*100000 
        elif (converting=='crore'):
            car_price=float(car_price.strip().split('PKR')[1])*10000000
        model_year=int(response.xpath('//span[@class="engine-icon year"]/../p/a/text()').extract_first())
        car_mileage=response.xpath('//span[@class="engine-icon millage"]/../p/text()').extract_first()   
        car_mileage=int(car_mileage.replace('km','').replace(',',''))
        engine_type=response.xpath('//span[@class="engine-icon type"]/../p/a/text()').extract_first()  
        transmission=response.xpath('//span[@class="engine-icon transmission"]/../p/a/text()').extract_first() 
        if (transmission is None):
            transmission=response.xpath('//span[@class="engine-icon transmission"]/../p/text()').extract_first() 
        register_city=response.xpath("//*[@id='scroll_car_detail']/li[2]/text()").extract_first() 
        color=response.xpath("//*[contains(text(),'Color')]/following-sibling::li/text()").extract_first() 
        assembly=response.xpath("//*[contains(text(),'Assembly')]/following-sibling::li/a/text()").extract_first() 
        if (assembly!='Local') and (assembly!='Imported'):
            assembly=response.xpath("//*[contains(text(),'Assembly')]/following-sibling::li/text()").extract_first() 
        body_type=response.xpath("//*[contains(text(),'Body Type')]/following-sibling::li/a/text()").extract_first()          
        capacity=response.xpath("//*[contains(text(),'Engine Capacity')]/following-sibling::li/text()").extract_first() 
        self.data.append([car_name,car_price,model_year,car_mileage,engine_type,transmission,register_city,color,assembly,body_type,capacity])
        yield {
                "Name":     car_name,
                "Price":    car_price,
                "Model Year": model_year,
                "Mileage": car_mileage,
                "Registered City": register_city,
                "Engine Type": engine_type,
                "Engine Capacity": capacity,
                "Transmission": transmission,
                "Color": color,
                "Assembly": assembly,
                "Body Type": body_type
        }