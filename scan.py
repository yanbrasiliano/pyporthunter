import socket
import argparse
from datetime import datetime


def scan_port(host, port, timeout=1, protocol='tcp'):
    """Scan a single port on a given host."""
    try:
        sock_type = socket.SOCK_STREAM if protocol == 'tcp' else socket.SOCK_DGRAM
        with socket.socket(socket.AF_INET, sock_type) as sock:
            sock.settimeout(timeout)
            return sock.connect_ex((host, port)) == 0
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
        return False


def get_service_name(port, protocol='tcp'):
    """Return the service name for a given port if it's known."""
    try:
        service = socket.getservbyport(port, protocol)
        return service
    except OSError:
        return "Unknown service"


def scan_ports(host, start_port, end_port, timeout=1, protocol='tcp'):
    """Scan a range of ports on a given host and identify the service."""
    print(f"Starting scan on host: {host}")
    open_ports = []
    start_time = datetime.now()

    try:
        for port in range(start_port, end_port + 1):
            if scan_port(host, port, timeout, protocol):
                service_name = get_service_name(port, protocol)
                open_ports.append((port, service_name))
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
    except socket.gaierror:
        print("\nHostname could not be resolved.")
    except socket.error:
        print("\nCouldn't connect to server.")
    finally:
        duration = datetime.now() - start_time
        print(f"Scan completed in: {duration}")
        if open_ports:
            for port, service in open_ports:
                print(f"Port {port} is open (Service: {service})")
        else:
            print("No open ports found.")


def main():
    parser = argparse.ArgumentParser(description="Simple Python port scanner.")
    parser.add_argument("-H", "--host", required=True,
                        help="Target hostname or IP address.")
    parser.add_argument("-p", "--ports", required=True,
                        help="Range of ports to scan (e.g., 20-80).")
    parser.add_argument("-t", "--timeout", type=int, default=1,
                        help="Timeout for each port scan in seconds.")
    parser.add_argument("-T", "--tcp", action="store_true",
                        help="Use TCP protocol (default).")
    parser.add_argument("-U", "--udp", action="store_true",
                        help="Use UDP protocol.")

    args = parser.parse_args()

    protocol = 'udp' if args.udp else 'tcp'
    start_port, end_port = map(int, args.ports.split("-"))

    scan_ports(args.host, start_port, end_port, args.timeout, protocol)


if __name__ == "__main__":
    main()
