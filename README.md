# Conan packages for third party libraries used at CCDC

This repository is based on the [bincrafters repository template](https://github.com/bincrafters/templates) and makes use of bincrafters-package-tools to build the packages

## Finding the latest versions of packages on conan-center

```
for pkg in $(LOCAL_CONAN_INDEX=./conan-ccdc-index cit info package | sed -e 's/- //')
do
conan search -r public-conan-center --raw "$pkg/*" | tail -n 1
done
```
