import os, glob
from itertools import chain

outindex = "list.html"
outdir = "./gfiles/"
html5gamesin = "html5/"
rarchgamesin = "rarch/"
romdir = "roms/*"
flashgamesin = "flash/"
pregba = [".gba"]
pregen = [".mdx", ".md", ".smd", ".gen", ".sms", ".gg", ".sg"]
prenes = [".nes", ".fds", ".unf", ".unif"]
pren64 = [".n64", ".v64", ".z64", ".ndd"]
presnes = [".smc", ".sfc", ".swc", ".fig"]
index = '''<!DOCTYPE html>\n<html>\n<head>\n<title>Games List</title>\n<link rel="stylesheet" href="./css/style.css">\n</head>\n<body class="fbody">\n<div class="container">\n<div class="box">\n<input type="text" id="gsearchbar" onkeyup="var a=document.querySelectorAll('#glist a[href]');for(var i=0;i<a.length;i++)a[i].style.display=a[i].textContent.toUpperCase().indexOf(this.value.toUpperCase())!=-1?'block':'none'" autocomplete="off" spellcheck="false" placeholder="Search" />\n<div id="glist">\n%s\n</div>\n</div>\n</div>\n</body>\n</html>'''
alist = '''<a href="%s">%s</a>'''

# Make HTML5 lists
html5_1 = next(os.walk(outdir + html5gamesin))[1]
html5_2 = ["<h2>HTML5 Games</h2>"]

# Generate HTML code for HTML5 list
for x in range(0, len(html5_1)):
	html5_2.append(alist % (outdir + html5gamesin + html5_1[x], html5_1[x].capitalize()))

# Make GBA lists
gba_1 = list(chain.from_iterable([[os.path.basename(x) for x in glob.glob(outdir + rarchgamesin + romdir + y)] for y in pregba]))
gba_2 = ["\n<h2>Gameboy Advance</h2>", alist % (outdir + rarchgamesin + "?core=vba_next", "Upload ROM")]

# Generate HTML code for GBA list
for x in range(0, len(gba_1)):
	gba_2.append(alist % (outdir + rarchgamesin + "?core=vba_next&rom=" + gba_1[x], os.path.splitext(gba_1[x])[0].capitalize()))

# Make Genesis lists
gen_1 = list(chain.from_iterable([[os.path.basename(x) for x in glob.glob(outdir + rarchgamesin + romdir + y)] for y in pregen]))
gen_2 = ["\n<h2>Genesis / Master System</h2>", alist % (outdir + rarchgamesin + "?core=genesis_plus_gx", "Upload ROM")]

# Generate HTML code for Genesis list
for x in range(0, len(gen_1)):
	gen_2.append(alist % (outdir + rarchgamesin + "?core=genesis_plus_gx&rom=" + gen_1[x], os.path.splitext(gen_1[x])[0].capitalize()))

# Make N64 lists
n64_1 = list(chain.from_iterable([[os.path.basename(x) for x in glob.glob(outdir + rarchgamesin + romdir + y)] for y in pren64]))
n64_2 = ["\n<h2>Nintendo 64</h2>", alist % (outdir + rarchgamesin + "?core=mupen64plus_next", "Upload ROM")]

# Generate HTML code for N64 list
for x in range(0, len(n64_1)):
	n64_2.append(alist % (outdir + rarchgamesin + "?core=mupen64plus_next&rom=" + n64_1[x], os.path.splitext(n64_1[x])[0].capitalize()))

# Make NES lists
nes_1 = list(chain.from_iterable([[os.path.basename(x) for x in glob.glob(outdir + rarchgamesin + romdir + y)] for y in prenes]))
nes_2 = ["\n<h2>NES</h2>", alist % (outdir + rarchgamesin + "?core=nestopia", "Upload ROM")]

# Generate HTML code for NES list
for x in range(0, len(nes_1)):
	nes_2.append(alist % (outdir + rarchgamesin + "?core=nestopia&rom=" + nes_1[x], os.path.splitext(nes_1[x])[0].capitalize()))

# Make SNES lists
snes_1 = list(chain.from_iterable([[os.path.basename(x) for x in glob.glob(outdir + rarchgamesin + romdir + y)] for y in presnes]))
snes_2 = ["\n<h2>Super Nintendo</h2>", alist % (outdir + rarchgamesin + "?core=snes9x", "Upload ROM")]

# Generate HTML code for SNES list
for x in range(0, len(snes_1)):
	snes_2.append(alist % (outdir + rarchgamesin + "?core=snes9x&rom=" + snes_1[x], os.path.splitext(snes_1[x])[0].capitalize()))

