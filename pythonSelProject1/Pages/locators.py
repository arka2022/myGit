class locators():
    #Locatiors of login page
    userName_textBox_xpath = "//input[@id='txtUsername']"
    password_textBox_xpath = "//input[@name='txtPassword']"
    submit_btn_xpath = "//input[@id='btnLogin']"

    #Locators of weatherShopper
    temp_webElement_xpath="//span[@id='temperature']"
    buyMoist_button_xpath="//button[contains(text(),'Buy moisturizers')]"
    buySunscre_button_xpath="//button[contains(text(),'Buy sunscreens')]"

    #Locators of moisturizers page
    add_tigranAloeIsolani_btn="//div[@class='text-center col-4' and .//text()='Tigran Aloe Isolani']//button"
    add_BorisAlmondHoney_btn="//div[@class='text-center col-4' and .//text()='Boris Almond and Honey']//button"
    add_vassilyAloeAttack_btn="//div[@class='text-center col-4' and .//text()='Vassily Aloe Attack']//button"
    cart_button="//button[@class='thin-text nav-link']"

    #Locaters in sunsScreen Page
    add_akibaAmazingSPF50_btn="//div[@class='text-center col-4' and .//text()='Akiba Amazing SPF-50']//button"




    #Locators of checkout Page
    total_webElement="//p[@id='total']"
    payWithCard_button="//button[@class='stripe-button-el']"
    email_textbox="//input[@id='email']"
    cardNumber_textbox="//input[@placeholder='Card number']"
    monthYear_textbox="//input[@id='cc-exp']"
    cvc_textbox="//input[@id='cc-csc']"
    pay_button="//span[@class='iconTick']"



# Confirmation  ->final page title
#//p[contains(text(),'Emmanuel Aloe Vera Beauty Gel')]/button[@class='btn btn-primary']
# //div[@class='text-center col-4' and .//text()='Tigran Aloe Isolani']//button
