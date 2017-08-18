#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : aioeventlet
Version  : 0.5.1
Release  : 25
URL      : http://pypi.debian.net/aioeventlet/aioeventlet-0.5.1.tar.gz
Source0  : http://pypi.debian.net/aioeventlet/aioeventlet-0.5.1.tar.gz
Summary  : asyncio event loop scheduling callbacks in eventlet.
Group    : Development/Tools
License  : Apache-2.0
Requires: aioeventlet-python
Requires: eventlet
Requires: trollius
BuildRequires : eventlet
BuildRequires : greenlet
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : trollius

%description
possible to write asyncio code in a project currently written for eventlet.
        
        aioeventlet allows to use greenthreads in asyncio coroutines, and to use

%package python
Summary: python components for the aioeventlet package.
Group: Default

%description python
python components for the aioeventlet package.


%prep
%setup -q -n aioeventlet-0.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1503070628
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python runtests.py --verbose || :
%install
export SOURCE_DATE_EPOCH=1503070628
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
