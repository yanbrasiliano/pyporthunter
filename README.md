
# pyPortHunter

### Description
`pyPortHunter` is a lightweight Python-based port scanner designed to help you identify open ports on a host or network. This tool allows you to scan a range of ports to detect active services, providing insights for security assessments or network troubleshooting.

### Features
- Scan specific ports or a range of ports.
- Option to scan using TCP or UDP protocols.
- Fast or comprehensive scans depending on port range.
- Displays a report of open ports at the end.
- Simple and easy-to-use interface.

### Requirements
Before running `pyPortHunter`, ensure you have Python installed. This project has been tested with Python 3.7 and above.

You will also need the following Python libraries:
- `socket`
- `argparse`

You can install additional dependencies using pip:

```bash
pip install -r requirements.txt
```

### Usage
To scan a host, simply run the following command:

```bash
python3 port_scanner.py -H <hostname> -p <port_range>
```

Example:

```bash
python3 port_scanner.py -H 192.168.1.1 -p 20-10000
```

Options:
- `-H`, `--host`: Target hostname or IP address.
- `-p`, `--ports`: Range of ports to scan (e.g., 20-1024).
- `-t`, `--timeout`: Optional. Timeout for the socket connection in seconds (default: 1).
- `-T`, `--tcp`: Optional. Scan using TCP (default behavior).
- `-U`, `--udp`: Optional. Scan using UDP.

### Example Output

```bash
Starting scan on host: 192.168.1.1
Scan completed in: 0:00:04.814766
Port 23 is open (Service: telnet)
Port 80 is open (Service: http)
Port 5080 is open (Service: Unknown service)
Port 5371 is open (Service: Unknown service)
Port 8080 is open (Service: http-alt)
```

### Contributing
Feel free to submit pull requests or report any issues! Contributions to improve this project are welcome.

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.