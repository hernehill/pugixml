name = "pugixml"

version = "1.14.hh.1.0.0"

authors = [
    "Arseny Kapoulkine",
]

description = """Light-weight XML parser for C++"""

with scope("config") as c:
    import os

    c.release_packages_path = os.environ["HH_REZ_REPO_RELEASE_EXT"]

requires = []

private_build_requires = []

variants = []


def commands():
    env.REZ_PUGIXML_ROOT = "{root}"
    env.PUGIXML_ROOT = "{root}"
    env.PUGIXML_LOCATION = "{root}"
    env.pugixml_ROOT = "{root}"
    env.pugixml_LOCATION = "{root}"
    env.pugixml_INCLUDE_DIR = "{root}/include"
    env.pugixml_LIBRARY_DIR = "{root}/lib64"

    env.LD_LIBRARY_PATH.append("{root}/lib64")


uuid = "repository.pugixml"
build_system = "cmake"
