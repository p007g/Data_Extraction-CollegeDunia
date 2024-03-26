from selenium import webdriver

try:
    # Set up the Selenium WebDriver
    path_to_chromedriver = "C:\Program Files (x86)\chromedriver.exe"

    cService = webdriver.ChromeService(executable_path=path_to_chromedriver)
    driver = webdriver.Chrome(service = cService)

    # Open the web page
    driver.get('https://collegedunia.com/course-finder')

    # Close the browser
    driver.quit()
    
except Exception as e:
    print(e)