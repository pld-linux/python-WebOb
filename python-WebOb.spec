#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

%define 	module	WebOb
Summary:	WSGI request and response object
Summary(pl.UTF-8):	Obiekty żądań i odpowiedzi WSGI
Name:		python-%{module}
Version:	1.8.2
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/WebOb/
Source0:	https://files.pythonhosted.org/packages/source/W/WebOb/%{module}-%{version}.tar.gz
# Source0-md5:	d04756e6683fedddba52eafbe9adf404
URL:		https://webob.org/
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest >= 3.1.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest >= 3.1.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg >= 1.3.1
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WebOb provides wrappers around the WSGI request environment, and an
object to help create WSGI responses.

The objects map much of the specified behavior of HTTP, including
header parsing and accessors for other standard parts of the
environment.

%description -l pl.UTF-8
Moduł WebOb udostępnia opakowanie środowiska żądań WSGI oraz
obiekty pomagające przy tworzeniu odpowiedzi WSGI.

Obiekty odwzorowują większość określonego zachowania HTTP, w tym
analizę nagłówków oraz dostęp do innych standardowych elementów
środowiska.

%package -n python3-%{module}
Summary:	WSGI request and response object
Summary(pl.UTF-8):	Obiekty żądań i odpowiedzi WSGI
Group:		Libraries/Python

%description -n python3-%{module}
WebOb provides wrappers around the WSGI request environment, and an
object to help create WSGI responses.

The objects map much of the specified behavior of HTTP, including
header parsing and accessors for other standard parts of the
environment.

%description -n python3-%{module} -l pl.UTF-8
Moduł WebOb udostępnia opakowanie środowiska żądań WSGI oraz
obiekty pomagające przy tworzeniu odpowiedzi WSGI.

Obiekty odwzorowują większość określonego zachowania HTTP, w tym
analizę nagłówków oraz dostęp do innych standardowych elementów
środowiska.

%package apidocs
Summary:	API documentation for Python WebOb module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona WebOb
Group:		Documentation

%description apidocs
API documentation for Python WebOb module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona WebOb.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python} -m unittest discover -s tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python3} -m unittest discover -s tests
%endif
%endif

%if %{with doc}
PYTHONPATH=$(pwd)/src \
%{__make} -C docs html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.txt HISTORY.txt README.rst docs/license.txt
%{py_sitescriptdir}/webob
%{py_sitescriptdir}/WebOb-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES.txt HISTORY.txt README.rst docs/license.txt
%{py3_sitescriptdir}/webob
%{py3_sitescriptdir}/WebOb-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,api,experimental,*.html,*.js}
%endif
