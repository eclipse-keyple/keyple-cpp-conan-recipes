# Eclipse Keyple Conan recipes

Conan 2 recipes for the Eclipse Keyple C++ libraries, laid out like
[conan-center-index](https://github.com/conan-io/conan-center-index) so that
they can be used as a
[local-recipes-index](https://docs.conan.io/2/devops/devops_local_recipes_index.html)
remote (Conan >= 2.2).

## Usage

Keyple depends on the Keypop APIs, so both indexes are needed:

```sh
git clone https://github.com/eclipse-keypop/keypop-cpp-conan-recipes
git clone https://github.com/eclipse-keyple/keyple-cpp-conan-recipes
conan remote add keypop ./keypop-cpp-conan-recipes --type=local-recipes-index
conan remote add keyple ./keyple-cpp-conan-recipes --type=local-recipes-index
conan install --requires=keyple-card-calypso-cpp-lib/3.2.2 --build=missing
```

Packages are built from the tagged GitHub release sources on first use.

## Adding a version

1. Add the version to `recipes/<package>/config.yml`.
2. Add its source URL and `sha256` to `recipes/<package>/all/conandata.yml`.
3. Release tags made before Conan support was added need the CMake changes
   back-ported as a patch (see `all/patches/`). Releases that already ship a
   Conan-ready `CMakeLists.txt` need no patch.
4. Check it with `conan create recipes/<package>/all --version=<version>`.
