Name:           qconf
Version:        1.4
Release:        7
Epoch:          0
Summary:        Allows you to have a nice configure script for your qmake-based project
Group:          Development/KDE and Qt
License:        GPL
URL:            http://delta.affinix.com/qconf/
Source0:        http://delta.affinix.com/download/qconf-%{version}.tar.bz2
Buildrequires:  qt4-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
QConf allows you to have a nice configure script for your
qmake-based project. It is intended for developers who don't need
(or want) to use the more complex GNU autotools. With qconf/qmake,
it is easy to maintain a cross-platform project that uses a
familiar configuration interface on unix.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} \
            --bindir=%{_bindir} \
            --datadir=%{_datadir} \
            --qtdir=%{qt4dir}
%{make}

%install
%{__rm} -rf %{buildroot}
%{make} INSTALL_ROOT=%{buildroot} install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}




%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0:1.4-6mdv2010.0
+ Revision: 433753
- rebuild

* Mon Sep 07 2009 Thierry Vignaud <tvignaud@mandriva.com> 0:1.4-5mdv2010.0
+ Revision: 432723
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 0:1.4-4mdv2009.0
+ Revision: 259908
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tvignaud@mandriva.com> 0:1.4-3mdv2009.0
+ Revision: 247757
- rebuild

* Thu Jan 31 2008 David Walluck <walluck@mandriva.org> 0:1.4-1mdv2008.1
+ Revision: 160614
- 1.4

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Jan 29 2007 David Walluck <walluck@mandriva.org> 1.3-1mdv2007.0
+ Revision: 115188
- 1.3
- Import qconf

* Tue Sep 05 2006 David Walluck <walluck@mandriva.org> 0:1.2-2mdv2007.0
- rebuild to fix release

* Mon May 08 2006 David Walluck <walluck@mandriva.org> 0:1.2-1mdk
- release

