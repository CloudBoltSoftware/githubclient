from distutils.core import setup
setup(
    name='githubclient',
    packages=['githubclient'],
    version='0.1',
    description='A Python github client.',
    author='CloudBolt Software',
    author_email='taylor@cloudbolt.io',
    url='https://github.com/CloudBoltSoftware/githubclient',
    download_url='https://github.com/CloudBoltSoftware/githubclient/tarball/0.1',
    keywords=['github', 'api', 'rest', 'client'],
    license='MIT',
    long_description=open('README.md').read(),
    classifiers=[],
    py_modules=['githubclient'],
)
