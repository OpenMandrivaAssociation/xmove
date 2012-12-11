%define name	xmove
%define version	2.0
%define rel	4
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
BuildRequires:	libx11-devel imake
Patch0:		xmove-2.0-unix-domain.patch

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
	%make CXXOPTIONS="%optflags" EXTRA_LDOPTIONS="%ldflags"
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
%_bindir/xmove*
%{_mandir}/man1/xmove*



%changelog
* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 2.0-0.beta2.4mdv2011.0
+ Revision: 634908
- simplify BR

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 2.0-0.beta2.3mdv2010.0
+ Revision: 435250
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.0-0.beta2.2mdv2009.0
+ Revision: 136612
- restore BuildRoot

* Thu Dec 20 2007 Thierry Vignaud <tv@mandriva.org> 2.0-0.beta2.2mdv2008.1
+ Revision: 135615
- adatp to new xorg layout
- BR imake
- kill bogus BR
- kill re-definition of %%buildroot on Pixel's request
- import xmove


* Sat Sep 03 2005 Marcel Pol <mpol@mandriva.org> 2.0-0.beta2.2mdk
- buildrequires x11

* Thu Aug  4 2005 Olivier Blin <oblin@mandriva.com> 2.0-0.beta2.1mdk
- initial Mandriva release
- Patch0: Unix domain sockets support (from Debian)
