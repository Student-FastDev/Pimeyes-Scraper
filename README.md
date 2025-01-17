# Pimeyes-Scraper

**Pimeyes-Scraper** is a Python-based tool that leverages Selenium for automated web scraping, specifically designed to interact with the [Pimeyes](https://pimeyes.com/) website. This script includes robust proxy support to ensure anonymity and efficiency during scraping tasks.

## Features

- **Automated Image Search:** Seamlessly upload images to Pimeyes and initiate reverse image searches.
- **Result Extraction:** Scrape and store search results for further analysis or record-keeping.
- **Proxy Support:** Utilize proxies to mask IP addresses, enhancing privacy and preventing IP bans.
- **Bulk Processing:** Handle multiple image searches in automated scenarios, improving productivity.
- **Image Management:** Automatically delete image files after processing to maintain a clean workspace.
- **Error Handling:** Robust mechanisms to handle common scraping issues and ensure smooth operation.

## Prerequisites

Before setting up the **Pimeyes-Scraper**, ensure you have the following installed:

- **Python:** Version 3.6 or higher. [Download Python](https://www.python.org/downloads/)
- **Google Chrome:** Latest version recommended for compatibility with ChromeDriver. [Download Chrome](https://www.google.com/chrome/)
- **Git:** For cloning the repository. [Download Git](https://git-scm.com/downloads)
- **Proxies:** A list of working proxies in the format `IP:PORT:USER:PASS` for anonymity (optional but recommended).

## Installation

1. **Clone the Repository:**

    ```sh
    git clone https://github.com/Student-FastDev/Pimeyes-Scraper/
    cd Pimeyes-Scraper
    ```

2. **Install Required Packages:**

    Install the necessary Python packages using `pip`:

    ```sh
    pip install -r requirements.txt
    ```

3. **Set Up WebDriver:**

    Ensure that the Chrome WebDriver version matches your installed Google Chrome version. You can download the appropriate WebDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

    - **Add WebDriver to PATH:**

      Place the downloaded `chromedriver` executable in a directory that's included in your system's PATH, or specify its location in the script if necessary.

## Usage

### Running the Script

Execute the script from the command line, specifying the image file you wish to search:

```bash
python pimeyes.py [image_file_name]
```

**Example:**

```bash
python pimeyes.py sample_image.jpg
```

### Configuration

1. **Proxy Configuration:**

    To enhance anonymity and prevent IP bans, configure proxies by editing the `proxy.txt` file:

    ```plaintext
    IP:PORT:USER:PASS
    ```

    **Example:**

    ```plaintext
    192.168.1.100:8080:username:password
    203.0.113.50:3128:proxyuser:proxypass
    ```

    The script randomly selects a proxy from this file for each session, ensuring varied IP addresses for different scraping tasks.

2. **Image Management:**

    After processing, the script automatically deletes the image file to maintain a clean directory. Ensure that the image file you want to search is located in the same directory as the script or provide the correct path.

3. **Settings Adjustment:**

    If the script generates a `settings.json` file upon first run, review and adjust any configurable parameters as needed.

    ```json
    {
        "search_delay": 5,
        "max_retries": 3,
        "headless": true
    }
    ```

    - **search_delay:** Time in seconds to wait between searches.
    - **max_retries:** Number of retry attempts for failed searches.
    - **headless:** Set to `true` to run the browser in headless mode.

## Notes

- **Asynchronous Efficiency:** While the current version uses Selenium for automation, future updates may incorporate asynchronous programming to handle multiple searches concurrently, further enhancing efficiency.
  
- **Proxy Reliability:** Using high-quality and reliable proxies is crucial to prevent IP bans and ensure smooth operation.
  
- **Security:** Handle your proxy information securely to prevent unauthorized access.
  
- **Compliance:** Ensure that your usage of the bot complies with Pimeyes' [Terms of Service](https://pimeyes.com/legal) to avoid potential legal issues.

---

<div align="center">  
    <img src="https://s3-eu-west-1.amazonaws.com/tpd/logos/60910dd62ebaea0001d6f783/0x0.png" alt="Pimeyes Logo" width="80px">
</div>
