%define 	module	WebOb
Summary:	WSGI request and response object
Name:		python-%{module}
Version:	1.0
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/W/WebOb/%{module}-%{version}.tar.gz
# Source0-md5:	2949c7b4cee48aa10ddc244eaff5d38b
URL:		http://pythonpaste.org/webob/
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WebOb provides wrappers around the WSGI request environment, and an
object to help create WSGI responses.

The objects map much of the specified behavior of HTTP, including
header parsing and accessors for other standard parts of the
environment.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/WebOb-*.egg-info
%endif
%dir %{py_sitescriptdir}/webob
%{py_sitescriptdir}/webob/*.py[co]
%dir %{py_sitescriptdir}/webob/util
%{py_sitescriptdir}/webob/util/*.py[co]
