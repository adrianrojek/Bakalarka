#!/usr/local/bin/python
# coding: windows-1250
from Extrakcia import Extrakcia,extraction_success,subory_json,perf_measure,UspesnostAtributov


def main():
    for x in subory_json:
        Extrakcia(x)
    UspesnostAtributov()
    print(perf_measure)

main()

