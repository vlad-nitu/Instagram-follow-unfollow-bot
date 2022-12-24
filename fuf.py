from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random
import time

def sleep_for_period_of_time():
    limit = random.randint(2,5)
    time.sleep(limit)

def scroll_through_all_followers(driver):
    SCROLL_PAUSE_TIME = 3

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

user = input("Enter your username: ")
pwd = input("Enter your password: ")

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=en")
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    browser.get("https://www.instagram.com")
    time.sleep(5)

    cookies_button = browser.find_element(By.XPATH, "//button[@class='_a9-- _a9_0']")
    cookies_button.click()
    sleep_for_period_of_time()

    username_input = browser.find_element(By.CSS_SELECTOR, "input[name='username']")
    password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")

    username_input.send_keys(user)
    password_input.send_keys(pwd)
    sleep_for_period_of_time()

    login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    sleep_for_period_of_time()

    # not_now = browser.find_element_by_xpath("//div[@class='cmbtv']/button")
    # not_now.click()
    # sleep_for_period_of_time()

    page_ig = input("Enter page username: ")
    browser.get(f"https://www.instagram.com/{page_ig}")
    sleep_for_period_of_time()

    followers_link = browser.find_element(By.XPATH, "//ul/li[2]/a")
    followers_link.click()
    sleep_for_period_of_time()


    num_follow = input("How many person you want to follow: ")

    while(True):
        try:
            i = 0
            list_of_followers = browser.find_elements(By.XPATH, '//button/div/div[contains(text(), "Follow") or contains(text(), "Requested")]')
            ActionChains(browser).move_to_element(list_of_followers[0]).perform()
            scroll_through_all_followers(browser)
            print("There are" + str(len(list_of_followers)) + "followers for this profile")
            for person in list_of_followers:
                if person.text == "Follow":
                    person.click()
                    print("Followed!")
                    i += 1
                    print(i)
                    sleep_for_period_of_time()
                else:
                    continue
                if i >= int(num_follow):
                    break

            browser.execute_script("arguments[0].scrollIntoView(true);", list_of_followers[i])

            answer = input("The programm finished! Click on 'e' to exit.. ")
            if answer.lower().startswith("e"):
                browser.quit()
                exit()

        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()

