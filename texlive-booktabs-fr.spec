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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The translation comes from a collection provided by Benjamin Bayart.

