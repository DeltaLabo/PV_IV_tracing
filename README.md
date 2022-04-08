# PV_IV_tracing

## Instalación de dependencias 
Instalar [PyVisa](https://pyvisa.readthedocs.io/projects/pyvisa-py/en/latest/installation.html)
`pip3 install -U pyvisa`

PyVisa requiere de [PyUSB](https://github.com/pyusb/pyusb)
`pip3 install -U pyusb`

PyVisa requiere PyVisa-Py
`pip3 install -U pyvisa-py`

Instalar libreria pandas
`pip3 install -U pandas`

Pandas requiere de NumPy
`pip3 install -U numpy`

Hay un posible bug al instalar NumPy, este se puede solucionar con
`sudo apt-get install libatlas-base-dev`

Se deben cambiar los permisos de Linux para lectura de dispositivos USB, puede usarse 
el siguiente [script](https://techoverflow.net/2019/08/09/how-to-fix-pyvisa-found-a-device-whose-serial-number-cannot-be-read-the-partial-visa-resource-name-is-usb0-0instr/)
```bash
wget https://techoverflow.net/scripts/udev-install-usbusers.sh
chmod +x udev-install-usbusers.sh
sudo ./udev-install-usbusers.sh
```

