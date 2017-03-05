from distutils.core import setup

VERSION = '0.1.2'

setup(
    name='githubclient',
    packages=['githubclient'],
    version=VERSION,
    description='A Python github client.',
    author='Taylor J. Meek, CloudBolt Software',
    author_email='taylor+pypi@cloudbolt.io',
    url='https://github.com/CloudBoltSoftware/githubclient',
    download_url='https://github.com/CloudBoltSoftware/githubclient/tarball/{version}'.format(version=VERSION),
    keywords=['github', 'api', 'rest', 'client'],
    license='MIT',
    long_description=open('README').read(),
    classifiers=[],
    py_modules=['githubclient'],
)
