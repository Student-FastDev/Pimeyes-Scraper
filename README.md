# Pimeyes-Scraper

Pimeyes-Scraper is a Python-based tool utilizing Selenium for automated web scraping, specifically designed to interact with the Pimeyes website. This script includes proxy support.

## Table of Contents
- [Introduction](#introduction)
  - [Functionality](#functionality)
  - [Safety and Privacy](#safety-and-privacy)
- [Setup Guide](#setup-guide)
  - [System Requirements](#system-requirements)
  - [Installation Steps](#installation-steps)
- [Usage](#usage)
  - [Running the Script](#running-the-script)
  - [Configuration](#configuration)
- [Proxy Configuration](#proxy-configuration)

## Introduction

### Functionality

Pimeyes-Scraper automates tasks on the Pimeyes website using Selenium. The script's key feature is its ability to easily grab the results from Pimeyes website.

### Safety and Privacy

While designed with safety in mind, users should responsibly manage proxies and respect the terms of service of websites they interact with.

## Setup Guide

### System Requirements

Ensure the following are installed:
- Google Chrome
- Python
- Git

### Installation Steps

1. Clone the repository:

   ```
   git clone https://github.com/YourUsername/Pimeyes-Scraper
   ```

2. Navigate to the directory:

   ```
   cd Pimeyes-Scraper
   ```

3. Install required Python packages:

   ```
   pip install -r requirements.txt
   ```

## Usage

### Running the Script

Execute the script from the command line:

```bash
python main.py
```

### Configuration

On the first run, edit `settings.json`:

```json
{
    "proxy_file": "proxy.txt",
    "use_proxy": true,
    "headless_mode": true
}
```

## Proxy Configuration

Manage your proxies through `proxy.txt`. The script randomly selects a proxy from this file for each session, ensuring varied IP addresses for different scraping tasks.
