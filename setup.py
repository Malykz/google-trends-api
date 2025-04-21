from setuptools import setup, find_packages

setup(
    name='googletrends',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'user_agent'
    ],
    author='P.Didy Damar',
    author_email='vididamar45@gmail.kom',
    description='Shoot the trends.google.com API, and serve that response as a python objects',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Malykz/google-trends-api',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
