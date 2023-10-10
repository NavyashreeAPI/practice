from datetime import datetime
def take_screenshot(driver):
    date=datetime.now()
    d=date.strftime("%d-%m-%y %H-%M-%S")
    driver.save_screenshot(f"../screenshot/{d}.png")