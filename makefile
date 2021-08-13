build:
	@pyinstaller run.py --onefile

clean:
	@rm -rf build dist