# Pimeyes-Scraper

Tool specifically designed to interact with the Pimeyes website.

## Prerequisites

To run the Pimeyes-Scraper script, ensure you have the following installed:

- **Python:** Version 3.6 or higher.
- **Google Chrome:** Latest version recommended for compatibility with ChromeDriver.
- **Git:** For cloning the repository.
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

## Usage

1. **Run the Python Script:**

    Execute the script from the command line, specifying the image file you wish to search:

    ```bash
    python pimeyes.py [image_file_name]
    ```

2. **Configure Settings:**

    After running the program for the first time, a `settings.json` file will be generated. Open this file in a text editor to customize your settings:

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

- **Proxy Configuration:** Utilize proxies to mask IP addresses and prevent IP bans. Configure proxies by adding them to a `proxy.txt` file in the format `IP:PORT:USER:PASS`, one per line. The script randomly selects a proxy for each session.
- **Compliance & Security:** Handle your proxy information securely to prevent unauthorized access. Ensure that your usage of the bot complies with Pimeyes' Terms of Service to avoid potential legal issues.

---

<div align="center">  
    <img src="https://upload.wikimedia.org/wikipedia/commons/3/33/Pimeyes-logo.png?_=20230210185416" alt="Pimeyes Logo" width="80px">
</div>
