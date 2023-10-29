# Python-To-RPM
Выбранный пакет - **spec_cleaner**
github: https://github.com/rpm-software-management/spec-cleaner
## Запуск

Либо собрать докер-образ с установленным rpm-пакетом
```
docker build -t oraclelinux:8-upgrade .
```
Либо собрать явно rpm-пакет
```
cd spec_cleaner
make
make install
```