#screenshot.py

from selenium import webdriver
from PIL import Image

# Function to capture screenshot of a webpage
def capture_screenshot(url, output_file):
    # Initialize Chrome WebDriver (you need chromedriver installed)
    driver = webdriver.Chrome()
    
    # Open URL
    driver.get(url)
    
    # Capture viewport screenshot
    screenshot = driver.get_screenshot_as_png()
    
    # Save screenshot to file
    with open(output_file, 'wb') as f:
        f.write(screenshot)
    
    # Close the browser
    driver.quit()

# Example usage
if __name__ == "__main__":
    url = "https://example.com"  # Replace with your desired URL
    output_file = "screenshot.png"
    capture_screenshot(url, output_file)
    print(f"Screenshot saved to {output_file}")

