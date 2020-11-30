import cx_Freeze

executables = [cx_Freeze.Executable("MinMaxConnect4.py")]

cx_Freeze.setup(
    name="Min Max Connect 4",
    options={"build_exe": {"packages":["pygame","sys","bitstring","math"], "include_files":["background3_3.png","Poppins-Italic.ttf","Poppins-ExtraLight.ttf"]}},
    executables = executables

    )
