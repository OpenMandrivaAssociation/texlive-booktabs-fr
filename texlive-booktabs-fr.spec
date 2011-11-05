# revision 21948
# category Package
# catalog-ctan /info/translations/booktabs/fr
# catalog-date 2011-04-03 23:29:51 +0200
# catalog-license lppl
# catalog-version 1.00
Name:		texlive-booktabs-fr
Version:	1.00
Release:	1
Summary:	French translation of booktabs documentation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/booktabs/fr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/booktabs-fr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/booktabs-fr.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The translation comes from a collection provided by Benjamin
Bayart.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/booktabs-fr/README
%doc %{_texmfdistdir}/doc/latex/booktabs-fr/f-booktabs.dtx
%doc %{_texmfdistdir}/doc/latex/booktabs-fr/f-booktabs.pdf
%doc %{_texmfdistdir}/doc/latex/booktabs-fr/ltxdoc.cfg
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}