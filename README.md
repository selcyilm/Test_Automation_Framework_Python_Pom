# Amazon Test Automation Project

This is a Selenium based test automation framework for Amazon's e-commerce website, implementing the Page Object Model design pattern.

## Project Structure

```
.
├── pages
│   ├── components
│   │   └── header_comp.py
│   ├── base_page.py
│   ├── cart_page.py
│   ├── home_page.py
│   ├── product_page.py
│   └── search_results_page.py
├── tests
│   ├── base_test.py
│   └── test_check_add_and_delete_cart_amazon.py
├── utils
│   └── driver_factory.py
├── README.md
├── config.json
└── requirements.txt
```

## Configuration

The framework can be configured through `config.json`:
- For browser selection, both "edge" and "chrome" are supported
- You can pre-define browser options such as headless mode or notification settings
- If you encounter timing/synchronization issues, enable the static-wait option to reduce test flakiness
```json
{
  "browser": "chrome",
  "base_url": "https://www.amazon.com.tr/",
  "timeout": 10,
  "options": {
    "headless-mode": false,
    "disable-notifications": true
  },
  "static-wait": {
    "enabled": false,
    "wait-time": 1
  }
}
```

## Setup And Installation
- Clone the repository
- Install dependencies via
```bash
pip install -r requirements.txt
```
- Configure test settings in config.json

## Run Test Cases

You can run it like this:
```bash
python -m unittest discover tests
```
> **Note**
> 
> If you run tests from PyCharm,
> leave the config path as is(config path is in base_test.py file).
> However, if you're running tests from the terminal,
> change the config path to "config.json"
