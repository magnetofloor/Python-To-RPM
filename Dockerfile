FROM oraclelinux:8

COPY spec_cleaner /spec_cleaner_build
WORKDIR /spec_cleaner_build

RUN dnf install -y make python3 \
    python3-setuptools.noarch python3-devel python3-pytest.noarch \
    rpmdevtools rpm-build

RUN make 
RUN make install

CMD ["bash"]