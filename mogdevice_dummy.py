# In mogdevice_dummy.py
class MOGDevice:
    def __init__(self, address):
        self.address = address
        print("Dummy device initialized at", address)

    def ask(self, command):
        print("Dummy ask called with:", command)
        return "Dummy response"

    def cmd(self, command):
        print("Dummy cmd called with:", command)
        return "OK"

    def ask_dict(self, command):
        print("Dummy ask_dict called with:", command)
        return {"dummy_key": "dummy_value"}

    def ask_bin(self, command):
        print("Dummy ask_bin called with:", command)
        return b"Dummy binary data"

    def close(self):
        print("Dummy device closed")
