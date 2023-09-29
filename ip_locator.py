from os import system
try:
    import ipapi
except ModuleNotFoundError:
    system('pip install ipapi')


def iplocate(ip_address: str):
    location = ipapi.location(ip_address)
    return location


if __name__ == "__main__":
    ip = input("Input your IP address here >> ")
    print(iplocate(ip))
