pyinstaller capyknock_server_win_x64.spec
copy capyknock_server-conf.json dist\capyknock_server
copy capyknock_keygen-conf.json dist\capyknock_server

pyinstaller capyknock_client_win_x64.spec
copy capyknock_client-conf.json dist\capyknock_client
