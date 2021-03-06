#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rgenoud
Version  : 5.8.3.0
Release  : 35
URL      : https://cran.r-project.org/src/contrib/rgenoud_5.8-3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rgenoud_5.8-3.0.tar.gz
Summary  : R Version of GENetic Optimization Using Derivatives
Group    : Development/Tools
License  : GPL-3.0
Requires: R-rgenoud-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
## rgenoud: R-GENetic Optimization Using Derivatives (RGENOUD)
Walter R. Mebane, Jr. and Jasjeet S. Sekhon

%package lib
Summary: lib components for the R-rgenoud package.
Group: Libraries

%description lib
lib components for the R-rgenoud package.


%prep
%setup -q -c -n rgenoud
cd %{_builddir}/rgenoud

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589567659

%install
export SOURCE_DATE_EPOCH=1589567659
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rgenoud
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rgenoud
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rgenoud
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rgenoud || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rgenoud/CITATION
/usr/lib64/R/library/rgenoud/DESCRIPTION
/usr/lib64/R/library/rgenoud/INDEX
/usr/lib64/R/library/rgenoud/Meta/Rd.rds
/usr/lib64/R/library/rgenoud/Meta/features.rds
/usr/lib64/R/library/rgenoud/Meta/hsearch.rds
/usr/lib64/R/library/rgenoud/Meta/links.rds
/usr/lib64/R/library/rgenoud/Meta/nsInfo.rds
/usr/lib64/R/library/rgenoud/Meta/package.rds
/usr/lib64/R/library/rgenoud/Meta/vignette.rds
/usr/lib64/R/library/rgenoud/NAMESPACE
/usr/lib64/R/library/rgenoud/R/rgenoud
/usr/lib64/R/library/rgenoud/R/rgenoud.rdb
/usr/lib64/R/library/rgenoud/R/rgenoud.rdx
/usr/lib64/R/library/rgenoud/doc/index.html
/usr/lib64/R/library/rgenoud/doc/rgenoud.R
/usr/lib64/R/library/rgenoud/doc/rgenoud.Rnw
/usr/lib64/R/library/rgenoud/doc/rgenoud.bib
/usr/lib64/R/library/rgenoud/doc/rgenoud.pdf
/usr/lib64/R/library/rgenoud/help/AnIndex
/usr/lib64/R/library/rgenoud/help/aliases.rds
/usr/lib64/R/library/rgenoud/help/paths.rds
/usr/lib64/R/library/rgenoud/help/rgenoud.rdb
/usr/lib64/R/library/rgenoud/help/rgenoud.rdx
/usr/lib64/R/library/rgenoud/html/00Index.html
/usr/lib64/R/library/rgenoud/html/R.css
/usr/lib64/R/library/rgenoud/tests/tests.R
/usr/lib64/R/library/rgenoud/tests/tests.Rout.save
/usr/lib64/R/library/rgenoud/tests/testthat.R
/usr/lib64/R/library/rgenoud/tests/testthat/test-Example.R
/usr/lib64/R/library/rgenoud/tests/testthat/test-genoud_fixed_seed.R
/usr/lib64/R/library/rgenoud/tests/testthat/test-genoud_no_given_seed.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/rgenoud/libs/rgenoud.so
/usr/lib64/R/library/rgenoud/libs/rgenoud.so.avx2
/usr/lib64/R/library/rgenoud/libs/rgenoud.so.avx512
