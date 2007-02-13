Summary:	Python interface for libshout 2 library
Summary(pl.UTF-8):	Interfejs Pythona do biblioteki libshout 2
Name:		python-shout
Version:	0.2
Release:	1
License:	LGPL v2+
Group:		Libraries/Python
Source0:	http://downloads.xiph.org/releases/libshout/shout-python-%{version}.tar.gz
# Source0-md5:	80bec97a1462c2d2a9282ba8a7c18336
URL:		http://icecast.org/
BuildRequires:	libshout-devel >= 2.1
BuildRequires:	pkgconfig
BuildRequires:	python-devel
Requires:	libshout >= 2.1
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a Python binding for libshout 2 library. It allows you
to act as a source for icecast 1 and 2, and shoutcast.

%description -l pl.UTF-8
Ten moduł jest interfejsem Pythona do biblioteki libshout 2. Pozwala
na działanie jako źródło dla icecasta 1 i 2 oraz shoutcasta.

%prep
%setup -q -n shout-python-%{version}

%build
export CFLAGS="%{rpmcflags}"
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install example.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{py_sitedir}/*.so
%{_examplesdir}/%{name}-%{version}
