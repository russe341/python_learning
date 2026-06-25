def scanner_machine(ip):
    print(f"Scan {ip}...")
    dernier = ip.split(".")[-1]
    ports = [21, 22, 80, 443, 3306, 25, 53, 198]

    
    if dernier in ["1", "3"]:
        print("Machine active")
        for port in ports:
            scanner_port(port)
    else:
        print("Machine inactive")

def scanner_port(port):
    print(f"Scan du port {port}...")
    if port in [22, 80, 443]:
        print("Port ouvert")
    else:
        print("Port fermé")



for ip in range(1, 10):
    scanner_machine(f"192.168.1.{ip}")
