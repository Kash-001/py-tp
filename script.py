def produce_default_dict():
    return {'root':'password'}

def salutation(nom: str, age: int):
    return f"Bonjour {nom}, vous avez actuellement {str(age)} ans."

## display chosen amount of power of 2 
def power_2(limit):
    power = 2
    for _ in range(0,limit):
        print(power)
        power = power*2

## check if string is ipv4
def check_ipv4(chain:str):
    if len(chain) > 15:
        return False
    elif "." not in chain:
        return False
    ipv4_octets = chain.split(".")
    if len(ipv4_octets) > 4 or len(ipv4_octets) < 4:
        return False
    for octet in ipv4_octets:
        try:
            if int(octet) > 255 or int(octet) < 0:
                return False
        except ValueError:
            return False
    return True
