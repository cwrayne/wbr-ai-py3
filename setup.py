from setuptools import setup, find_packages

setup(
    name='wbr-ai',
    version='0.1.0',
    description='AI-powered solver for What Beats Rock game.',
    author='Dashiell Benton',
    author_email='dash@dashbenton.com',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'wbr-ai = wbr_ai.game:play_game',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Creative Commons Attribution 4.0 International License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)