# pc_api/esp_client.py
# Python biasa (jalan di PC), untuk kirim command ke ESP32 via USB Serial

import time
import serial
from serial import SerialException


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

        self.ser = serial.Serial(
            self.port,
            baudrate=self.baudrate,
            timeout=self.timeout,
            write_timeout=self.timeout,
        )

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
        self.ser = None

    def _reopen(self):
        self.close()
        time.sleep(0.2)
        self.open()

    def send_command(self, cmd: str) -> str:
        """
        Kirim 1 command dan baca 1 baris balasan.
        Return: string balasan (misal 'OK K1_ON' / 'PONG' / dst)
        """
        msg = (cmd.strip() + "\n").encode("utf-8")
        last_error = None

        # 1x attempt normal + 1x attempt setelah reconnect.
        for attempt in range(2):
            try:
                if not self.ser or not self.ser.is_open:
                    self.open()

                self.ser.write(msg)
                self.ser.flush()

                # Baca balasan satu baris
                resp = self.ser.readline().decode("utf-8", errors="ignore").strip()
                if not resp:
                    # retry sekali pada koneksi yang sama
                    time.sleep(0.1)
                    self.ser.write(msg)
                    self.ser.flush()
                    resp = self.ser.readline().decode("utf-8", errors="ignore").strip()

                if resp:
                    return resp

                last_error = TimeoutError("ESP32 did not return response")
            except (SerialException, OSError, TimeoutError) as exc:
                last_error = exc

            if attempt == 0:
                self._reopen()

        raise RuntimeError(f"Failed to send command '{cmd}' to ESP32: {last_error}")
