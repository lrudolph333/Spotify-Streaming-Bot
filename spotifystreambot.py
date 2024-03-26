#!/usr/bin/env python3
import logging
import os
import random
import time
import webbrowser

# import keyboard
import pytz
from colorama import Fore
from pystyle import Center, Colorate, Colors
from selenium.common.exceptions import NoSuchElementException
# to add capabilities for chrome and firefox, import their Options with different aliases
from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from seleniumwire import webdriver
# import webdriver for downloading respective driver for the browser
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# import requests



# from .driver_initialization import Initializer


# os.system(f"title Kichi779 - Spotify Streaming bot v1 ")

url = "https://github.com/Kichi779/Spotify-Streaming-Bot/"

# def check_for_updates():
#     try:
#         r = requests.get("https://raw.githubusercontent.com/Kichi779/Spotify-Streaming-Bot/main/version.txt")
#         remote_version = r.content.decode('utf-8').strip()
#         local_version = open('version.txt', 'r').read().strip()
#         if remote_version != local_version:
#             print(Colors.red, Center.XCenter("A new version is available. Please download the latest version from GitHub"))
#             time.sleep(2)
#             webbrowser.open(url)
#             return False
#         return True
#     except:
#         return True

# def print_announcement():
#     try:
#         r = requests.get("https://raw.githubusercontent.com/Kichi779/Spotify-Streaming-Bot/main/announcement.txt", headers={"Cache-Control": "no-cache"})
#         announcement = r.content.decode('utf-8').strip()
#         return announcement
#     except:
#         print("Could not retrieve announcement from GitHub.\n")

supported_timezones = pytz.all_timezones




logger = logging.getLogger(__name__)
format = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch = logging.StreamHandler()
ch.setFormatter(format)
logger.addHandler(ch)

user_agents = [
# Chrome (Windows)
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",

# Chrome (Mac)
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",

# Firefox (Windows)
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",

# Firefox (Mac)
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:93.0) Gecko/20100101 Firefox/93.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 11.4; rv:93.0) Gecko/20100101 Firefox/93.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:93.0) Gecko/20100101 Firefox/93.0",

# Safari (Mac)
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",

# Opera (Windows)
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 OPR/80.0.4170.61",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 OPR/80.0.4170.61",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 OPR/80.0.4170.61"
]

#FAKE Language
supported_languages = [
"en-US", "en-GB", "en-CA", "en-AU", "en-NZ", "fr-FR", "fr-CA", "fr-BE", "fr-CH", "fr-LU",
"de-DE", "de-AT", "de-CH", "de-LU", "es-ES", "es-MX", "es-AR", "es-CL", "es-CO", "es-PE",
"it-IT", "it-CH", "ja-JP", "ko-KR", "pt-BR", "pt-PT", "ru-RU", "tr-TR", "nl-NL", "nl-BE",
"sv-SE", "da-DK", "no-NO"
]

random_user_agent = random.choice(user_agents)


