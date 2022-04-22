pip3 install -U pyvisa          #Libreria que permite comunicar la fuente con Raspberry. 
pip3 install -U pyusb           #Libreria habilita comunicación usb
pip3 install -U pyvisa-py       #Drivers para Visa
pip3 install -U pandas          #Escribe archivos csv
pip3 install -U numpy           #Usado por pandas
sudo apt-get install libatlas-base-dev -y  #Soluciona posible bug de NumPy
# Cambia los permisos de Linux para lectura de dispositivos USB:
wget https://techoverflow.net/scripts/udev-install-usbusers.sh
sudo bash udev-install-usbusers.sh
rm udev-install-usbusers.sh