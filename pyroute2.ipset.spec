#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyroute2.ipset
Version  : 0.6.5
Release  : 12
URL      : https://files.pythonhosted.org/packages/4e/29/4085ee8f1ee09023c18ccbee5473c45349b4fbe77eef551a5deee872de9b/pyroute2.ipset-0.6.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/4e/29/4085ee8f1ee09023c18ccbee5473c45349b4fbe77eef551a5deee872de9b/pyroute2.ipset-0.6.5.tar.gz
Summary  : Python Netlink library: ipset
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0 GPL-2.0+
Requires: pyroute2.ipset-license = %{version}-%{release}
Requires: pyroute2.ipset-python = %{version}-%{release}
Requires: pyroute2.ipset-python3 = %{version}-%{release}
Requires: pyroute2.core
BuildRequires : buildreq-distutils3
BuildRequires : pyroute2.core

%description
==============
        
        PyRoute2 is a pure Python **netlink** library.
        
        This module provides IPSet and WiSet classes.
        
        links
        =====

%package license
Summary: license components for the pyroute2.ipset package.
Group: Default

%description license
license components for the pyroute2.ipset package.


%package python
Summary: python components for the pyroute2.ipset package.
Group: Default
Requires: pyroute2.ipset-python3 = %{version}-%{release}

%description python
python components for the pyroute2.ipset package.


%package python3
Summary: python3 components for the pyroute2.ipset package.
Group: Default
Requires: python3-core
Provides: pypi(pyroute2.ipset)
Requires: pypi(pyroute2.core)

%description python3
python3 components for the pyroute2.ipset package.


%prep
%setup -q -n pyroute2.ipset-0.6.5
cd %{_builddir}/pyroute2.ipset-0.6.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1632182062
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyroute2.ipset
cp %{_builddir}/pyroute2.ipset-0.6.5/LICENSE.Apache.v2 %{buildroot}/usr/share/package-licenses/pyroute2.ipset/cd9bad64b174708395f795bb92f7b4be7d996e8f
cp %{_builddir}/pyroute2.ipset-0.6.5/LICENSE.GPL.v2 %{buildroot}/usr/share/package-licenses/pyroute2.ipset/4cc77b90af91e615a64ae04893fdffa7939db84c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyroute2.ipset/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/pyroute2.ipset/cd9bad64b174708395f795bb92f7b4be7d996e8f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
