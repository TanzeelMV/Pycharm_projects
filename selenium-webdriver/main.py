# import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# keep browser window open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")

captcha = driver.find_element(By.LINK_TEXT, value="Try different image")
captcha.click()

# driver.close() # closes the particular tab

dollar_price = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
cents_price = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text

print(f"The price is $ {dollar_price}.{cents_price}.")
# //*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[3]
driver.quit()  # closes the entire browser [quit the program]
