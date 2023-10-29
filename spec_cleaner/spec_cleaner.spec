%{!?_version: %define _version 1.2.2 }
%global srcname spec_cleaner
Name:           python-%{srcname}
Version:        %{_version}
Release:        1%{?dist}
Summary:        RPM .spec files cleaner

License:        BSD License
URL:            https://pypi.org/project/%{srcname}
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

%description
spec-cleaner is a tool that cleans the given RPM spec file according to the style guide and returns the result.

%package -n     python3-%{srcname}
Summary:        %{summary}
%description -n python3-%{srcname}


%prep
%autosetup -n %{srcname}-%{_version}
rm -rf %{srcname}.egg-info


%build
%{__python3} setup.py build


%install
%{__python3} setup.py install --root=$RPM_BUILD_ROOT


%files -n python3-%{srcname}
%doc README.md README.md.in
%{_bindir}/spec-cleaner
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{_version}-py%{python3_version}.egg-info
%{_prefix}/lib/obs/service/*
%{_datadir}/spec-cleaner


%changelog
* Sun Oct 22 2023 root
- 
