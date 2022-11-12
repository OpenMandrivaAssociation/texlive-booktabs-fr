Name:		texlive-booktabs-fr
Version:	21948
Release:	1
Summary:	French translation of booktabs documentation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/booktabs/fr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/booktabs-fr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/booktabs-fr.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The translation comes from a collection provided by Benjamin
Bayart.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/booktabs-fr/README
%doc %{_texmfdistdir}/doc/latex/booktabs-fr/f-booktabs.dtx
%doc %{_texmfdistdir}/doc/latex/booktabs-fr/f-booktabs.pdf
%doc %{_texmfdistdir}/doc/latex/booktabs-fr/ltxdoc.cfg

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
