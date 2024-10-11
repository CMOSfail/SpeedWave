
# SpeedWave

## Overview
SpeedWave is a simple Python application that allows users to test their internet download speed, upload speed, and ping (latency) through either a command-line interface (CLI) or a graphical user interface (GUI). It also allows for logging these results into a file.

## Requirements
- Python 3.x
- Required Python packages are listed in `requirements.txt`.

## How to Install and Run

1. **Install the dependencies:**

    First, install the required packages using the following command:
    ```
    pip install -r requirements.txt
    ```

2. **Run the script:**

    Start the application by running the `main.py` script:
    ```
    python main.py
    ```

3. **Choose between CLI or GUI:**

    - Enter `cli` to run the application in the command-line interface.
    - Enter `gui` to run the application in the graphical interface.

## Features
- **Single-threaded speed test**: Allows you to perform a single-threaded speed test (both in CLI and GUI).
- **Multi-threaded speed test**: Allows you to perform a multi-threaded speed test (both in CLI and GUI).
- **Logging results**: Speed test results (download, upload, ping) can be logged to a `speedtest_results.log` file.
- **Icon Support**: The GUI features a custom icon located in `resources/icons/icon.ico`.

## Logging
If you choose to log the results, a `speedtest_results.log` file will be created in the same directory, recording the download speed, upload speed, and ping for each test.

## Error Handling
The script includes error handling for network issues or unexpected errors and will provide informative messages in case something goes wrong.
