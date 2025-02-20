# OSINT Downloader

OSINT Downloader is a Python-based tool that helps you easily clone various OSINT (Open-Source Intelligence) tools directly from GitHub repositories. It provides a simple interactive interface for selecting and cloning the repositories of popular OSINT tools.

## Features

- Clone various popular OSINT tools with ease.
- Checks if a tool is already cloned to avoid redundant cloning.
- Colorful and interactive terminal interface using `colorama`.
- Simple and clean Python script that automates the setup process.

## Tools Available

The following OSINT tools can be cloned:

1. **TheHarvester** - [GitHub Repository](https://github.com/laramies/theHarvester)
2. **Sherlock** - [GitHub Repository](https://github.com/sherlock-project/sherlock)
3. **Recon-ng** - [GitHub Repository](https://github.com/lanmaster53/recon-ng)
4. **Amass** - [GitHub Repository](https://github.com/OWASP/Amass)
5. **dnsrecon** - [GitHub Repository](https://github.com/darkoperator/dnsrecon)
6. **OSINT-ToolKit** - [GitHub Repository](https://github.com/dazz3d/OSINT-ToolKit)
7. **Github Dorks** - [GitHub Repository](https://github.com/techwhale/github-dorks)
8. **gitrob** - [GitHub Repository](https://github.com/michenriksen/gitrob)
9. **SpiderFoot** - [GitHub Repository](https://github.com/smicallef/spiderfoot)
10. **Crt.sh** - [GitHub Repository](https://github.com/gleeda/crt.sh)

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x
- Git (for cloning the repositories)

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/osintdownloader.git
    cd osintdownloader
    ```

2. Install the required Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

3. Make the script executable:

    ```bash
    chmod +x osintdownloader.py
    ```

4. Run the script:

    ```bash
    python osintdownloader.py
    ```

## Usage

1. When you run the script, a menu will display a list of available OSINT tools.
2. Select the number corresponding to the tool you want to clone.
3. The script will check if the tool is already cloned. If it is, it will notify you; otherwise, it will clone the repository.

## Example

```bash
$ python osintdownloader.py
Welcome by Lothbrok9
Initializing program...
Select an OSINT tool to clone:

1. TheHarvester
2. Sherlock
3. Recon-ng
4. Amass
5. dnsrecon
6. OSINT-ToolKit
7. Github Dorks
8. gitrob
9. SpiderFoot
10. Crt.sh

Enter the number of the tool you want to clone:
