from setuptools import setup, find_packages

setup(
    name='pregress',
    version='0.9.0',
    packages=find_packages(),
    install_requires=[
        'matplotlib', 'pandas', 'numpy', 'statsmodels', 'seaborn'
    ],
    entry_points={
        'console_scripts': [
            # Define any command-line scripts here, if applicable
        ],
    },
    author="Daniel McGibney",
    author_email="dmcgibney@bus.miami.edu",
    description="Python Regression Analysis.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/danmcgib/pregress",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
