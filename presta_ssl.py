#Main module for Google Trends Scraper
#Author: Lukasz Golojuch
#Description:
#Program uses sellenium for scrapping google trends for several key words

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

#Global variables
Sex = 1 #1-male 2-female
Name = "Lukasz"
Surname = "Golojuch"
Email = "lukasz.golojuch@gmail.com"
Password = "jakieshaslo123!"
Code = "blackfriday2021"

Adress = "ul. Politechniczna 12"
PostCode = "11-111"
City = "Polska"
Phone = "664654654"

class textColours:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#path to current working directory
path = os.getcwd() 

try:
    print ("")
        
    #opening Chrome browser using chromedriver
    driver = webdriver.Chrome( ('{path}/chromedriver'.format(**locals())) );
    print (textColours.OKGREEN + ("Chromedriver executive found under path: \n{}").format(path) + textColours.ENDC)
    print (textColours.UNDERLINE + ("Opening browser...") + textColours.ENDC)

except:

    #output when chromedriver is in other path than CurrentWorkingDirectory/chromedriver
    print ("\n\n")
    print (textColours.FAIL + ("There is no chromedriver executable under this path: \n{}").format(path))
    print("Please put chromedriver executable there!") + textColours.ENDC 
    print ()

def newAccount():
    #Function for creating new account

    print("Creating new accout started")

    try:
        driver.get('https://localhost:11936/index.php?controller=authentication&create_account=1')

        time.sleep(10)

        #input sex
        if Sex == 1:
            driver.find_element_by_xpath("//input[@id='field-id_gender-1']").click()
        else:
            driver.find_element_by_xpath("//input[@id='field-id_gender-2']").click()

        #input name
        inputElement = driver.find_element_by_id("field-firstname")
        inputElement.send_keys(Name)

        #input surname
        inputElement = driver.find_element_by_id("field-lastname")
        inputElement.send_keys(Surname)

        #input email
        inputElement = driver.find_element_by_id("field-email")
        inputElement.send_keys(Email)

        #input password
        inputElement = driver.find_element_by_id("field-password")
        inputElement.send_keys(Password)

        #input agreement
        driver.find_element_by_xpath("//input[@name='customer_privacy']").click()

        #Create Account
        driver.find_element_by_xpath("//button[@class='btn btn-primary form-control-submit float-xs-right']").click()

        print (textColours.OKGREEN + ("Creating new account works correctly") + textColours.ENDC)

    except:

        print (textColours.FAIL + ("Register new accout feature does not work correctly") + textColours.ENDC)

