# esp32_fw/main.py
# MicroPython code (jalan di ESP32)
from machine import Pin
import time
import sys

# =========================
# KONFIGURASI PIN RELAY (8 CHANNEL)
# =========================
RELAY1_GPIO = 13
RELAY2_GPIO = 14
RELAY3_GPIO = 27
RELAY4_GPIO = 26
RELAY5_GPIO = 25
RELAY6_GPIO = 33
RELAY7_GPIO = 32
RELAY8_GPIO = 16

# Banyak board relay itu "aktif LOW":
# - Kirim 0 -> relay ON
# - Kirim 1 -> relay OFF
ACTIVE_LOW = True


def write_relay(pin: Pin, on: bool):
    """Hidup/matikan relay dengan mempertimbangkan ACTIVE_LOW."""
    if ACTIVE_LOW:
        pin.value(0 if on else 1)
    else:
        pin.value(1 if on else 0)


# Setup pin
relay1 = Pin(RELAY1_GPIO, Pin.OUT)
relay2 = Pin(RELAY2_GPIO, Pin.OUT)
relay3 = Pin(RELAY3_GPIO, Pin.OUT)
relay4 = Pin(RELAY4_GPIO, Pin.OUT)
relay5 = Pin(RELAY5_GPIO, Pin.OUT)
relay6 = Pin(RELAY6_GPIO, Pin.OUT)
relay7 = Pin(RELAY7_GPIO, Pin.OUT)
relay8 = Pin(RELAY8_GPIO, Pin.OUT)

# Biar gampang ON/OFF semua
relays = [relay1, relay2, relay3, relay4, relay5, relay6, relay7, relay8]

# Default: semua OFF (aman)
for r in relays:
    write_relay(r, False)

print("ESP32 READY")
print("Commands: "
      "K1_ON, K1_OFF, K2_ON, K2_OFF, K3_ON, K3_OFF, K4_ON, K4_OFF, "
      "K5_ON, K5_OFF, K6_ON, K6_OFF, K7_ON, K7_OFF, K8_ON, K8_OFF, "
      "K_ON_ALL, K_OFF_ALL, PING")


def clean_cmd(s: str) -> str:
    # Buang karakter aneh/escape: hanya izinkan A-Z, 0-9, dan _
    s = s.upper()
    allowed = []
    for ch in s:
        if ("A" <= ch <= "Z") or ("0" <= ch <= "9") or ch == "_":
            allowed.append(ch)
    return "".join(allowed)


def handle_command(cmd: str):
    cmd = clean_cmd(cmd)

    if cmd == "K1_ON":
        write_relay(relay1, True);  print("OK from relay = K1_ON")
    elif cmd == "K1_OFF":
        write_relay(relay1, False); print("OK from relay = K1_OFF")

    elif cmd == "K2_ON":
        write_relay(relay2, True);  print("OK from relay = K2_ON")
    elif cmd == "K2_OFF":
        write_relay(relay2, False); print("OK from relay = K2_OFF")

    elif cmd == "K3_ON":
        write_relay(relay3, True);  print("OK from relay = K3_ON")
    elif cmd == "K3_OFF":
        write_relay(relay3, False); print("OK from relay = K3_OFF")

    elif cmd == "K4_ON":
        write_relay(relay4, True);  print("OK from relay = K4_ON")
    elif cmd == "K4_OFF":
        write_relay(relay4, False); print("OK from relay = K4_OFF")

    elif cmd == "K5_ON":
        write_relay(relay5, True);  print("OK from relay = K5_ON")
    elif cmd == "K5_OFF":
        write_relay(relay5, False); print("OK from relay = K5_OFF")

    elif cmd == "K6_ON":
        write_relay(relay6, True);  print("OK from relay = K6_ON")
    elif cmd == "K6_OFF":
        write_relay(relay6, False); print("OK from relay = K6_OFF")

    elif cmd == "K7_ON":
        write_relay(relay7, True);  print("OK from relay = K7_ON")
    elif cmd == "K7_OFF":
        write_relay(relay7, False); print("OK from relay = K7_OFF")

    elif cmd == "K8_ON":
        write_relay(relay8, True);  print("OK from relay = K8_ON")
    elif cmd == "K8_OFF":
        write_relay(relay8, False); print("OK from relay = K8_OFF")

    elif cmd == "K_ON_ALL":
        for r in relays:
            write_relay(r, True)
        print("OK from relay = K_ON_ALL")

    elif cmd == "K_OFF_ALL":
        for r in relays:
            write_relay(r, False)
        print("OK from relay = K_OFF_ALL")

    elif cmd == "PING":
        print("PONG")
    elif cmd == "":
        pass
    else:
        print("ERR UNKNOWN:", cmd)


# Loop utama: baca baris dari Serial (USB)
# readline() bersifat blocking (menunggu input), ini justru stabil untuk receiver.
while True:
    try:
        line = sys.stdin.readline()
        if line == "":
            time.sleep_ms(50)   # cegah busy loop saat serial putus
            continue
        handle_command(line)
    except Exception as e:
        print("ERR:", repr(e))
        time.sleep(0.2)
