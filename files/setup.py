from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "Projet_Voltaire_Hack",
    version = "1",
    description = "A project developped by BAALBAKYA",
    executables = [Executable("voltaire_project_hack.py")],
)