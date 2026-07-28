import subprocess


class ADB:
    def __init__(self, adb_path="adb"):
        self.adb = adb_path

    def run(self, *args):
        result = subprocess.run(
            [self.adb, *args],
            capture_output=True,
            text=True
        )
        return result.stdout.strip()

    # ------------------------
    # Device Information
    # ------------------------

    def devices(self):
        return self.run("devices")

    def serial(self):
        return self.run("get-serialno")

    def android_version(self):
        return self.run("shell", "getprop", "ro.build.version.release")

    def model(self):
        return self.run("shell", "getprop", "ro.product.model")

    def manufacturer(self):
        return self.run("shell", "getprop", "ro.product.manufacturer")

    def battery(self):
        return self.run("shell", "dumpsys", "battery")

    def ip_address(self):
        return self.run("shell", "ip", "addr")

    # ------------------------
    # Power
    # ------------------------

    def reboot(self):
        return self.run("reboot")

    def reboot_bootloader(self):
        return self.run("reboot", "bootloader")

    def reboot_recovery(self):
        return self.run("reboot", "recovery")

    # ------------------------
    # Screen
    # ------------------------

    def screenshot(self, filename="screen.png"):
        self.run("shell", "screencap", "-p", "/sdcard/temp.png")
        self.run("pull", "/sdcard/temp.png", filename)

    def screen_record(self, seconds=30):
        self.run(
            "shell",
            "screenrecord",
            "--time-limit",
            str(seconds),
            "/sdcard/video.mp4",
        )
        self.run("pull", "/sdcard/video.mp4")

    # ------------------------
    # Touch Controls
    # ------------------------

    def tap(self, x, y):
        self.run("shell", "input", "tap", str(x), str(y))

    def swipe(self, x1, y1, x2, y2, duration=300):
        self.run(
            "shell",
            "input",
            "swipe",
            str(x1),
            str(y1),
            str(x2),
            str(y2),
            str(duration),
        )

    def text(self, message):
        self.run("shell", "input", "text", message)

    def keyevent(self, key):
        self.run("shell", "input", "keyevent", str(key))

    # ------------------------
    # Buttons
    # ------------------------

    def home(self):
        self.keyevent(3)

    def back(self):
        self.keyevent(4)

    def recent(self):
        self.keyevent(187)

    def power(self):
        self.keyevent(26)

    def volume_up(self):
        self.keyevent(24)

    def volume_down(self):
        self.keyevent(25)

    # ------------------------
    # Apps
    # ------------------------

    def install(self, apk):
        return self.run("install", apk)

    def uninstall(self, package):
        return self.run("uninstall", package)

    def launch(self, package):
        return self.run(
            "shell",
            "monkey",
            "-p",
            package,
            "-c",
            "android.intent.category.LAUNCHER",
            "1",
        )

    def stop(self, package):
        return self.run("shell", "am", "force-stop", package)

    def packages(self):
        return self.run("shell", "pm", "list", "packages")

    # ------------------------
    # Files
    # ------------------------

    def push(self, local, remote):
        return self.run("push", local, remote)

    def pull(self, remote, local="."):
        return self.run("pull", remote, local)

    def delete(self, remote):
        return self.run("shell", "rm", remote)

    # ------------------------
    # Shell
    # ------------------------

    def shell(self, command):
        return self.run("shell", command)

    # ------------------------
    # Logs
    # ------------------------

    def logcat(self):
        return self.run("logcat", "-d")

    # ------------------------
    # WiFi ADB
    # ------------------------

    def tcpip(self, port=5555):
        return self.run("tcpip", str(port))

    def connect(self, ip, port=5555):
        return self.run("connect", f"{ip}:{port}")

    def disconnect(self):
        return self.run("disconnect")