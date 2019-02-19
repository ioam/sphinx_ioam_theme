import os.path
import param

NAME = "sphinx_pyviz_theme"

# version comes from git if available, otherwise from .version file
__version__ = str(param.version.Version(fpath=__file__, archive_commit="$Format:%h$",
                                        reponame=NAME))

def setup(app):
    app.add_html_theme('sphinx_pyviz_theme', os.path.abspath(os.path.dirname(__file__)))

