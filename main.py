from driver import driver
def main():
    print("Welcome to School Scraper")
    scraping_instance = driver()

    scraping_instance.run_scraping_instance()

if __name__ == "__main__":
    main()