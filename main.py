#Joseph Nam and Derek Lu
#Hoop Scraping

#Run application in terminal with command "streamlit run main.py"

from driver import driver

def main():
    scraping_instance = driver()
    
    scraping_instance.run_scraping_instance()

main()