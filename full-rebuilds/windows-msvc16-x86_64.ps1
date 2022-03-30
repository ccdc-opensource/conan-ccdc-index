$WS=Resolve-Path -Path "$($PSScriptRoot)/../.."

# This presumes you have a python virtualenv in citvenv with conan-ccdc-index-tools installed
. "$($WS)\citvenv\Scripts\Activate.ps1"

# choco install -y cmake.install --installargs 'ADD_CMAKE_TO_PATH=System'
# choco install -y python2

$CONAN_USER="cbantaloukas"
$Env:LOCAL_CONAN_INDEX="$($WS)/conan-ccdc-index"
$Env:LCI_PLATFORM_COMBINATION="native-windows-msvc16-x86_64"
Remove-Item -recurse -force "$($HOME)/.conan" -ErrorAction SilentlyContinue
conan config install "$($WS)/conan-ccdc-common-configuration"

conan user --remote ccdc-3rdparty-conan-testing --password=$Env:ARTIFACTORY_API_KEY $CONAN_USER
conan user --remote public-conan-center --password=$Env:ARTIFACTORY_API_KEY $CONAN_USER
conan user --remote public-conan-bincrafters --password=$Env:ARTIFACTORY_API_KEY $CONAN_USER


cit publish recipe

cit build