class Initializer:

    def __init__(self, browser_name, proxy=None, headless=True):
        self.browser_name = browser_name
        self.proxy = proxy
        self.headless = headless

    def set_properties(self, browser_option):
        """adds capabilities to the driver"""
        # if self.headless:
        #     browser_option.add_argument(
        #         '--headless')  # runs browser in headless mode
        browser_option.add_argument('--no-sandbox')
        browser_option.add_argument("--disable-dev-shm-usage")
        browser_option.add_argument('--ignore-certificate-errors')
        browser_option.add_argument('--disable-gpu')
        browser_option.add_argument('--log-level=3')
        browser_option.add_argument('--disable-notifications')
        browser_option.add_argument('--disable-popup-blocking')
        random_language = random.choice(supported_languages)

        browser_option = webdriver.ChromeOptions()
        browser_option.add_experimental_option('excludeSwitches', ["enable-automation", 'enable-logging', "disable-popup-blocking"])
        browser_option.add_argument('--disable-logging')
        # browser_option.add_argument('--log-level=3')
        browser_option.add_argument('--disable-infobars')
        browser_option.add_argument('--disable-extensions')
        browser_option.add_argument("--window-size=1366,768")
        browser_option.add_argument("--lang=en-US,en;q=0.9")
        browser_option.add_argument("--disable-notifications")
        # browser_option.add_argument(f"--user-agent={random_user_agent}")
        browser_option.add_argument(f"--lang={random_language}")
        browser_option.add_argument("--mute-audio")
        browser_option.add_argument('--disable-dev-shm-usage')
        browser_option.add_experimental_option('prefs', {
            'profile.default_content_setting_values.notifications': 2
        })
        browser_option.add_argument("--user-data-dir=/Users/godye/Library/Application Support/Google/Chrome/Profile 1")

        # Set preferences to block pop-ups
        prefs = {
            "profile.default_content_setting_values.popups": 2,  # Block pop-ups
            "profile.default_content_setting_values.notifications": 2  # Block notifications
        }
        browser_option.add_experimental_option("prefs", prefs)
    
        return browser_option

    def set_driver_for_browser(self, browser_name):
        """expects browser name and returns a driver instance"""
        logger.setLevel(logging.INFO)
        # if browser is suppose to be chrome
        if browser_name.lower() == "chrome":
            browser_option = ChromeOptions()
            # automatically installs chromedriver and initialize it and returns the instance
            if self.proxy is not None:
                options = {
                    'https': 'https://{}'.format(self.proxy.replace(" ", "")),
                    'http': 'http://{}'.format(self.proxy.replace(" ", "")),
                    'no_proxy': 'localhost, 127.0.0.1'
                }
                logger.info("Using: {}".format(self.proxy))
                return webdriver.Chrome(executable_path="/Applications/chrome/mac_arm-121.0.6167.85/chrome-mac-arm64/Google Chrome for Testing.app",
                # return webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                        options=self.set_properties(browser_option), seleniumwire_options=options)

            return webdriver.Chrome(executable_path="/Users/godye/github/Spotify-Streaming-Bot/chromedriver-mac-arm64/chromedriver", options=self.set_properties(browser_option))
            # return webdriver.Chrome(executable_path="/Applications/chrome/mac_arm-121.0.6167.85/chrome-mac-arm64/Google Chrome for Testing.app", options=self.set_properties(browser_option))
            # return webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=self.set_properties(browser_option))
        elif browser_name.lower() == "firefox":
            browser_option = FirefoxOptions()
            if self.proxy is not None:
                options = {
                    'https': 'https://{}'.format(self.proxy.replace(" ", "")),
                    'http': 'http://{}'.format(self.proxy.replace(" ", "")),
                    'no_proxy': 'localhost, 127.0.0.1'
                }
                logger.info("Using: {}".format(self.proxy))
                return webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                         options=self.set_properties(browser_option), seleniumwire_options=options)

            # automatically installs geckodriver and initialize it and returns the instance
            return webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=self.set_properties(browser_option))
        else:
            # if browser_name is not chrome neither firefox than raise an exception
            raise Exception("Browser not supported!")

    def init(self):
        """returns driver instance"""
        driver = self.set_driver_for_browser(self.browser_name)
        return driver


def set_random_timezone(driver):
    random_timezone = random.choice(supported_timezones)
    driver.execute_cdp_cmd("Emulation.setTimezoneOverride", {"timezoneId": random_timezone})

def set_fake_geolocation(driver, latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "accuracy": 100
    }
    driver.execute_cdp_cmd("Emulation.setGeolocationOverride", params)

def main():
    # if not check_for_updates():
    #     return
