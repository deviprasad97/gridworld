from setuptools import setup
from setuptools import find_packages


with open('README.md', 'r') as f:
    long_description = f.read()

setup(name='gridworld',
      version='0.2.0',
      author='Devi Prasad Tripathy',
      author_email='tripathy.devi7@gmail.com',
      description='gridworld generator.',
      long_description=long_description, 
      long_description_content_type='text/markdown',
      url='https://github.com/deviprasad97/gridworld',
      # Minimal requried dependencies (full dependencies in requirements.txt)
      install_requires=['gym', 
                        'numpy', 
                        'matplotlib', 
                        'scikit-image'],
      tests_require=['pytest'],
      python_requires='>=3',
      # List all packages (folder with __init__.py), useful to distribute a release
      packages=find_packages(), 
      # tell pip some metadata (e.g. Python version, OS etc.)
      classifiers=['Programming Language :: Python :: 3', 
                   'License :: OSI Approved :: MIT License', 
                   'Operating System :: OS Independent', 
                   'Natural Language :: English', 
                   'Topic :: Scientific/Engineering :: Artificial Intelligence']
)
