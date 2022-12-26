from selenium import webdriver
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

    # not_now = browser.find_element_by_xpath("//div[@class='cmbtv']/button")
    # not_now.click()
    # sleep_for_period_of_time()

    ig_user = input("Enter your instagram username: ")
    browser.get(f"https://www.instagram.com/{ig_user}")
    sleep_for_period_of_time(5, 10)

    browser.find_element(By.PARTIAL_LINK_TEXT, "following").click()
    sleep_for_period_of_time(2, 4)

    num_unfollow = input("How many person you want to unfollow: ")
    sleep_for_period_of_time(2, 4)

    pop_up_window = browser.find_element(By.XPATH, "//div[@class='_aano']")
    i = 0

    while True:
        try:

            list_of_following = browser.find_elements(By.XPATH, '//button/div/div[contains(text(), "Following")]')
            for person in list_of_following:
                if person.text == "Following":
                    person.click()
                    time.sleep(5)
                    unfollow_btn = browser.find_element(By.XPATH, '//button[text()= "Unfollow"]')
                    unfollow_btn.click()
                    print("Unfollowed!")
                    i += 1
                    print(i)
                    sleep_for_period_of_time(3, 10) # larger
                else:
                    pass
            if i >= int(num_unfollow):
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

