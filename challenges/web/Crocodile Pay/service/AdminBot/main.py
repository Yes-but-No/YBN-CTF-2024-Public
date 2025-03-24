from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlencode,urlparse
import json
import threading
import os

app = Flask(__name__)
ADMIN_TOKEN = os.environ.get('ADMIN_TOKEN','admin_token')
DEDUCT_TOKEN = os.environ.get('DEDUCT_TOKEN','deduct_token')
WEBSITE_URL = 'http://website:3000'

def set_chrome_options() -> Options:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model, necessary for running in a container
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (may not be needed for headless mode)
    chrome_options.add_argument("--window-size=1920,1080") 
    chrome_options.add_argument('ignore-certificate-errors')
    chrome_options.add_argument("--allow-insecure-localhost") 

    return chrome_options

def clickElement(driver, element_id):
    try:
        # Wait for the element to be clickable
        element = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, element_id))
        )
        action = ActionChains(driver)
        action.move_to_element(element).click().perform()
    except Exception as e:
        print(f"Failed to click element with ID: {element_id}. Error: {e}")

class AdminBot:
    def __init__(self, base_url, ADMIN_TOKEN, DEDUCT_TOKEN):
        self.base_url = base_url
        self.ADMIN_TOKEN = ADMIN_TOKEN
        self.DEDUCT_TOKEN = DEDUCT_TOKEN
        self.driver = webdriver.Chrome(options=set_chrome_options())
        self.lock = threading.Lock()

        
    def login_as_admin(self,userToken):
        admin_url = f"{self.base_url}/admin/{self.ADMIN_TOKEN}/login?userToken={userToken}"
        self.driver.get(admin_url)
        clickElement(self.driver, 'login')
        print("Visited the /admin endpoint with authentication.")
        

    def visit(self, userToken, cart):
        self.driver.delete_all_cookies()

        with self.lock:
            self.login_as_admin(userToken)
            self.driver.add_cookie({'name': 'deductToken', 'value': self.DEDUCT_TOKEN})
            url = f"{self.base_url}/admin/{self.ADMIN_TOKEN}/shop"
            params = {"cart": json.dumps(cart)}

            self.driver.get(f"{url}?{urlencode(params)}")

            current_url_base = urlparse(self.driver.current_url).path
            intended_url_base = urlparse(url).path

            if current_url_base != intended_url_base:
                return "Failed to visit the shop page. Please Relogin."
            clickElement(self.driver, 'purchase')
            
            WebDriverWait(self.driver, 5).until(
                lambda d: d.find_element(By.ID, "result").text != ""
            )
            result_ele = self.driver.find_element(By.ID, "result")
            result_content = result_ele.text

            return result_content

    def close(self):
        self.driver.quit()

bot = AdminBot(WEBSITE_URL, ADMIN_TOKEN , DEDUCT_TOKEN)
@app.route('/visit', methods=['POST'])
def visit():
    # Get the Admin Bot to visit the requested page
    print(request.json)
    userToken = request.json.get('userToken', None)
    with open("debug.txt", "w") as f:
        f.write(str(userToken))
    cart = request.json.get('cart', None)
    userToken = str(userToken)
    if type(cart) != list:
        return jsonify({"error": "Cart is not a list"}), 400
    
    if not userToken:
        return jsonify({"error": "No URL provided"}), 400
    try:
        result = bot.visit(userToken,cart)
        return jsonify({"result":result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(port = 12345)
