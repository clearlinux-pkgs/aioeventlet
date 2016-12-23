#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : aioeventlet
Version  : 0.5.1
Release  : 20
URL      : https://pypi.python.org/packages/source/a/aioeventlet/aioeventlet-0.5.1.tar.gz
Source0  : https://pypi.python.org/packages/source/a/aioeventlet/aioeventlet-0.5.1.tar.gz
Summary  : asyncio event loop scheduling callbacks in eventlet.
Group    : Development/Tools
License  : Apache-2.0
Requires: aioeventlet-python
BuildRequires : eventlet
BuildRequires : funcsigs-python
BuildRequires : greenlet
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : trollius

%description
aioeventlet implements the asyncio API (PEP 3156) on top of eventlet. It makes
possible to write asyncio code in a project currently written for eventlet.

%package python
Summary: python components for the aioeventlet package.
Group: Default

%description python
python components for the aioeventlet package.


%prep
%setup -q -n aioeventlet-0.5.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python runtests.py --verbose || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
