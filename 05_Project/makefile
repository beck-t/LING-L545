all: frc.inv.hfst

frc.adj.hfst: adjectives.lexc
	hfst-lexc adjectives.lexc -o frc.adj.hfst
frc.verb.hfst: verbs.lexc
	hfst-lexc verbs.lexc -o frc.verb.hfst
frc.misc.hfst: misc.lexc
	hfst-lexc misc.lexc -o frc.misc.hfst	
frc.lexc.hfst: frc.adj.hfst frc.verb.hfst frc.misc.hfst
	hfst-disjunct frc.adj.hfst frc.verb.hfst -o frc.pt1.hfst
	hfst-disjunct frc.pt1.hfst frc.misc.hfst -o frc.lexc.hfst
frc.twol.hfst: frc.twol
	hfst-twolc frc.twol -o frc.twol.hfst
frc.gen.hfst: frc.lexc.hfst frc.twol.hfst
	hfst-compose-intersect -1 frc.lexc.hfst -2 frc.twol.hfst -o frc.gen.hfst
frc.inv.hfst: frc.gen.hfst
	hfst-invert frc.gen.hfst -o frc.inv.hfst
	
clean:
	rm -f *.hfst