Summary:	Tool to interact with EWMH/NetWM compatible X Window managers
Name:		wmctrl
Version:	1.07
Release:	1
License:	GPL
Group:		X11/Applications
Vendor:		Tomas Styblo <tripie@cpan.org>
Source0:	http://sweb.cz/tripie/utils/wmctrl/dist/%{name}-%{version}.tar.gz
# Source0-md5:	1fe3c7a2caa6071e071ba34f587e1555
Patch0:		%{name}-64bit.patch
URL:		http://sweb.cz/tripie/utils/wmctrl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libXmu-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The tool provides command line access to almost all the features
defined in the EWMH specification. It can be used, for example, to get
information about the window manager, to get a detailed list of
desktops and managed windows, to switch and resize desktops, to make
windows full-screen, always-above or sticky, and to activate, close,
move, resize, maximize and minimize them.

%prep
%setup -q
%ifarch %{x8664}
%patch0 -p1
%endif

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/wmctrl
%{_mandir}/man1/wmctrl.1*

