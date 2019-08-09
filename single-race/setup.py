import cx_Freeze

executables = [cx_Freeze.Executable("race.py")]

cx_Freeze.setup(
    name = "Rainy Formula",
    options = {"build_exe" : {  "packages" : ["pygame"], 
				"include_files": ["racecar.png", "caricon.png", "crash.wav", "jazz.wav"]
}},
    executables = executables
)
