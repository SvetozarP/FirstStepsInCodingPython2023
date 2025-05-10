import os

while True:
    with open('prank.bat', 'w') as file:
        file.write('@echo off\n')
        file.write('color 0A\n')
        file.write('echo Are you scared?????\n')
        file.write('pause >nul\n')

    os.system('start prank.bat')
