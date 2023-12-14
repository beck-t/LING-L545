all: lat.gen.hfst

lat.lexc.hfst: lat.lexc
	hfst-lexc lat.lexc -o lat.lexc.hfst
lat.twol.hfst: lat.twol
	hfst-twolc lat.twol -o lat.twol.hfst
lat.gen.hfst: lat.lexc.hfst lat.twol.hfst
	hfst-compose-intersect -1 lat.lexc.hfst -2 lat.twol.hfst -o lat.gen.hfst

clean:
	rm -f *.hfst