from distutils.core import setup

VERSION = '0.1.1'

setup(
    name='githubclient',
    packages=['githubclient'],
    version='0.1.1',
    description='A Python github client.',
    author='Taylor J. Meek, CloudBolt Software',
    author_email='taylor+pypi@cloudbolt.io',
    url='https://github.com/CloudBoltSoftware/githubclient',
    download_url='https://github.com/CloudBoltSoftware/githubclient/tarball/0.1.1',
    keywords=['github', 'api', 'rest', 'client'],
    license='MIT',
    long_description=open('README').read(),
    classifiers=[],
    py_modules=['githubclient'],
)
