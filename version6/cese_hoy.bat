cls
@echo off

for /f %%a in ('cscript //nologo yester.vbs') do set yesterday=%%a
set BuscarFecha=%yesterday:~6,2%.%yesterday:~4,2%.%yesterday:~0,4%
set "BuscarNombre=CESADOS_%date:~5,2%%date:~8,2%%date:~11,4%.xls%"
rem set BuscarFecha="17.06.2019"
rem set BuscarNombre="CESADOS_18062019.XLS"
set "BuscarArchivo=\\xx.xx.x.x\RRHH\CESADOS\%BuscarNombre%"
set "DestinoArchivo=%CD%\prueba1.csv"
set "ResultadoArchivo=%CD%\prueba2.csv"

copy %BuscarArchivo% "%DestinoArchivo%" /Y
find "%BuscarFecha%" "%DestinoArchivo%" > "%ResultadoArchivo%"
del "%DestinoArchivo%"
REM pause>nul
exit