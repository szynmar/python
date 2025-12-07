import time

class MojTimer:
    def __init__(self, etykieta):
        self.etykieta = etykieta
        self.strEtykieta = "dla '" + etykieta + "'" if "" != etykieta else ""

    def __enter__(self):
        print(f"--- start {self.strEtykieta}")
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        diff = self.end - self.start
        print(f"--- koniec {self.strEtykieta} (sekund: {diff})")

# Kod testowy tylko jeśli uruchamiasz plik samodzielnie, a nie importujesz go
if __name__ == "__main__":
    with MojTimer("test") as moj:
        time.sleep(1)
