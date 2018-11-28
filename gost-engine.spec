%define lbname gost
%define engver 1.1

%global commit0 0b50e0028fa9d2cfb9648f8f3209e89d75e311c1
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20181118

Name: gost-engine
Version: 1.1.0.3
Release: 1.%{date}git%{shortcommit0}%{?dist}

License: BSD
Summary: Implementation of the Russian GOST crypto algorithms
URL: https://github.com/%{name}/engine
Source0: %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: openssl-devel
BuildRequires: ninja-build
BuildRequires: cmake
BuildRequires: gcc

%description
A reference implementation of the Russian GOST crypto algorithms for OpenSSL.

%prep
%autosetup -n engine-%{commit0}
mkdir -p %{_target_platform}

%build
pushd %{_target_platform}
    %cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    ..
popd
%ninja_build -C %{_target_platform}

%install
%ninja_install -C %{_target_platform}

%files
%doc README.md README.%{lbname} INSTALL.md
%license LICENSE
%{_bindir}/%{lbname}*
%{_libdir}/engines-%{engver}/%{lbname}.so
%{_mandir}/man1/%{lbname}*.*

%changelog
* Wed Nov 28 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1.0.3-1.20181118git0b50e00
- Initial SPEC release.
