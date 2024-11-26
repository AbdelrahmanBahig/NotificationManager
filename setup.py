from setuptools import setup, find_packages 

setup(
    name="NotificationManager",
    version="1.0",
    packages=find_packages(),
    install_requires=[],
    author="Abdelrahman Bahig",
    description="A simple notification manager package",
   # long_description=open("ReadME.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AbdelrahmanBahig/NotificationManager",
    python_requires='>=3.6',
)