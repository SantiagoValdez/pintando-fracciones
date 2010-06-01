#!/usr/bin/env python
try:
	from sugar.activity import bundlebuilder
	bundlebuilder.start()
except ImportError:
	import os
	os.system("find ./ | sed 's,^./,PaintingFractionsActivity.activity/,g' > MANIFEST")
	os.system('rm PaintingFractionsActivity.xo')
	os.chdir('..')
	os.system('zip -r PaintingFractionsActivity.xo PaintingFractionsActivity.activity')
	os.system('mv PaintingFractionsActivity.xo ./PaintingFractionsActivity.activity')
	os.chdir('PaintingFractionsActivity.activity')
