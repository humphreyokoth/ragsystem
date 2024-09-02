from setuptools import setup, find_packages

setup(
    name='ragsystem',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'elasticsearch',
        'requests',
        'transformers',
        'scikit-learn',
        'python-dotenv',
    ],
)