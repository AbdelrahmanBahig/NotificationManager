from selenium import webdriver
from selenium.webdriver.common.by import By




class Scrapper:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        self.driver = webdriver.Chrome(options=options) 
        
    
    def extract_data(self,url,xpath):
        self.driver.get(url)
        match= self.driver.find_element(By.XPATH, xpath).text
        return match
    

# scrapper = Scrapper()
# print(scrapper.extract_data("https://realpython.com/python-web-scraping-practical-introduction/",'/html/body/div[1]/div/div/div[2]/p[1]'))
