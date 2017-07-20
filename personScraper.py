from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class pScraper(object):
    
    def __init__(self, start_url = None):
        
        self.wd = webdriver.Chrome()
        
        if start_url:
            if 'https://' not in start_url:
                start_url =  'https://' + '.'.join(start_url.split('.')[-2:-1])
        else:
            start_url = 'https://www.google.com' 

        self.wd.get(start_url)
        

    def start(self, next_btn, main_form, num_pages, dir_name):

        for i in range(num_pages):
            self.wd.save_screenshot("/".join( [dir_name, 'page_{0}'.format(1+i)] ) )
            print('Saving Page {0}...'.format(1+i))
            self.wd.find_element_by_xpath(next_btn).click()


if __name__  == '__main__':
    
    print('Yo, welcome to the Pearson Website eBook Scraper')
    start = input('Enter in the location of the starting url including the "https" part\n(i.e. "https://www.google.com") or nothing manually enter it into the web browser later\n\t>>> ')
    
    if start == "":
        start = None

    print('Opening up the web browser. Please login in and get to the page you need scraped')
    ps = pScraper(start)

    print('This is where it gets a bit technical. Use the chrome inspect tool to get the \nXPATH of the next page button and the main form for the ebook viewer\nooooor find someone to do it form you')
    
    next    = input('\tXPATH of the next page button: ')
    mform   = input('\tXPATH of the main ebook viewer form: ')

    input('Press <Enter> for next set of instructions')

    print('Yeah booi, almost ready. Testing to see if the next button works...')
    print("\t<**WARNING**>: If it doesn't work it may crash the program. Either way just \n\trestart and try again")
    
    ps.wd.find_element_by_xpath(next).click()
    
    print("If you're reading this, then the program didn't crash lol. But if it didn't go to the \nnext page, that still means something went wrong. If so, restart and try again, otherwise, go on")
    print("\t** Make sure to move the page back if you wanted to start from the previous page")
    
    input('Press <Enter> for next set of instructions')

    pages = int(input("How many pages do y'all need scraped fam: "))
    name = input("What would you like to call this book: ")
    
    print("Alright, we're all set. Leggo!\n\t**There is a chance this thing will crap out after about ~45 pages, \n\tso check up on the browser periodically to make sure its doing what it \n\tshould be doing")

    input('Press <Enter> to start scraping')

    ps.start(next, mform, pages, name)
    
    print('Done! Go check the folder this file is in to make sure all your images are alright')
        
    input('<Press Enter to exit...>')
    

    