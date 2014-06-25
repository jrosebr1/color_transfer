from distutils.core import setup

setup(
	name = 'color_transfer',
	packages = ['color_transfer'],
	version = '0.1',
	description = 'Implements color transfer between two images using the Lab color space, similar to the Reinhard et al. paper, "Color Transfer between Images"',
	author = 'Adrian Rosebrock',
	author_email = 'adrian@pyimagesearch.com',
	url = 'https://github.com/jrosebr1/color_transfer',
	download_url = 'https://github.com/jrosebr1/color_transfer/tarball/0.1',
	keywords = ['computer vision', 'image processing', 'color', 'rgb', 'lab'],
	classifiers = [],
)