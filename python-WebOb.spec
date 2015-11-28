#
# Conditional build:
%bcond_without	python3	# CPython 3.x module

%define 	module	WebOb
Summary:	WSGI request and response object
Name:		python-%{module}
Version:	1.2.3
Release:	4
License:	MIT
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/W/WebOb/%{module}-%{version}.tar.gz
# Source0-md5:	11825b7074ba7043e157805e4e6e0f55
URL:		http://webob.org/
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WebOb provides wrappers around the WSGI request environment, and an
object to help create WSGI responses.

The objects map much of the specified behavior of HTTP, including
header parsing and accessors for other standard parts of the
environment.

%package -n python3-%{module}
Summary:	Add options to doctest examples while they are running
Group:		Libraries/Python

%description -n python3-%{module}
WebOb provides wrappers around the WSGI request environment, and an
object to help create WSGI responses.

The objects map much of the specified behavior of HTTP, including
header parsing and accessors for other standard parts of the
environment.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/webob
%{py_sitescriptdir}/webob/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/WebOb-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%dir %{py3_sitescriptdir}/webob
%{py3_sitescriptdir}/webob/*.py
%{py3_sitescriptdir}/webob/__pycache__
%{py3_sitescriptdir}/WebOb-%{version}-py*.egg-info
%endif