def addProduct():

    print("Adding product to the cart started")

    #Funtction that adds products to cart
    try:
        driver.get('https://localhost:11936/index.php?id_category=39&controller=category')
        time.sleep(1)
        driver.find_element_by_xpath("//article[@data-id-product='1561']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//button[@class='btn btn-primary add-to-cart']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//button[@class='btn btn-secondary']").click()

        driver.get('https://localhost:11936/index.php?id_category=39&controller=category')
        time.sleep(1)
        driver.find_element_by_xpath("//article[@data-id-product='1562']").click()
        time.sleep(1)
        inputElement = driver.find_element_by_id("quantity_wanted")
        inputElement.clear()
        inputElement.send_keys("2")
        driver.find_element_by_xpath("//button[@class='btn btn-primary add-to-cart']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//button[@class='btn btn-secondary']").click()
        
        driver.get('https://localhost:11936/index.php?id_category=39&controller=category')
        time.sleep(1)
        driver.find_element_by_xpath("//article[@data-id-product='1563']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//button[@class='btn btn-primary add-to-cart']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//button[@class='btn btn-secondary']").click()
        
        driver.get('https://localhost:11936/index.php?id_category=39&controller=category')
        time.sleep(1)
        driver.find_element_by_xpath("//article[@data-id-product='1564']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//button[@class='btn btn-primary add-to-cart']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//button[@class='btn btn-secondary']").click()

        driver.get('https://localhost:11936/index.php?id_category=39&controller=category')
        time.sleep(1)
        driver.find_element_by_xpath("//article[@data-id-product='1565']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//button[@class='btn btn-primary add-to-cart']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//button[@class='btn btn-secondary']").click()

        driver.get('https://localhost:11936/index.php?id_category=45&controller=category')
        time.sleep(1)
        driver.find_element_by_xpath("//article[@data-id-product='1819']").click()
        time.sleep(1)
        inputElement = driver.find_element_by_id("quantity_wanted")
        inputElement.send_keys("2")
        driver.find_element_by_xpath("//button[@class='btn btn-primary add-to-cart']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//button[@class='btn btn-secondary']").click()

        driver.get('https://localhost:11936/index.php?id_category=45&controller=category')
        time.sleep(1)
        driver.find_element_by_xpath("//article[@data-id-product='1820']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//button[@class='btn btn-primary add-to-cart']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//button[@class='btn btn-secondary']").click()

        driver.get('https://localhost:11936/index.php?id_category=45&controller=category')
        time.sleep(1)
        driver.find_element_by_xpath("//article[@data-id-product='1821']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//button[@class='btn btn-primary add-to-cart']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//button[@class='btn btn-secondary']").click()

        driver.get('https://localhost:11936/index.php?id_category=45&controller=category')
        time.sleep(1)
        driver.find_element_by_xpath("//article[@data-id-product='1822']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//button[@class='btn btn-primary add-to-cart']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//button[@class='btn btn-secondary']").click()

        driver.get('https://localhost:11936/index.php?id_category=45&controller=category')
        time.sleep(1)
        driver.find_element_by_xpath("//article[@data-id-product='1823']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//button[@class='btn btn-primary add-to-cart']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//button[@class='btn btn-secondary']").click()
        
        print (textColours.OKGREEN + ("Adding product works correctly") + textColours.ENDC)

    except:

        print (textColours.FAIL + ("Add product feature does not work correctly") + textColours.ENDC)

def deleteProd():
    #Function that deletes product from the cart
    print("Deleting product from cart started")

    try:
        driver.get('https://localhost:11936/index.php?controller=cart&action=show')
        time.sleep(1)
        driver.find_element_by_xpath("//a[@data-id-product='1561']").click()

        print (textColours.OKGREEN + ("Deleting product works correctly") + textColours.ENDC)

    except:
        print (textColours.FAIL + ("Delete product feature does not work correctly") + textColours.ENDC)


def submitOrder():
    #Function for submitting the order
    print("Deleting product from cart started")

    try:
        driver.get('https://localhost:11936/index.php?controller=cart&action=show')
        time.sleep(1)

        #input promo code
        driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[1]/div[1]/div[3]/div/p/a").click()
        time.sleep(1)
        inputElement = driver.find_element_by_xpath("//*[@id='promo-code']/div/form/input[3]")
        time.sleep(1)
        inputElement.send_keys(Code)    
        time.sleep(1)
        driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[@class='btn btn-primary']").click()

        #input adress
        inputElement = driver.find_element_by_id("field-address1")
        inputElement.send_keys(Adress)

        #input postcode
        inputElement = driver.find_element_by_id("field-postcode")
        inputElement.send_keys(PostCode)

        #input city
        inputElement = driver.find_element_by_id("field-city")
        inputElement.send_keys(City)
        
        #input phone number
        inputElement = driver.find_element_by_id("field-phone")
        inputElement.send_keys(Phone)

        time.sleep(2)

        driver.find_element_by_xpath("//button[@name='confirm-addresses']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@id='delivery_option_6']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//button[@name='confirmDeliveryOption']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@name='conditions_to_approve[terms-and-conditions]']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//button[@class='btn btn-primary center-block']").click()

        print (textColours.OKGREEN + ("Submitting order works correctly") + textColours.ENDC)

    except:
        print (textColours.FAIL + ("Submit order feature does not work correctly") + textColours.ENDC)


if __name__ == "__main__":
    print("Program starts working...")

    print("========================================")
    newAccount()
    print("========================================")
    addProduct()
    print("========================================")
    deleteProd()
    print("========================================")
    submitOrder()
    print("========================================")

    print("Program Shutdown")

    


    

