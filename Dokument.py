import numpy as np

class Dokument:
    def __init__(self, subor):
        self.subor = subor

    def naSlova(self):
        subor = open("dataset/" + self.subor, encoding="cp1250")
        slova = list()
        for line in subor:
            array_line = np.asarray(line.split())
            i = 0
            for x in array_line:
                if len(x.strip()) != 0:
                    slova.append(x.strip())
                i = i + 1

        array = np.asarray(slova)
        return array

    def hlavicka(self):
        subor = open("dataset/" + self.subor, encoding="cp1250")
        slova = list()
        for line in subor:
            array_line = np.asarray(line.split())
            i = 0
            for x in array_line:
                if len(x.strip()) != 0:
                    slova.append(x.strip())
                i = i + 1
            if "ECLI:" in line:
                break

        array = np.asarray(slova)
        return array

    def naVety(self):
        pass