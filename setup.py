from setuptools import setup

NAME = 'sphinx_pyviz_theme'
DESCRIPTION = "PyViz theme for use with nbsite"

# duplicated from pyct.build.get_setup_version until pyct[build] >0.4.6 lands
def get_setup_version(root, reponame):
    """
    Helper to get the current version from either git describe or the
    .version file (if available) - allows for param to not be available.
    Normally used in setup.py as follows:
    >>> from pyct.build import get_setup_version
    >>> version = get_setup_version(__file__, reponame)  # noqa
    """
    import os
    import json

    filepath = os.path.abspath(os.path.dirname(root))
    version_file_path = os.path.join(filepath, reponame, '.version')
    try:
        from param import version
    except:
        version = None
    if version is not None:
        return version.Version.setup_version(filepath, reponame, archive_commit="$Format:%h$")
    else:
        print("WARNING: param>=1.6.0 unavailable. If you are installing a package, this warning can safely be ignored. If you are creating a package or otherwise operating in a git repository, you should install param>=1.6.0.")
        return json.load(open(version_file_path, 'r'))['version_string']

setup_args = dict(
    name=NAME,
    version=get_setup_version(__file__, NAME),
    url="https://github.com/pyviz-dev/sphinx_pyviz_theme",
    description=DESCRIPTION,
    license="BSD-3",
    zip_safe=False,
    packages=[NAME],
    package_data={NAME: [
        'theme.conf',
        '*.html',
        'includes/*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/images/*.*'
    ]},
    include_package_data=True,
    entry_points = {
        'sphinx.html_themes': [
            'sphinx_pyviz_theme = sphinx_pyviz_theme',
        ]
    },
    python_requires = ">=2.7",

    install_requires = [
        "sphinx",
        "param >=1.7.0",
    ],
    extras_require = {
        'build': [
            "param >=1.7.0",
            "setuptools",
        ]
    }
)

if __name__=="__main__":
    setup(**setup_args)
