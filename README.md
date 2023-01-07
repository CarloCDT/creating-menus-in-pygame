# Creating Menus in PyGame
Simple templete of menus in PyGame. 
To create executable file for the game run:

`pyinstaller --onefile main.py --collect-data img --windowed`

Modify `main.spec` empty `datas=[]` with `datas=[('img/*','img')]` and run:

`pyinstaller main.spec`

The executable file can be found in the dist directory, wioth the name `main.exe`.
