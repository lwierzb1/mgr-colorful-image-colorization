# [Colorful Image Colorization](https://richzhang.github.io/colorization/)

### Implementacja algorytmu z wykorzystaniem języka Python.

### Łukasz Wierzbicki, Politechnika Warszawska

# Minimalne wymagania systemowe do uruchomienia aplikacji:

- pipenv

# Proces pobrania repozytorium

```
sudo apt install git-lfs
git lfs clone https://github.com/lwierzb1/mgr-colorful-image-colorization.git
```

# Proces uruchamiania aplikacji

Ważnym punktem poprawnego uruchomienia aplikacji jest ewentualna korekta ustawień sieci neuronowej umieszonej w
pliku `cnn_config.ini`

```
python3 -m pipenv install
python3 -m pipenv shell

python3 main.py --input bw.bmp --mode image --store colored.bmp
python3 main.py --mode camera
python3 main.py --input 1.avi --mode video --store result_1.avi
```