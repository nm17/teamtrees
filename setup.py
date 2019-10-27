from setuptools import setup

setup(
    name="teamtrees",
    version="0.1.0",
    packages=["teamtrees"],
    url="https://github.com/nm17/teamtrees",
    license="MIT",
    author="NeverMine17",
    author_email="dannevergame@gmail.com",
    description="Get data from official TeamTrees website",
    install_requires=["requests", "beautifulsoup4"],
    python_requires=">=3.5",
    long_description_content_type="text/markdown",
    long_description=open("README.md").read(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
