Name:		python-notofonttools
Version:	0.2.19
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/n/notofonttools/notofonttools-%{version}.tar.gz
Summary:	Noto font tools
URL:		https://pypi.org/project/notofonttools/
License:	Apache
Group:		Development/Python
BuildRequires:	python-setuptools
BuildRequires:	python%{py_ver}dist(pip)
BuildRequires:	python%{py_ver}dist(wheel)
BuildRequires:	python%{py_ver}dist(tomli)
BuildRequires:	python%{py_ver}dist(setuptools-scm)
BuildArch:	noarch

%description
Noto font tools

%prep
%autosetup -p1 -n notofonttools-%{version}

%build
python setup.py build

%install
python setup.py install --skip-build --root=%{buildroot}

%files
%{_bindir}/*
%{python_sitelib}/nototools
%{python_sitelib}/third_party
%{python_sitelib}/notofonttools*.egg-info
