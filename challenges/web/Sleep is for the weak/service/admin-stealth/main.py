from __future__ import print_function
from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import threading
import os
import sys


FLAG = os.environ.get('FLAG', 'flag{test_flag}')
ADMIN_CREDS = os.environ.get('ADMIN_CREDS', 'admin_token')
WEBSITE_URL = os.environ.get('WEBSITE_URL', 'https://sleep-is-for-the-weak-website-chall.ybn.sg')
app = Flask(__name__)

def set_chrome_options() -> Options:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model, necessary for running in a container
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (may not be needed for headless mode)
    return chrome_options

class AdminBot:
    def __init__(self, base_url, auth_token,flag):
        self.base_url = base_url
        self.auth_token = auth_token
        self.flag = flag
        self.driver = webdriver.Chrome(options=set_chrome_options())
        self.lock = threading.Lock()


    def visit_url(self, uuid):
        self.driver.delete_all_cookies()
        with self.lock:
            self.driver.get(self.base_url)
            self.driver.add_cookie({
                'name': 'auth_token',
                'value': self.auth_token,
                'path': '/',
                'httpOnly': True
            })
            self.driver.add_cookie({
                'name': 'uuid',
                'value': uuid,
                'path': '/',
                'httpOnly': True
            })
            self.driver.add_cookie({
                'name': 'flag',
                'value': self.flag,
                'path': '/',
                'httpOnly': False
            })
            self.driver.refresh()
            self.driver.get(f"{self.base_url}/backend/admin_login.php")
            self.driver.implicitly_wait(5)
            print("Visited the admin endpoint with authentication.", file=sys.stderr)

            self.driver.get(f"{self.base_url}?page=sleep&limit=5")
            # print contents of the page
            print(self.driver.page_source, file=sys.stderr)
            self.driver.implicitly_wait(10)
            return "Excellent schedule. We are one step closer to a sleepless society."

    def close(self):
        self.driver.quit()

bot = AdminBot(WEBSITE_URL, ADMIN_CREDS,FLAG)
# configure JSON
@app.route('/visit', methods=['POST'])
def visit():
    # Get the Admin Bot to visit the requested page
    data = request.get_json()
    if not data or 'uuid' not in data:
        return jsonify({"error": "No data provided."}), 400
    try:
        print("ran", file=sys.stdout)
        result = bot.visit_url(data['uuid'])
        return jsonify({"data":result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/test', methods=['GET'])
def test():
    return jsonify({"data":"Test"}), 200

if __name__ == '__main__':
    app.run( port = 12345)
