Name:           qconf
Version:        1.4
Release:        %mkrel 3
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


