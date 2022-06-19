from setuptools import setup, find_namespace_packages

setup(
    name='clean up',
    version='1.0.0.',
    description='Sorting files',
    url='https://github.com/qsopol/goit-python.git,
    author='qsopol',
    author_email='alkaalisi@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
)
