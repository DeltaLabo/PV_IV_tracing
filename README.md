# PV_IV_tracing

## Instalación de dependencias 

Se dispone de dos opciones para instalar dependencias desde la terminal:

1. Instalarlo automáticamente usando el [script](https://github.com/DeltaLabo/PV_IV_tracing/blob/master/descargar_dependencias.sh)

2. Ejecutar los siguientes comandos manualmente:

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
sudo bash udev-install-usbusers.sh
```

## Actualizar controller
Este proceso es necesario, para llamar un archivo más reciente desde otro repositorio el cual es privado. **Se requiere tener los permisos configurados en la terminal.**

Se realiza ejecutando en terminal

`bash actualizar_controller.sh`

## Contactos
Colaboradores activos en el proyecto:
- Luis Ross Lépiz ([lross2k](https://github.com/lross2k)) luisross87@estudiantec.cr
- Byron Bolaños Zamora ([Byron-Bolanos](https://github.com/Byron-Bolanos)) bbolanos@estudiantec.cr
