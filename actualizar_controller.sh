#!/bin/bash

# Elimina el archivo viejo y descarga el nuevo desde el repositorio de instrument driver 
rm controller_IV_reads.py 
curl https://raw.githubusercontent.com/DeltaLabo/instrument_driver/main/controller.py?token=GHSAT0AAAAAABT2WINFLYLSQ77D2DJ5RR52YTC2QSA > controller_IV_reads.py

