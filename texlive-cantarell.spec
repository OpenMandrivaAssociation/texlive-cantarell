%global tl_name cantarell
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.2
Release:	%{tl_revision}.1
Summary:	LaTeX support for the Cantarell font family
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cantarell
License:	ofl lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cantarell.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cantarell.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Cantarell is a contemporary Humanist sans serif designed by Dave
Crossland and Jakub Steiner. This font, delivered under the OFL version
1.1, is available on the GNOME download server. The present package
provides support for this font in LaTeX. It includes Type 1 versions of
the fonts, converted for this package using FontForge from its sources,
for full support with Dvips.

