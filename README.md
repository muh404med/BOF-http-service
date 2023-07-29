
# Exact Offset Finder

This Python script helps find the exact offset number that can potentially cause a service crash example "Sync Breeze Enterprise v10.0.28" .
The tool utilizes a buffer overflow technique to determine the offset where the service crashes, without requiring the msf-passtern tool.

## Requirements

- Python 3.x

## How to Use

1. Start the target service that you want to test for buffer overflow vulnerabilities.

2. Obtain the nearly offset number:
   - Run the script and input "1" when prompted. This will make requests with incremental offsets (100, 200, 300, ...) until the service crashes.
   - You get will 'nearly offset number' copy it , 

    Note 
    nearly offset number : the last successful offset before the service crashes.

3. Run the script again and input "2" when prompted. Then, enter the 'nearly offset number' obtained in the previous step.

4. The script will run additional tests to find the exact offset that crashes the service. Once found, the script will stop, and the exact offset number will be displayed.

## How the Script Works

The script uses a simple network communication approach to send crafted payloads to the target service.
It iteratively increases the payload size (offset) until the service crashes.
Then, it narrows down the exact offset by making additional requests.

