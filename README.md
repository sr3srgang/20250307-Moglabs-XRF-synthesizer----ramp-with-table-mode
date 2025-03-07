Resources and example codes for generating dynamic RF signals (optionally with external contorl) via the table mode of Moglabs RF synthesizer (e.g., XRF)

Recommended to create a conda env at `./.conda` in this folder to run Python scripts (e.g., via vscode). `.gitignore` prevent the conda env to be cached in the `git` so that different computer can create/configure their own env. One can also create the env manually in a terminal:
```bash
    cd /path/to/project/folder
    conda create -p ./.conda python=3.11 numpy scipy matplotlib ipykernel
```
Tested for Python 3.11. `mogdevice` and `six` package should be installed:
```bash
pip install mogdevice six
```




