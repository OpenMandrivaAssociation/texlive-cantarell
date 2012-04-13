# revision 25752
# category Package
# catalog-ctan /fonts/cantarell
# catalog-date 2012-03-27 12:09:20 +0200
# catalog-license lppl1.3
# catalog-version 2.3
Name:		texlive-cantarell
Version:	2.3
Release:	1
Summary:	LaTeX support for the Cantarell font family
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/cantarell
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cantarell.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cantarell.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cantarell.source.tar.xz
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
%{_texmfdistdir}/fonts/afm/public/cantarell/Cantarell-Bold.afm
%{_texmfdistdir}/fonts/afm/public/cantarell/Cantarell-Regular.afm
%{_texmfdistdir}/fonts/enc/dvips/cantarell/cantarell-01.enc
%{_texmfdistdir}/fonts/enc/dvips/cantarell/cantarell-02.enc
%{_texmfdistdir}/fonts/map/dvips/cantarell/cantarell.map
%{_texmfdistdir}/fonts/tfm/public/cantarell/Cantarell-Bold-01.tfm
%{_texmfdistdir}/fonts/tfm/public/cantarell/Cantarell-Bold-02.tfm
%{_texmfdistdir}/fonts/tfm/public/cantarell/Cantarell-Bold-Slanted-01.tfm
%{_texmfdistdir}/fonts/tfm/public/cantarell/Cantarell-Bold-Slanted-02.tfm
%{_texmfdistdir}/fonts/tfm/public/cantarell/Cantarell-Bold-Slanted-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/cantarell/Cantarell-Bold-Slanted-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/cantarell/Cantarell-Bold-Slanted-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/cantarell/Cantarell-Bold-Slanted-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/cantarell/Cantarell-Bold-Slanted-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/cantarell/Cantarell-Bold-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/cantarell/Cantarell-Bold-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/cantarell/Cantarell-Bold-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/cantarell/Cantarell-Bold-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/cantarell/Cantarell-Bold-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/cantarell/Cantarell-Regular-01.tfm
%{_texmfdistdir}/fonts/tfm/public/cantarell/Cantarell-Regular-02.tfm
%{_texmfdistdir}/fonts/tfm/public/cantarell/Cantarell-Regular-Slanted-01.tfm
%{_texmfdistdir}/fonts/tfm/public/cantarell/Cantarell-Regular-Slanted-02.tfm
%{_texmfdistdir}/fonts/tfm/public/cantarell/Cantarell-Regular-Slanted-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/cantarell/Cantarell-Regular-Slanted-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/cantarell/Cantarell-Regular-Slanted-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/cantarell/Cantarell-Regular-Slanted-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/cantarell/Cantarell-Regular-Slanted-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/cantarell/Cantarell-Regular-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/cantarell/Cantarell-Regular-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/cantarell/Cantarell-Regular-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/cantarell/Cantarell-Regular-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/cantarell/Cantarell-Regular-ts1.tfm
%{_texmfdistdir}/fonts/type1/public/cantarell/Cantarell-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/cantarell/Cantarell-Regular.pfb
%{_texmfdistdir}/fonts/vf/public/cantarell/Cantarell-Bold-Slanted-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/cantarell/Cantarell-Bold-Slanted-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/cantarell/Cantarell-Bold-Slanted-ot1.vf
%{_texmfdistdir}/fonts/vf/public/cantarell/Cantarell-Bold-Slanted-t1.vf
%{_texmfdistdir}/fonts/vf/public/cantarell/Cantarell-Bold-Slanted-ts1.vf
%{_texmfdistdir}/fonts/vf/public/cantarell/Cantarell-Bold-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/cantarell/Cantarell-Bold-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/cantarell/Cantarell-Bold-ot1.vf
%{_texmfdistdir}/fonts/vf/public/cantarell/Cantarell-Bold-t1.vf
%{_texmfdistdir}/fonts/vf/public/cantarell/Cantarell-Bold-ts1.vf
%{_texmfdistdir}/fonts/vf/public/cantarell/Cantarell-Regular-Slanted-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/cantarell/Cantarell-Regular-Slanted-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/cantarell/Cantarell-Regular-Slanted-ot1.vf
%{_texmfdistdir}/fonts/vf/public/cantarell/Cantarell-Regular-Slanted-t1.vf
%{_texmfdistdir}/fonts/vf/public/cantarell/Cantarell-Regular-Slanted-ts1.vf
%{_texmfdistdir}/fonts/vf/public/cantarell/Cantarell-Regular-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/cantarell/Cantarell-Regular-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/cantarell/Cantarell-Regular-ot1.vf
%{_texmfdistdir}/fonts/vf/public/cantarell/Cantarell-Regular-t1.vf
%{_texmfdistdir}/fonts/vf/public/cantarell/Cantarell-Regular-ts1.vf
%{_texmfdistdir}/tex/latex/cantarell/cantarell.sty
%{_texmfdistdir}/tex/latex/cantarell/ot1fca.fd
%{_texmfdistdir}/tex/latex/cantarell/t1fca.fd
%{_texmfdistdir}/tex/latex/cantarell/ts1fca.fd
%doc %{_texmfdistdir}/doc/fonts/cantarell/CHANGES
%doc %{_texmfdistdir}/doc/fonts/cantarell/README
%doc %{_texmfdistdir}/doc/fonts/cantarell/cantarell-samples.pdf
%doc %{_texmfdistdir}/doc/fonts/cantarell/cantarell-samples.tex
%doc %{_texmfdistdir}/doc/fonts/cantarell/cantarell.pdf
%doc %{_texmfdistdir}/doc/fonts/cantarell/cantarell.tex
%doc %{_texmfdistdir}/doc/fonts/cantarell/manifest.txt
#- source
%doc %{_texmfdistdir}/source/fonts/cantarell/Cantarell-Bold.sfd
%doc %{_texmfdistdir}/source/fonts/cantarell/Cantarell-Regular.sfd
%doc %{_texmfdistdir}/source/fonts/cantarell/Makefile
%doc %{_texmfdistdir}/source/fonts/cantarell/cantarell-01.etx
%doc %{_texmfdistdir}/source/fonts/cantarell/cantarell-02.etx
%doc %{_texmfdistdir}/source/fonts/cantarell/cantarell-drv.tex
%doc %{_texmfdistdir}/source/fonts/cantarell/cantarell-fixlatin.mtx
%doc %{_texmfdistdir}/source/fonts/cantarell/cantarell-fixtextcomp.mtx
%doc %{_texmfdistdir}/source/fonts/cantarell/cantarell-map.tex
%doc %{_texmfdistdir}/source/fonts/cantarell/sfd2type1.pe

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
