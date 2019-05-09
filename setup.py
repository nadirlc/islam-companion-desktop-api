import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ic-desktop-api",
    version="1.0.0.post1",
    author="Nadir Latif",
    author_email="nadir@pakjiddat.pk",
    description="Desktop API for accessing Holy Quran and Hadith data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nadirlc/islam-companion-desktop-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
