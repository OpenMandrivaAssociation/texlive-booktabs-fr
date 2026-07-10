%global tl_name booktabs-fr
%global tl_revision 79121

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.00
Release:	%{tl_revision}.1
Summary:	French translation of booktabs documentation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/translations/booktabs/fr
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/booktabs-fr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/booktabs-fr.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The translation comes from a collection provided by Benjamin Bayart.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/doc/latex/booktabs-fr
%doc %{_datadir}/texmf-dist/doc/latex/booktabs-fr/README
%doc %{_datadir}/texmf-dist/doc/latex/booktabs-fr/f-booktabs.dtx
%doc %{_datadir}/texmf-dist/doc/latex/booktabs-fr/f-booktabs.pdf
%doc %{_datadir}/texmf-dist/doc/latex/booktabs-fr/ltxdoc.cfg
