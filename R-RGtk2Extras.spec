%global packname  RGtk2Extras
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.6.1
Release:          2
Summary:          Data frame editor and dialog making wrapper for RGtk2
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/RGtk2Extras_0.6.1.tar.gz
Requires:         R-methods R-RGtk2 R-gWidgets R-gWidgetsRGtk2
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-methods R-RGtk2 R-gWidgets R-gWidgetsRGtk2
BuildRequires:    gtk2-devel
BuildRequires:    pkgconfig(libglade-2.0)
BuildRequires:    x11-server-xvfb

%description
Useful add-ons for RGtk2

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
xvfb-run %{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
