# -*- mode: python ; coding: utf-8 -*-


a_client = Analysis(
    ['capyknock_client.py'],
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
pyz_client = PYZ(a_client.pure)

exe_client = EXE(
    pyz_client,
    a_client.scripts,
    [],
    exclude_binaries=True,
    name='capyknock_client',
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

a_qrcode = Analysis(
    ['capyknock_qrcode.py'],
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
pyz_qrcode = PYZ(a_qrcode.pure)

exe_qrcode = EXE(
    pyz_qrcode,
    a_qrcode.scripts,
    [],
    exclude_binaries=True,
    name='capyknock_qrcode',
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
    exe_client,
    a_client.binaries,
    a_client.datas,
    exe_qrcode,
    a_qrcode.binaries,
    a_qrcode.datas,	
    strip=False,
    upx=True,
    upx_exclude=[],
    name='capyknock_client',
)
