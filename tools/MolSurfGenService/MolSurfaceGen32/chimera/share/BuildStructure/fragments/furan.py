from BuildStructure.Fragment import Fragment, RING5
frag = Fragment("furan", [
	("C", (0.626944, -3.02095, -1.49527)),
	("H", (1.28794, -2.16592, -1.49527)),
	("C", (-0.78902, -3.02095, -1.49527)),
	("H", (-1.45014, -2.16604, -1.49508)),
	("C", (-1.17148, -4.34228, -1.49537)),
	("H", (-2.12758, -4.84693, -1.49539)),
	("O", (-0.0809714, -5.15183, -1.49559)),
	("C", (1.00954, -4.34214, -1.49551)),
	("H", (1.9656, -4.8467, -1.4956)),
	], [
	((0,1), None),
	((0,2), None),
	((2,3), None),
	((4,2), (-0.0809974, -3.97563, -1.4954)),
	((4,5), None),
	((6,4), None),
	((7,6), None),
	((7,8), None),
	((0,7), (-0.0809974, -3.97563, -1.4954)),
	])

fragInfo = [RING5, frag]
