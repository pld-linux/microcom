Summary:	minicom-like serial terminal emulator
Name:		microcom
Version:	1.02
Release:	1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://microcom.port5.com/m102.tar.gz
# Source0-md5:	c7817035dc41cb02e7cfb565cf9b7401
URL:		http://microcom.port5.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
microcom is a minicom-like serial terminal emulator with scripting
support. The requirement for this program was to be small enough
to fit on a floppy-based Linux distribution - such as the one
from Linux Router Project.

%prep
%setup -q -c

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.html
%attr(755,root,root) %{_bindir}/*
