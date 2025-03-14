import socket


def find_local_subnet() -> str:
    """
    Retrieves the local subnet by removing the last octet from the local IP address
    and appending '.1/24' to form the subnet notation.

    :return: A string representing the local subnet in the format 'xxx.xxx.xxx.1/24'.
    :raises socket.gaierror: If the local IP address cannot be retrieved.
    :raises ValueError: If the retrieved IP address is in an invalid format.
    :raises Exception: For any other unexpected errors.
    """
    global short_ip
    try:
        local_ip = socket.gethostbyname(socket.gethostname())

        parts = local_ip.split('.')
        if len(parts) != 4 or not all(part.isdigit() and 0 <= int(part) <= 255 for part in parts):
            raise ValueError("Niepoprawny format adresu IP")

        short_ip = '.'.join(parts[:-1])

    except socket.gaierror:
        print("Error: Unable to retrieve local IP address.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return short_ip + '.1/24'


print('Local subnet: ' + find_local_subnet())