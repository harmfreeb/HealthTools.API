from setuptools import setup, find_packages

setup(
    name='healthtools',
    version='0.0.2',
    keywords='healthtools',
    author='Code for Africa',
    author_email='support@codeforafrica.org',
    url='https://github.com/CodeForAfricaLabs/HealthTools.API',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'test']),
    include_package_data=True,

    # Pull these from requirements.txt
    install_requires=[
        'flask',
        'requests',
        'bs4',
        'elasticsearch',
        'requests_aws4auth'
    ],
)
