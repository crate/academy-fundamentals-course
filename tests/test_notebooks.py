from pathlib import Path

from pueblo.testing.notebook import generate_notebook_tests, list_notebooks, run_notebook

HERE = Path(__file__).parent
ROOT = HERE.parent


def pytest_generate_tests(metafunc):
    """
    Generate pytest test case per Jupyter Notebook.
    """
    notebooks_root = ROOT / "notebooks"
    notebook_paths = list_notebooks(notebooks_root)
    generate_notebook_tests(metafunc, notebook_paths=notebook_paths)


def test_notebook(notebook):
    """
    Execute Jupyter Notebook, one test case per .ipynb file.
    """
    run_notebook(notebook)
