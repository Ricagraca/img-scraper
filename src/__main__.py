from image_scraper.client import Driver

def main():
    driver = Driver(url="https://www.images.google.com")
    
    # Accept agreement
    if driver.click_button("Aceitar tudo"):
        print('clicked')
        
    # Search for dogs
    if driver.write_search_bar("tree"):
        print('searched for dogs')
        
    # Submit
    if driver.submit():
        print('submit')
        
    # Search for dogs
    for i in range(100):
        driver.scroll_down()
        
    driver.get_urls()
    
if __name__ == "__main__":
    main()
