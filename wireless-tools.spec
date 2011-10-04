#specfile originally created for Fedora, modified for Moblin Linux

Summary: Wireless ethernet configuration tools
Group: System/Base
License: GPL+
Name: wireless-tools
Version: 29
Release: 2
URL: http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/Tools.html
Source: http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/wireless_tools.%{version}.tar.gz
Patch1: wireless-tools-29-makefile.patch
Patch2: buildfix.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This package contain the Wireless tools, used to manipulate
the Wireless Extensions. The Wireless Extension is an interface
allowing you to set Wireless LAN specific parameters and get the
specific stats for wireless networking equipment.

%package devel
Summary: Development headers for the wireless-tools package
Group: Development/Libraries
Requires: wireless-tools = %{version}-%{release}

%description devel
Development headers for the wireless-tools package.

%prep

%setup -q -n wireless_tools.%{version}
%patch1 -p1 -b .makefile
%patch2 -p1 -b .buildfix

%build
make clean
make OPT_FLAGS="$RPM_OPT_FLAGS" BUILD_SHARED=1 FORCE_WEXT_VERSION=16

%install
%{__mkdir_p} $RPM_BUILD_ROOT{/sbin,/%{_lib},%{_mandir}/man8,%{_includedir},%{_libdir}}

make install INSTALL_DIR=$RPM_BUILD_ROOT/sbin \
	INSTALL_LIB=$RPM_BUILD_ROOT/%{_lib} \
	INSTALL_INC=$RPM_BUILD_ROOT%{_includedir} \
	INSTALL_MAN=$RPM_BUILD_ROOT%{_mandir} \
	%{?_smp_mflags}
%{__rm} -f $RPM_BUILD_ROOT/%{_lib}/libiw.{a,so}
ln -sf ../../%{_lib}/libiw.so.%{version} \
       $RPM_BUILD_ROOT%{_libdir}/libiw.so

%clean

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
/sbin/*
/%{_lib}/*.so.*
%doc INSTALL README DISTRIBUTIONS.txt
%doc %{_mandir}/man*/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so

