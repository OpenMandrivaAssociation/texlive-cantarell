Name:		texlive-cantarell
Version:	54512
Release:	1
Summary:	LaTeX support for the Cantarell font family
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/cantarell
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cantarell.r54512.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cantarell.doc.r54512.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Cantarell is a contemporary Humanist sans serif designed by
Dave Crossland and Jakub Steiner. This font, delivered under
the OFL version 1.1, is available on the GNOME download server.
The present package provides support for this font in LaTeX. It
includes Type 1 versions of the fonts, converted for this
package using FontForge from its sources, for full support with
Dvips.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/cantarell
%{_texmfdistdir}/fonts/map/dvips/cantarell
%{_texmfdistdir}/fonts/tfm/gnome/cantarell
%{_texmfdistdir}/fonts/type1/gnome/cantarell
%{_texmfdistdir}/fonts/vf/gnome/cantarell
%{_texmfdistdir}/fonts/opentype/gnome/cantarell
%{_texmfdistdir}/tex/latex/cantarell
%doc %{_texmfdistdir}/doc/fonts/cantarell

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
