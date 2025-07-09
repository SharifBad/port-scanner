import socket      # Used to create network connections
import threading   # Used to run multiple scans at the same time (in parallel)

# This function scans a single port on a target IP
def scan_port(ip, port):
    try:
        # Create a socket object (like a virtual phone line)
        s = socket.socket()
        s.settimeout(1)  # Wait 1 second max for a connection
        s.connect((ip, port))  # Try to connect to the target IP and port

        # Try to receive a banner (welcome message)
        try:
            banner = s.recv(1024).decode().strip()
            print(f"[+] Port {port} is OPEN — Service: {banner}")
        except:
            # If no banner is sent, just say it's open
            print(f"[+] Port {port} is OPEN — No banner received")

        s.close()  # Close the connection
    except:
        pass  # If connection fails, just skip (port is closed or filtered)

# This is the main function that runs the scan
def main():
    # Ask the user for target IP and port range
    target = input("Enter target IP address: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    print(f"\n[~] Scanning {target} from port {start_port} to {end_port}...\n")

    threads = []  # This list will store all thread objects

    # Loop through the range of ports
    for port in range(start_port, end_port + 1):
        # For each port, create a thread to scan it in parallel
        thread = threading.Thread(target=scan_port, args=(target, port))
        thread.start()  # Start the thread (begin scanning)
        threads.append(thread)  # Save the thread so we can wait for it later

    # Wait for all threads to finish before ending the program
    for thread in threads:
        thread.join()

    print("\n[+] Scan complete.")

# Python runs this part first
if __name__ == "__main__":
    main()