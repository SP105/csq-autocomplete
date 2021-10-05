from setuptools import setup, find_namespace_packages
from csq.custom_exceptions import ReadException


def read_file(file: str) -> str:
    try:
        with open(file, 'r') as f:
            return f.read()
    except Exception as e:
        raise ReadException(f'There was a problem trying to read: {file}', e)


setup(name='csq-autocomplete',
      version='1.0',
      description='Data Engineer test for Contestsquare. Autocomplete functionality',
      long_description=read_file('READ.md'),
      project_urls={
          'Source': 'https://github.com/SP105/csq-autocomplete',
      },
      author='Santiago Panizza',
      author_email='panizzasantiago@gmail.com',
      packages=find_namespace_packages(include=['csq.*'], exclude=['test*']),
      package_data={'': ['resources/*',
                         'resources/*/*']},
      include_package_data=True,
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          'Intended Audience :: Developers',
      ],
      install_requires=read_file('requirements.txt'),
      tests_require=read_file('requirements_test.txt'),
      )
