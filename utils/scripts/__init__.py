from .generate_erd_script import generate_erd
from .rename_project_script import rename_project

USER_DEFINED_SCRIPTS = ["generate_erd", "rename_project"]


def utils_scripts_resolver(argv: list):
    if len(argv) >= 2:
        if argv[1] == "generate_erd":
            generate_erd()

        if argv[1] == "rename_project" and len(argv) == 3:
            rename_project(argv[2])
        else:
            print('project name not specified')
