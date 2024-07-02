# Test
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random
import time

def sleep_for_period_of_time(a, b):
    limit = random.randint(a, b)
    time.sleep(limit)


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
    sleep_for_period_of_time(5, 10)

    username_input = browser.find_element(By.CSS_SELECTOR, "input[name='username']")
    password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")

    username_input.send_keys(user)
    password_input.send_keys(pwd)
    sleep_for_period_of_time(2, 4)

    login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    sleep_for_period_of_time(2, 4)


    page_ig = input("Enter page username: ")
    browser.get(f"https://www.instagram.com/{page_ig}")
    sleep_for_period_of_time(5, 10)

    num_follow = input("How many person you want to follow: ")

    browser.find_element(By.PARTIAL_LINK_TEXT, "followers").click()
    sleep_for_period_of_time(2, 4)

    pop_up_window = browser.find_element(By.XPATH, "//div[@class='_aano']")

    followed = 0

    while True:
        try:
            list_of_followers = browser.find_elements(By.XPATH, '//button/div/div[contains(text(), "Follow")]')

            print(len(list_of_followers))

            for person in list_of_followers:
                if person.text == "Follow":

                    print(person)

                    retries = 0
                    max_retries = 10
                    while retries < max_retries:
                        try:
                            person.click()
                            break
                        except ElementClickInterceptedException as e:
                            print("Click intercepted, retrying...")
                            time.sleep(2)  # Wait for a second before retrying
                            retries += 1

                    if (retries < max_retries):
                        print("Followed!")
                        followed += 1
                        print(followed)
                        sleep_for_period_of_time(40, 60)
                    else:
                        print("Was not able to click")
                else:
                    pass

            if followed >= int(num_follow):
                break
            else:
                browser.execute_script(
                    'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                    pop_up_window)
                time.sleep(1)
        except Exception as e:
            print(e)


    answer = input("The program finished! Click on 'e' to exit.. ")
    if answer.lower().startswith("e"):
        browser.quit()
        exit()


if __name__ == "__main__":
    main()

