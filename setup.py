from setuptools import setup
from pathlib import Path

currentFolder = str(Path(__file__).parent.absolute())
currentFolder = currentFolder.replace(' ', '%20')

setup(  name='catvsdog_ML',
        version='0.1',
        description='Crack Assir test with Tensorflow and Keras',
        url='---',
        author='JESUS',
        author_email='jesuga174@gmail.com',
        license='Proprietary',
        install_requires=['tensorflow==2.10.0', 'keras==2.10.0', 'numpy==1.24.3', 'notebook==7.0.4', 'Pillow==9.5.0',
                          'scipy==1.10.1', 'matplotlib'],
        zip_safe=False)