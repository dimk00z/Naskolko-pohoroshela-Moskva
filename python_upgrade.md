# Обновление Python 3.7 to 3.8

## Ubuntu
В консоли следует выполнить ниже указанные команды:
```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.8
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 2
sudo update-alternatives --config python3
<!-- Выберите приоритет 1 для python3.8  -->
python3 -V
```
## MacOS

К сожалению на маке никогда не работал, но гугл выдает следующие инструкции: [вариант 1](https://jun711.github.io/devop/how-to-update-python3.6-to-python3.7-on-mac-os/)
и [вариант 2](https://installvirtual.com/install-python-3-8-on-mac/).

Проверить не могу, но выглядит просто.