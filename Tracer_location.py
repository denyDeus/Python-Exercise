import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import time, random

def start_phone_tracer(target):
    print(f"[+] phoneTracer v2.1 - OSINT")
    print(f"[*] Target: {target}")
    print(f"[*] Initiating trace...")
    time.sleep(random.randint(2, 4))
    carrier_name = carrier.name_for_number(phonenumbers.parse(target, None), "en")
    phonenumbers.is_valid_number(phonenumbers.parse(target, None))
    print(f"[+] Carrier: {carrier_name}")
    p = phonenumbers.parse(target, None)
    r = geocoder.description_for_number(p, "en")
    print(f"[+] Location: {r}")
    print(f"[+] Trace complete")
start_phone_tracer("+255-755-778-113")