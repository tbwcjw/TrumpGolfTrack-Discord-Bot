from io import BytesIO
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import config
from lang import i8ln


class TrumpGolfTrack:
    def __init__(self, days_in_office, days_spent_golfing, time_spent_golfing, since, days):
        self.days_in_office = days_in_office
        self.days_spent_golfing = days_spent_golfing
        self.time_spent_golfing = time_spent_golfing
        self.since = since
        self.days = sorted(days)

    @classmethod
    async def fetch(cls):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        service = Service(config.CHROME_DRIVER_PATH) 
        driver = webdriver.Chrome(service=service, options=chrome_options)
        try:
            driver.get(config.URL_PATH)

            days_in_office = int(driver.find_element(By.CSS_SELECTOR, "main .grid div:nth-child(1) > p:nth-child(2)").text)
            days_spent_golfing = int(driver.find_element(By.CSS_SELECTOR, "main .grid div:nth-child(2) > p:nth-child(2)").text)
            time_spent_golfing = float(driver.find_element(By.CSS_SELECTOR, "main .grid div:nth-child(3) > p:nth-child(2)").text.strip('%'))
            
            #wait until graphs animate fully
            wait = WebDriverWait(driver, 10)
            #double check this the next time the site updates, is nth-child(7) always the last graph marker?
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "main div.flex:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > svg:nth-child(1) > g:nth-child(4) > g:nth-child(3) > circle:nth-child(7)"))) 
            
            #take screenshot of graphs
            graphs = driver.find_element(By.CSS_SELECTOR, "main .grid-cols-2")
            screenshot = driver.get_screenshot_as_png()
            location = graphs.location
            size = graphs.size
            image = Image.open(BytesIO(screenshot))
            left = location['x']                    # annoying evil shit
            top = location['y'] + 64                # offset 64
            right = left + size['width'] + 256      # offset 256
            bottom = top + size['height'] + 50      # offset 50
            cropped_image = image.crop((left, top, right, bottom))
            cropped_image.save(config.GRAPHS_SAVE_PATH)

            since_text = driver.find_element(By.CSS_SELECTOR, "main .grid div:nth-child(1) > p:nth-child(3)").text
            since = datetime.strptime(since_text.strip("Since "), "%B %d, %Y").date()

            days_elements = driver.find_elements(By.CSS_SELECTOR, "main .container:nth-child(2) ul li p:nth-child(1)")
            days = [datetime.strptime(el.text, "%m/%d/%Y").date() for el in days_elements]

            driver.quit()
        except Exception as e:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error occurred while fetching data: {e}")
        finally:
            driver.quit()

        return cls(days_in_office, days_spent_golfing, time_spent_golfing, since, days)

    def to_dict(self):
        return {
            f"🕓 {i8ln('days_in_office')}": self.days_in_office,
            f"👎 {i8ln('president_since')}": self.since,
            f"🏌️‍♂️ {i8ln('days_spent_golfing')}": self.days_spent_golfing,
            f"📈 {i8ln('perc_spent_golfing')}": f"{self.time_spent_golfing}%",
            f"📆 {i8ln('days_golfed_on')}": ", ".join(f"{day}" for day in self.days)
        }
