def presentation():
    print("================================")
    print("    SOC Monitoring Tool")
    print("================================")

def premier_menu():
    print("1. Login")
    print("2. Quitter")

def correspond_premier_menu():
    while True:
        choix = input("Choisissez une option (1-2): ")
        match choix:
            case "1":
                login()
                return
            case "2":
                print("Au revoir!")
                raise SystemExit()
            case _:
                print("Choix invalide. Veuillez réessayer.")

def login():
    username = input("username: ")
    password = input("password: ")
    idx = 0
    while idx < 3:
        if username == "admin" and password == "admin123":
            return
        else:
            print("Nom d'utilisateur ou mot de passe incorrect.")
            idx += 1
            username = input("username: ")
            password = input("password: ")
    print("Trop de tentatives infructueuses. Veuillez réessayer plus tard.")
    raise SystemExit()
    
def menu_principal():
    print("=========== Menu Principal ===========")
    print("1. Scan réseau")
    print("2. Scan ports")
    print("3. Lecture des logs")
    print("4. Statistiques")
    print("5. Alertes")
    print("6. Logout")

def scan_reseau():
    print("Scan réseau en cours...")
    for i in range(1, 6):
        print(f"Scan 192.168.1.{i}...")
        if i % 2 == 0:
            print(f"192.168.1.{i} est actif")
        else:
            print(f"192.168.1.{i} est inactif")
    
def scan_ports():
    adresse_ip = input("Entrez l'adresse IP à scanner: ")
    print(f"Scan des ports pour {adresse_ip} en cours...")
    for port in range(1, 1025):
        if port in [21, 22, 80, 443]:
            print(f"{port} ouvert")
        elif port in [445, 110, 143]:
            print(f"{port} filtré")
   
logs = [
        "INFO: Connexion réussie",
        "WARNING: Tentative de connexion échouée",
        "ERROR: Erreur de connexion",
        "INFO: Déconnexion réussie",
        "INFO: Backup completed",
        "ERROR: Malware detected",
        "INFO: SSH connection opened",
        "WARNING: Multiple failed logins"
    ]

def lecture_logs(logs):
    print("Lecture des logs en cours...")
    for log in logs:
        print(log)

def statistiques(logs):
    print("Statistiques en cours...")
    info = 0
    warning = 0
    error = 0 
    for log in logs:
        if "INFO" in log:
            info += 1
        elif "WARNING" in log:
            warning += 1
        elif "ERROR" in log:
            error += 1
    print(f"logs: {len(logs)}")
    print(f"INFO: {info}")
    print(f"WARNING: {warning}")
    print(f"ERROR: {error}")

def alertes(logs):
    for log in logs:
        if "Malware" in log:
            print("HIGH ALERT: Malware detected")
        elif "failed logins" in log:
            print("MEDIUM ALERT: Brute force possible")

def correspond_menu_principal():
    choix = input("Choisissez une option (1-6): ")
    match choix:
        case "1":
            scan_reseau()
        case "2":
            scan_ports()
        case "3":
            lecture_logs(logs)
        case "4":
            statistiques(logs)
        case "5":
            alertes(logs)
        case "6":
            return "Déconnexion..."
        case _:
            print("Choix invalide. Veuillez réessayer.")


while True:    
    presentation()
    premier_menu()
    correspond_premier_menu()
    while True:
        menu_principal()
        resultat = correspond_menu_principal()
        if resultat == "Déconnexion...":
            break