# Make flash lists
# Just a premade list for now
flash_1 = ['1on1soccer.swf', '3dtanks.swf', 'abobosbigadventure.swf', 'achievementunlocked.swf', 'achievementunlocked2.swf', 'achievementunlocked3.swf', 'actionturnip.swf', 'adaran.swf', 'adrenaline.swf', 'americanracing1.swf', 'americanracing2.swf', 'arkandianrevenant.swf', 'awesomecars.swf', 'awesomeplanes.swf', 'bloonsplayerpack2.swf', 'bloonsplayerpack3.swf', 'bloonsplayerpack4.swf', 'bloonsplayerpack5.swf', 'bloonstd1.swf', 'bloonstd3.swf', 'bloonstd4.swf', 'bloonstd5.swf', 'bobtherobber.swf', 'boombot2.swf', 'boxhead2play.swf', 'bubbletanks2.swf', 'bulletbill.swf', 'cactusmccoy.swf', 'cactusmccoy2.swf', 'cargobridge.swf', 'causality.swf', 'computerbashing.swf', 'crushthecastle.swf', 'cubefield.swf', 'cyclomaniacs2.swf', 'diggy.swf', 'donkeykong.swf', 'dontshootthepuppy.swf', 'doodledefender.swf', 'doom.swf', 'ducklife.swf', 'ducklife2.swf', 'ducklife3.swf', 'ducklife4.swf', 'earntodiesuperwheel.swf', 'electricman2.swf', 'elephantquest.swf', 'epicbattlefantasy3.swf', 'epiccomboredux.swf', 'exitpath.swf', 'factoryballs.swf', 'factoryballs2.swf', 'factoryballs3.swf', 'factoryballs4.swf', 'flashflightsimulator.swf', 'flight.swf', 'happywheels.swf', 'hobo.swf', 'hobo2.swf', 'hobo3.swf', 'hobo4.swf', 'hobo5.swf', 'hobo6.swf', 'hobo7.swf', 'houseofwolves.swf', 'interactivebuddy.swf', 'jacksmith.swf', 'jellytruck.swf', 'johnnyupgrade.swf', 'jumpix2.swf', 'learn2fly.swf', 'magnetface.swf', 'marioracingtournament.swf', 'megamanprojectx.swf', 'metroidelements.swf', 'mineblocks.swf', 'minesweeper.swf', 'mirrorsedge.swf', 'motherload.swf', 'multitask.swf', 'mutilateadoll2.swf', 'myangel.swf', 'nanotube.swf', 'ngame.swf', 'nucleus.swf', 'nyancatlostinspace.swf', 'onemanarmy2.swf', 'pacman.swf', 'pandemic.swf', 'pandemic2.swf', 'papalouie.swf', 'papalouie2.swf', 'papalouie3.swf', 'portal.swf', 'portal2d.swf', 'qwop.swf', 'raftwars.swf', 'raftwars2.swf', 'raze.swf', 'redshift.swf', 'revenant2.swf', 'run2.swf', 'run3.swf', 'saszombieassault3.swf', 'shoppingcarthero3.swf', 'siftheads.swf', 'siftheads2.swf', 'siftheads3.swf', 'siftheads4.swf', 'siftheads5.swf', 'sniperassassin4.swf', 'sportsheadsfootball.swf', 'stickrpg.swf', 'stickrun2.swf', 'stickwar.swf', 'strikeforceheroes2.swf', 'strikeforcekittylaststand.swf', 'sugarsugar.swf', 'sugarsugar2.swf', 'sugarsugar3.swf', 'superd.swf', 'superfighters.swf', 'supermario63.swf', 'supermarioflash.swf', 'swordsandsandals2.swf', 'tacticalassassin.swf', 'tanks.swf', 'tanktrouble.swf', 'tetris.swf', 'thebindingofisaac.swf', 'theimpossiblequiz2.swf', 'theworldshardestgame2.swf', 'thingthingarena.swf', 'tosstheturtle.swf', 'ultimateflashsonic.swf']
flash_2 = ["\n<h2>Flash Games</h2>", alist % (outdir + flashgamesin, "Upload SWF")]

# Generate HTML code for flash list
for x in range(0, len(flash_1)):
	flash_2.append(alist % (outdir + flashgamesin + "?swf=" + flash_1[x], os.path.splitext(flash_1[x])[0].capitalize()))



# Write to list file
def st(x):
	return "\n".join(x)

final_list = index % (st(html5_2) + st(gba_2) + st(gen_2) + st(n64_2) + st(nes_2) + st(snes_2) + st(flash_2))

with open(outindex, "w") as file:
	file.write(final_list)

for x in final_list.splitlines():
	print(x)

print("\nDone!")
