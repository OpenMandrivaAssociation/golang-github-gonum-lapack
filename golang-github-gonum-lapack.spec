# http://github.com/gonum/lapack
%global provider_prefix github.com/gonum/lapack
%global gobaseipath     %{provider_prefix}
%global commit          88ec467285859a6cd23900147d250a8af1f38b10
%global commitdate      20150716

%gocraftmeta -i

Name:           %{goname}
Version:        0
Release:        0.11.%{commitdate}git%{shortcommit}%{?dist}
Summary:        A lapack implementation for go
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

Patch0:         add-license.patch
# Took me more than 1 hour to figure this out!!!
Patch1:         use-system-library.patch

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: lapack-devel
Requires:      lapack-devel

BuildRequires: golang(github.com/gonum/blas)
BuildRequires: golang(github.com/gonum/blas/blas64)
BuildRequires: golang(github.com/gonum/floats)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{gobaseipath} prefix.

%prep
%gosetup
%patch0 -p1
%patch1 -p1

%install
%goinstall

%check
#%%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.11.20150716git88ec467
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git88ec467
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git88ec467
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git88ec467
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.7.git88ec467
- Polish the spec file
  related: #1269907

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git88ec467
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.git88ec467
- https://fedoraproject.org/wiki/Changes/golang1.7

* Thu Jul 14 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0-0.4.git88ec467
- Fix Exclusive arches for golang/openblas

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.git88ec467
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git88ec467
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git88ec467
- First package for Fedora
  resolves: #1269907
