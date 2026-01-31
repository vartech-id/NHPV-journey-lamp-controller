# pc_api/esp_client.py
# Python biasa (jalan di PC), untuk kirim command ke ESP32 via USB Serial

import time
import serial


class ESP32SerialClient:
    def __init__(self, port: str, baudrate: int = 115200, timeout: float = 1.5):
        """
        port: contoh "COM7"
        baudrate: biasanya 115200
        timeout: waktu tunggu baca balasan
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.ser = None

    def open(self):
        if self.ser and self.ser.is_open:
            return

        self.ser = serial.Serial(self.port, baudrate=self.baudrate, timeout=self.timeout)

        # cegah auto-reset berulang (banyak board reset saat DTR/RTS high)
        self.ser.dtr = False
        self.ser.rts = False

        # tunggu board selesai boot kalau sempat reset
        time.sleep(2.0)

        # buang output boot/print awal
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()

    def close(self):
        """Tutup koneksi serial."""
        if self.ser and self.ser.is_open:
            self.ser.close()

    def send_command(self, cmd: str) -> str:
        """
        Kirim 1 command dan baca 1 baris balasan.
        Return: string balasan (misal 'OK K1_ON' / 'PONG' / dst)
        """
        if not self.ser or not self.ser.is_open:
            self.open()

        msg = (cmd.strip() + "\n").encode("utf-8")
        self.ser.write(msg)
        self.ser.flush()

        # Baca balasan satu baris
        resp = self.ser.readline().decode("utf-8", errors="ignore").strip()
        if not resp:
            # retry sekali
            time.sleep(0.1)
            self.ser.write(msg)
            self.ser.flush()
            resp = self.ser.readline().decode("utf-8", errors="ignore").strip()
        return resp
