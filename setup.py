from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "Voltaire Project Hack",
    version = "1",
    description = "Programme d'aide au Projet Voltaire :-)",
    executables = [Executable("launcher.py")],
)
