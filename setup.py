from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': ["app", "MySQLdb", "sqlalchemy", "jinja2"], 'excludes': []}

bdist_msi_options = {
    'add_to_path': False,
    'initial_target_dir': r'[ProgramFilesFolder]\%s' % (r"Wistron AMS"),
    }

executables = [
    Executable(
        script="run.py",
        base="Console",
        targetName = 'Wistron AMS',
        icon='logo.ico',
        shortcutName = 'Wistron AMS',
        shortcutDir = 'DesktopFolder'
    )
]

setup(name='Wistron AMS',
      version = '1.0',
      description = 'Attendance Management Tool.',
      options = {
                'bdist_msi': bdist_msi_options,
                'build_exe': build_options
                },
      executables = executables)
