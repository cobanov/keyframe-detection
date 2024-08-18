from setuptools import setup, find_packages

setup(
    name="keyframe_detection",
    version="0.1.0",
    author="Mert Cobanov",
    author_email="mertcobanov@gmail.com",
    description="A Python package for keyframe detection using various algorithms.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cobanov/keyframe-detection",
    packages=find_packages(),
    install_requires=[
        "opencv-python",
        "numpy",
        "scikit-image",
        "tqdm",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
