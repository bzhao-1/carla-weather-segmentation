import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='mit_semseg',
    version='0.1.0',
    author='CV4AD team; based on MIT CSAIL',
    description='CARLA weather-robustness experiments based on MIT semantic-segmentation-pytorch',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bzhao-1/carla-weather-segmentation',
    packages=setuptools.find_packages(),
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
    ),
    install_requires=[
        'numpy',
        'torch>=2.0',
        'torchvision',
        'opencv-python',
        'yacs',
        'scipy',
        'tqdm',
        'Pillow>=9.0',
        'PyYAML>=6.0'
    ]
)
