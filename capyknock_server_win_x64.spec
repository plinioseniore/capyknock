# -*- mode: python ; coding: utf-8 -*-


a_server = Analysis(
    ['capyknock_server.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz_server = PYZ(a_server.pure)

exe_server = EXE(
    pyz_server,
    a_server.scripts,
    [],
    exclude_binaries=True,
    name='capyknock_server',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
a_keygen = Analysis(
    ['capyknock_keygen.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz_keygen = PYZ(a_keygen.pure)

exe_keygen = EXE(
    pyz_keygen,
    a_keygen.scripts,
    [],
    exclude_binaries=True,
    name='capyknock_keygen',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
a_bainip = Analysis(
    ['capyknock_banip.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz_bainip = PYZ(a_bainip.pure)

exe_bainip = EXE(
    pyz_bainip,
    a_bainip.scripts,
    [],
    exclude_binaries=True,
    name='capyknock_banip',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe_server,
    a_server.binaries,
    a_server.datas,
    exe_keygen,
    a_keygen.binaries,
    a_keygen.datas,	
    exe_bainip,
    a_bainip.binaries,
    a_bainip.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='capyknock_server',
)
