import urllib.request


def get_myip():

    external_ip = urllib.request.urlopen("https://ipv4.ident.me").read().decode()

    return external_ip


# get_ip = get_myip()
# print(get_ip)