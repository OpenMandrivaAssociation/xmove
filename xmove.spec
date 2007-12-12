%define name	xmove
%define version	2.0
%define rel	2
%define beta	2
%if %{beta}
%define release %mkrel 0.beta%{beta}.%{rel}
%else
%define release	%mkrel %{rel}
%endif

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	X11 pseudoserver to dynamically move X11 applications
%if %{beta}
Source0:	ftp://ftp.cs.columbia.edu/pub/xmove/%{name}.%{version}beta%{beta}.tar.bz2
%else
Source0:	ftp://ftp.cs.columbia.edu/pub/xmove/%{name}.%{version}.tar.bz2
%endif
License:	MIT
Group:		System/X11
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		ftp://ftp.cs.columbia.edu/pub/xmove/
BuildRequires:	X11-devel
BuildRequires:	X11
Patch0:		xmove-2.0-unix-domain.patch.bz2

%description
xmove is a pseudoserver (aka proxy server) which allows you
to dynamically move an X application between servers, and screens
within a server.

%prep
%setup -q -n %{name}
%patch0 -p1 -b .unix-domain
chmod 644 doc/*

%build
for i in xmove xmovectrl; do
	cd $i
	ln -sf ../man/man1/$i.1 $i.man
	xmkmf
	%make
	cd $OLDPWD
done

%install
rm -rf $RPM_BUILD_ROOT
install -d -m755 $RPM_BUILD_ROOT%{_mandir}/man1/
for i in xmove xmovectrl; do
	cd $i
	%{makeinstall_std}
	cd $OLDPWD
	install -m 644 man/man1/$i.1 $RPM_BUILD_ROOT%{_mandir}/man1/
done

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc README doc/*
/usr/X11R6/bin/xmove*
%{_mandir}/man1/xmove*

