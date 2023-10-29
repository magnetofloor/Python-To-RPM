# Переменные
PACKAGE_NAME = spec_cleaner
PACKAGE_VERSION = 1.2.2
PACKAGE_RELEASE = 1
OS_SUFFIX = el8

# Пути к исходным файлам
SOURCE_DIR = spec-cleaner
SPEC_FILE = $(PACKAGE_NAME).spec

# Цель по умолчанию
all: build

# Скачивание исходных файлов
download:
	[ -d ~/rpmbuild/SOURCES ] || mkdir -p ~/rpmbuild/SOURCES
	python3 -m pip download $(PACKAGE_NAME)==$(PACKAGE_VERSION) --dest ~/rpmbuild/SOURCES
#	tar xzf $(PACKAGE_NAME)-$(PACKAGE_VERSION).tar.gz -C ~/rpmbuild/SOURCES

# Сборка пакета
build: download
	rpmbuild -ba $(SPEC_FILE)

# Установка пакета
install:
	rpm -Uvh ~/rpmbuild/RPMS/noarch/python3-$(PACKAGE_NAME)-$(PACKAGE_VERSION)-$(PACKAGE_RELEASE).$(OS_SUFFIX).noarch.rpm

# Чистка
clean:
	rm -rf ~/rpmbuild
	rm -f $(PACKAGE_NAME)-$(PACKAGE_VERSION).tar.gz
	rm -rf $(SOURCE_DIR)

.PHONY: all download build install clean