#     announcement = print_announcement()
    print(Colorate.Vertical(Colors.white_to_green, Center.XCenter("""
           
                       ▄█   ▄█▄  ▄█    ▄████████    ▄█    █▄     ▄█  
                       ███ ▄███▀ ███   ███    ███   ███    ███   ███  
                       ███▐██▀   ███▌  ███    █▀    ███    ███   ███▌ 
                      ▄█████▀    ███▌  ███         ▄███▄▄▄▄███▄▄ ███▌ 
                     ▀▀█████▄    ███▌  ███        ▀▀███▀▀▀▀███▀  ███▌ 
                       ███▐██▄   ███   ███    █▄    ███    ███   ███  
                       ███ ▀███▄ ███   ███    ███   ███    ███   ███  
                       ███   ▀█▀ █▀    ████████▀    ███    █▀    █▀   
                       ▀                                             
 Improvements can be made to the code. If you're getting an error, visit my discord.  
                             Github  github.com/kichi779    """)))
    print("")
    # print(Colors.red, Center.XCenter("ANNOUNCEMENT"))
    # print(Colors.yellow, Center.XCenter(f"yellows"))
    # print(Colors.yellow, Center.XCenter(f"{announcement}"))
    print("")


    with open('accounts.txt', 'r') as file:
        accounts = file.readlines()

    # TODO consider using proxies, or connect to nordvpn/windscribe api
    # proxies = []

    # use_proxy = input(Colorate.Vertical(Colors.green_to_blue, "Do you want to use proxies? (y/n):"))

    # if use_proxy.lower() == 'y':  
    #     print(Colors.red, Center.XCenter("The proxy system will be added after 50 stars. I continue to process without a proxy"))
    #     with open('proxy.txt', 'r') as file:
    #         proxies = file.readlines()
    #     time.sleep(3)

    spotify_song = "https://open.spotify.com/track/1dzWH11jyP8gEQia6rZv7f?si=122335bd4f0e434c" #so waht
    # spotify_song = "https://open.spotify.com/track/6efkcs2aUBMFKxl0cl2JWQ?si=67a92459bdb9445c" #wild irish
    # spotify_song = input(Colorate.Vertical(Colors.green_to_blue, "Enter the Spotify song URL (e.g https://open.spotify.com/track/5hFkGfx038V0LhqI0Uff2J?si=bf290dcc9a994c36):"))

    drivers = []

    delay = random.uniform(2, 6)
    delay2 = random.uniform(5, 14)
    stream_count = 0
    driver =  Initializer("chrome").init()

    while stream_count < 1000:
        for account in accounts:

        
            # driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

            username, password = account.strip().split(':')

            try:
                driver.get("https://www.spotify.com/us/login/")
                try:
                    username_input = driver.find_element(By.CSS_SELECTOR, "input#login-username")
                    password_input = driver.find_element(By.CSS_SELECTOR, "input#login-password")

                    username_input.send_keys(username)
                    password_input.send_keys(password)

                    driver.find_element(By.CSS_SELECTOR, "button[data-testid='login-button']").click()
                except NoSuchElementException:
                    # print("no login element")
                    time.sleep(2)
                time.sleep(delay)

                driver.get(spotify_song)

                driver.maximize_window()

                # keyboard.press_and_release('esc')

                time.sleep(3)

                try:
                    cookie = driver.find_element(By.XPATH, "//button[text()='Accept Cookies']")
                    cookie.click()
                except NoSuchElementException:
                    try:
                        button = driver.find_element(By.XPATH, "//button[contains(@class,'onetrust-close-btn-handler onetrust-close-btn-ui')]")
                        button.click()
                    except NoSuchElementException:
                        time.sleep(delay2)

                time.sleep(2)
                # playmusic_xpath = "(//button[@data-testid='play-button']//span)[3]"
                # # playmusic_xpath = "(//button[@data-testid='play-button']//span)[3]"
                # playmusic = driver.find_element(By.XPATH, playmusic_xpath)
                # playmusic.click()
                play_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Play']")
                # play_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='play-button']")
                play_button.click()
                play_duration = random.uniform(35, 45)

                print("playing So What for {} seconds...".format(play_duration))

                # wait for the song to finish
                time.sleep(play_duration)

                print("Username: {} - Listening process has finished, count: {}\n".format(username, stream_count))

                # Before ending the iteration, open a new tab
                driver.execute_script("window.open('about:blank', 'secondtab');")
                # Switch to the new tab, which will be at index 1
                driver.switch_to.window(driver.window_handles[1])
                # Close the other tab, which will be at index 0
                driver.close()
                # Switch back to the first tab, now the only tab
                driver.switch_to.window(driver.window_handles[0])
            except Exception as e:
                print("An error occurred in the bot system:", str(e))

            # TODO reimplement these
            # set_random_timezone(driver)
            
            # # FAKE LOCATION
            # latitude = random.uniform(-90, 90)
            # longitude = random.uniform(-180, 180)
            # set_fake_geolocation(driver, latitude, longitude)
            finally:
                # Consider moving driver appending here if you wish to keep it for later use
                # drivers.append(driver)
                stream_count += 1
                pass
            time.sleep(5)

    print(Colors.blue, "Stream operations are completed. You can stop all transactions by closing the program.")

    while True:
        pass

if __name__ == "__main__":
    main()


# ==========================================
# Copyright 2023 Kichi779

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ==========================================
