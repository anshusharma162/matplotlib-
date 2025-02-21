from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Replace with your ChromeDriver path
service = Service("C:/Users/DELL/OneDrive/Desktop/anshu/chromedriver.exe")  # Update the path if needed

# Start WebDriver
driver = webdriver.Chrome(service=service)

# Target number and message
phone_number = "8923121949"  # Replace with the target number
message = "Hello, this is a test message!"  # Replace with your message
count = 10000  # Number of times to send the message

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")
print("Scan the QR code to log in to WhatsApp Web")
time.sleep(15)  # Wait for QR code to scan

# Open chat with the target number
driver.get(f"https://web.whatsapp.com/send?phone=+91{phone_number}")
time.sleep(10)  # Wait for the chat to load

# Send the message multiple times
for i in range(count):
    try:
        message_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@data-tab='10']")
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        print(f"Message {i + 1} sent")
        time.sleep(0.5)  # Wait 0.5 seconds between messages
    except Exception as e:
        print(f"Error occurred at message {i + 1}: {e}")
        break

# Close the browser
driver.quit()
