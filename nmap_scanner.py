import nmap

def run_nmap(hosts, ports, arguments, sudo=False):

    nm = nmap.PortScanner()


    command = 'nmap'
    if sudo:
        command = 'sudo ' + command
    command += f' -p {ports} {arguments} {hosts}'

    try:
        output = nm.scan(hosts=hosts, ports=ports, arguments=arguments)
        print(output)
    except Exception as e:
        print("Error:", e)

def main():
    print('*********** NMAP SCANNER **********\n')
    print('**Este scanner depende de tener todas las entradas solicitadas para su funcionamiento**\n')
    print('**Los comandos -sn y -p son redundantes, EVITAR su uso**\n')
    hosts = input("Ingrese los hosts (puede ser una dirección IP o un rango en formato CIDR: 192.168.6.0/24): ")
    ports = input("Ingrese los puertos (puede ser un solo puerto, un rango o una lista separada por comas: 80, 36,...): ")
    arguments = input("Ingrese los argumentos de nmap(-oN, -sS, -sV, etc): ")
    sudo = input("¿Desea ejecutar el comando como super usuario? (S/n): ").lower() == 's'

    # Ejecutar nmap
    run_nmap(hosts, ports, arguments, sudo)

if __name__ == "__main__":
    main()
