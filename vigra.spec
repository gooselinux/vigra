Summary:        Generic Programming for Computer Vision
Name:           vigra
Version:        1.6.0
Release:        2.1%{?dist}
License:        MIT
Group:          Development/Libraries
Source:         http://kogs-www.informatik.uni-hamburg.de/~koethe/vigra/%{name}%{version}.tar.gz
URL:            http://kogs-www.informatik.uni-hamburg.de/~koethe/vigra/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  zlib-devel libjpeg-devel libpng-devel libtiff-devel
BuildRequires:  fftw3-devel

%description
VIGRA stands for "Vision with Generic Algorithms". It's a novel computer vision
library that puts its main emphasis on customizable algorithms and data
structures. By using template techniques similar to those in the C++ Standard
Template Library, you can easily adapt any VIGRA component to the needs of your
application without thereby giving up execution speed.

%package devel
Summary:        Development tools for programs which will use the vigra library
Group:          Development/Libraries
Requires:       vigra = %{version}-%{release}
Requires:       libjpeg-devel libtiff-devel libpng-devel zlib-devel
Requires:       fftw3-devel

%description devel
The vigra-devel package includes the header files necessary for developing
programs that use the vigra library.

%prep
%setup -q -n %{name}%{version}

%build
export CXXFLAGS="$RPM_OPT_FLAGS"
./configure \
    --prefix=/usr \
    --with-tiff \
    --with-jpeg \
    --with-png \
    --with-zlib \
    --with-fftw \
    --enable-shared \
    --disable-static \
    --libdir=%{_libdir}
make

%install
rm -rf %{buildroot}
%makeinstall
rm -f %{buildroot}/%{_libdir}/libvigraimpex.la
rm -rf %{buildroot}/usr/doc

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root,-)
%doc LICENSE.txt README.txt
%{_libdir}/libvigraimpex.so.*

%files devel
%defattr(-, root, root,-)
%{_bindir}/vigra-config
%{_includedir}/vigra
%{_libdir}/libvigraimpex.so
%doc doc/vigra/*.html doc/vigra/*.css doc/vigra/*.png doc/vigra/*.gif doc/vigra/*.ps doc/vigra/documents/

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.6.0-2.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 08 2009 Bruno Postle - 1.6.0-1
- Update to latest release

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.5.0-4
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Bruno Postle <bruno@postle.net> 1.5.0-3
  - Bumping for Jesse

* Mon Feb 19 2007 Bruno Postle <bruno@postle.net> 1.5.0-2
  - update to 1.5.0 release
  - fix bug 228926: vigra: $RPM_OPT_FLAGS not used

* Sun Nov 23 2003 Bruno Postle <bruno@postle.net>
  - initial package


