<!--  -->
# Day 3 — Web Scraping & Web Automation (Python)

## What I Learned Today

This document summarizes everything I studied and practiced about **Web Scraping and Web Automation** using Python.

---

## 1. What is Web Scraping?

Web Scraping means **extracting data from websites** automatically using code.

### Characteristics

* Works on **static websites**
* Data is available directly in HTML
* No browser UI is required
* Faster than browser automation

### Common Use Cases

* Scraping news headlines
* Extracting quotes, blogs, articles
* Collecting product names and prices
* Creating datasets for analysis / AI

---

## 2. Tools Used for Web Scraping

### requests

Used to send HTTP requests and fetch webpage HTML.

```python
import requests
response = requests.get("https://example.com")
print(response.text)
```

### BeautifulSoup

Used to parse and extract data from HTML.

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")
print(soup.title.text)
```

---

## 3. Common Scraping Operations

### Extract Links

```python
for link in soup.find_all("a"):
    print(link.get("href"))
```

### Extract Text

```python
for p in soup.find_all("p"):
    print(p.text)
```

### Example: Scraping Headlines

```python
import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com"
soup = BeautifulSoup(requests.get(url).text, "html.parser")

titles = soup.find_all("a", class_="storylink")
for t in titles:
    print(t.text)
```

---

## 4. Limitations of Web Scraping

Web Scraping does not work well when:

* Content is loaded using JavaScript
* Login is required
* Buttons need to be clicked

For such cases, **Web Automation** is required.

---

## 5. What is Web Automation?

Web Automation means **automatically controlling a real browser** to perform actions like a human.

### Examples

* Auto login
* Auto search
* Clicking buttons
* Scrolling pages
* Extracting dynamically loaded data

---

## 6. Tool Used for Web Automation

### Selenium

* Controls a real browser (Chrome)
* Supports JavaScript websites
* Can perform clicks, typing, scrolling

Installation:

```bash
pip install selenium
```

---

## 7. Selenium Basics (What I Learned)

### Open Browser

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://google.com")
```

### Locate Elements and Perform Actions

```python
from selenium.webdriver.common.by import By

search = driver.find_element(By.NAME, "q")
search.send_keys("Python automation")
search.submit()
```

### Wait for Page Load

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, "//h3")))
```

### Scroll Page

```python
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
```

### Extract Data

```python
titles = driver.find_elements(By.XPATH, "//h3")
for t in titles:
    print(t.text)
```

---

## 8. Mini Project Completed

### Google Auto Search & Result Extraction

Features:

* Open Google
* Search query automatically
* Scroll page
* Extract result titles
* Close browser

This project helped me understand **basic Selenium automation**.

---

## 9. Ethics and Responsibility

* Always check `robots.txt`
* Respect website terms & conditions
* Avoid scraping private or sensitive data

---

## 10. Summary

Today I learned:

* Difference between Web Scraping and Web Automation
* Scraping static websites using `requests` and `BeautifulSoup`
* Basic Selenium automation
* Handling dynamic content
* Building small automation scripts

---

## Next Step

➡️ **Day 4 — SQL Basics & Python Database Automation**
