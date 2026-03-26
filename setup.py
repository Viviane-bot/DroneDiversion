from cx_Freeze import setup, Executable
executables = [Executable("main.py")]

setup(
    name = "DorneDiverson",
    version = "1.0",
    description = "Dorne Diverson app",
    options = {"build_exe": {"packages": ["pygame"]}},
    executables = executables
)