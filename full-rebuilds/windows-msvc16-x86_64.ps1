$WS=Resolve-Path -Path "$($PSScriptRoot)/../.."

# This presumes you have a python virtualenv in citvenv with conan-ccdc-index-tools installed
. "$($WS)\citvenv\Scripts\Activate.ps1"

# choco install -y cmake.install --installargs 'ADD_CMAKE_TO_PATH=System'
# choco install -y python2

$CONAN_USER="cbantaloukas"
$Env:LOCAL_CONAN_INDEX="$($WS)/conan-ccdc-index"

Remove-Item -recurse -force "$($HOME)/.conan" -ErrorAction SilentlyContinue
conan config install "$($WS)/conan-ccdc-common-configuration"

conan user --remote ccdc-3rdparty-conan --password=$Env:ARTIFACTORY_API_KEY $CONAN_USER
conan user --remote ccdc-3rdparty-conan-testing --password=$Env:ARTIFACTORY_API_KEY $CONAN_USER
conan user --remote public-conan-center --password=$Env:ARTIFACTORY_API_KEY $CONAN_USER
conan user --remote public-conan-bincrafters --password=$Env:ARTIFACTORY_API_KEY $CONAN_USER


cit publish recipe

cit build --platform-combination native-windows-msvc16-x86_64 zlib
cit build --platform-combination native-windows-msvc16-x86_64 bzip2
cit build --platform-combination native-windows-msvc16-x86_64 zstd
cit build --platform-combination native-windows-msvc16-x86_64 brotli
# cit build --platform-combination native-windows-msvc16-x86_64 gnu-config
# cit build --platform-combination native-windows-msvc16-x86_64 libffi
# cit build --platform-combination native-windows-msvc16-x86_64 pcre
# cit build --platform-combination native-windows-msvc16-x86_64 pcre2
# cit build --platform-combination native-windows-msvc16-x86_64 expat
# cit build --platform-combination native-windows-msvc16-x86_64 openssl
# cit build --platform-combination native-windows-msvc16-x86_64 double-conversion
# cit build --platform-combination native-windows-msvc16-x86_64 libpng
# cit build --platform-combination native-windows-msvc16-x86_64 libjpeg
# cit build --platform-combination native-windows-msvc16-x86_64 freetype
# cit build --platform-combination native-windows-msvc16-x86_64 m4
# cit build --platform-combination native-windows-msvc16-x86_64 autoconf
# cit build --platform-combination native-windows-msvc16-x86_64 libelf
# cit build --platform-combination native-windows-msvc16-x86_64 libiconv
# cit build --platform-combination native-windows-msvc16-x86_64 libgettext
# cit build --platform-combination native-windows-msvc16-x86_64 ninja 
# cit build --platform-combination native-windows-msvc16-x86_64 meson
# cit build --platform-combination native-windows-msvc16-x86_64 pkgconf
# cit build --platform-combination native-windows-msvc16-x86_64 flex
# cit build --platform-combination native-windows-msvc16-x86_64 glib
# cit build --platform-combination native-windows-msvc16-x86_64 harfbuzz
# cit build --platform-combination native-windows-msvc16-x86_64 ccdcsqlite3 
# cit build --platform-combination native-windows-msvc16-x86_64 sqlite3
# cit build --platform-combination native-windows-msvc16-x86_64 opengl
# cit build --platform-combination native-windows-msvc16-x86_64 xorg
# cit build --platform-combination native-windows-msvc16-x86_64 cmake 
# cit build --platform-combination native-windows-msvc16-x86_64 nodejs
# cit build --platform-combination native-windows-msvc16-x86_64 bison
# cit build --platform-combination native-windows-msvc16-x86_64 gperf 
# cit build --platform-combination native-windows-msvc16-x86_64 automake 
# cit build --platform-combination native-windows-msvc16-x86_64 libtool
# cit build --platform-combination native-windows-msvc16-x86_64 libuuid
# ## 
# cit build --platform-combination native-windows-msvc16-x86_64 libxml2
# cit build --platform-combination native-windows-msvc16-x86_64 wayland
# cit build --platform-combination native-windows-msvc16-x86_64 wayland-protocols
# cit build --platform-combination native-windows-msvc16-x86_64 xkbcommon
# cit build --platform-combination native-windows-msvc16-x86_64 dbus
# ##
# cit build --platform-combination native-windows-msvc16-x86_64 fontconfig
# cit build --platform-combination native-windows-msvc16-x86_64 icu
# cit build --platform-combination native-windows-msvc16-x86_64 opus
# cit build --platform-combination native-windows-msvc16-x86_64 nspr
# cit build --platform-combination native-windows-msvc16-x86_64 nss
# cit build --platform-combination native-windows-msvc16-x86_64 vulkan-headers 
# cit build --platform-combination native-windows-msvc16-x86_64 vulkan-loader

# # # qt dependencies end here

# cit build --platform-combination native-windows-msvc16-x86_64 gtest
# cit build --platform-combination native-windows-msvc16-x86_64 installbuilder
# cit build --platform-combination native-windows-msvc16-x86_64 swig
# cit build --platform-combination native-windows-msvc16-x86_64 ccdcboost
# cit build --platform-combination native-windows-msvc16-x86_64 boost
# cit build --platform-combination native-windows-msvc16-x86_64 cpp-httplib
# cit build --platform-combination native-windows-msvc16-x86_64 cppad
# cit build --platform-combination native-windows-msvc16-x86_64 cryptopp
# cit build --platform-combination native-windows-msvc16-x86_64 fasta


# cit build --platform-combination native-windows-msvc16-x86_64 inchi
# cit build --platform-combination native-windows-msvc16-x86_64 lexactivator
# cit build --platform-combination native-windows-msvc16-x86_64 lexfloatclient
# cit build --platform-combination native-windows-msvc16-x86_64 lexfloatserver
# cit build --platform-combination native-windows-msvc16-x86_64 libarchive
# cit build --platform-combination native-windows-msvc16-x86_64 libxl
# cit build --platform-combination native-windows-msvc16-x86_64 libcurl
# cit build --platform-combination native-windows-msvc16-x86_64 mariadb-connector-c
# cit build --platform-combination native-windows-msvc16-x86_64 range-v3
# cit build --platform-combination native-windows-msvc16-x86_64 rapidjson
# cit build --platform-combination native-windows-msvc16-x86_64 gsoap
# cit build --platform-combination native-windows-msvc16-x86_64 openscenegraph
# cit build --platform-combination native-windows-msvc16-x86_64 povray
# cit build --platform-combination native-windows-msvc16-x86_64 rstatistics

# cit build --platform-combination native-windows-msvc16-x86_64 ccdc-main

# time cit build --platform-combination native-windows-msvc16-x86_64 qt

# time cit build --platform-combination native-windows-msvc16-x86_64 qwt
