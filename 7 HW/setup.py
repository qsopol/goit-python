from setuptools import setup, find_packages

setup(
    name='clean_your_folder',
    version='0.0.1',
    description='Start the program and waiting a wonder',
    url='https://github.com/qsopol/goit-python.git',
    author='qsopol',
    author_email='alkaalisi@gmail.com',
    license='MIT',
    packages=find_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
)
