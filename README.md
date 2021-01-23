# [Colorful Image Colorization](https://richzhang.github.io/colorization/)

### Implementacja algorytmu z wykorzystaniem języka Python.

### Łukasz Wierzbicki, Politechnika Warszawska

# Minimalne wymagania systemowe do uruchomienia aplikacji:

- python 3.6
- pipenv

# Proces pobrania repozytorium

```
sudo apt install git-lfs
git lfs clone https://github.com/lwierzb1/mgr-colorful-image-colorization.git
```

# Proces uruchamiania aplikacji

```
python3 -m pipenv install
python3 -m pipenv shell
python3 main.py --input bw.bmp --mode image --store colored.bmp
```