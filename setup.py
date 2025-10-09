from setuptools import setup, find_packages

setup(
    name="lerobot_motor_starai",
    version="0.0.1",
    description="LeRobot motor integration",
    author="Welt-liu",
    author_email="1994524450@qq.com",
    packages=find_packages(),
    install_requires=[
        "lerobot",
        "fashionstar-uart-sdk>=1.3.6"
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
)
