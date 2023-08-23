%define		snap	20230723
%define		gitref	feae9fda26ea9de98da9cd6733980a203115537e
%define		rel	1

Summary:	Weechat Matrix protocol script written in python
Name:		weechat-plugin-matrix
Version:	0.3.0
Release:	0.%{snap}.%{rel}
License:	ISC
Group:		Applications/Communications
Source0:	https://github.com/poljar/weechat-matrix/archive/%{gitref}/%{name}-%{snap}.tar.gz
# Source0-md5:	9e59262c045f49eedc73401f2dfd269e
URL:		https://github.com/poljar/weechat-matrix
Requires:	python3 >= 1:3.6
Requires:	python3-aiohttp
Requires:	python3-atomicwrites
Requires:	python3-attrs
Requires:	python3-future
Requires:	python3-logbook
Requires:	python3-magic
Requires:	python3-matrix-nio
Requires:	python3-modules >= 1:3.6
Requires:	python3-pyOpenSSL
Requires:	python3-pygments
Requires:	python3-requests
Requires:	python3-webcolors
Requires:	weechat-plugin-python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Weechat Matrix protocol script written in python.

%prep
%setup -q -n weechat-matrix-%{gitref}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/weechat/python/matrix

cp -p main.py $RPM_BUILD_ROOT%{_datadir}/weechat/python/matrix.py
cp -p matrix/*.py $RPM_BUILD_ROOT%{_datadir}/weechat/python/matrix

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{_datadir}/weechat/python/matrix.py
%{_datadir}/weechat/python/matrix
