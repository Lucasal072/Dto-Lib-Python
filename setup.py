from setuptools import setup


with open('README.md','r') as file:
    readme = file.read()

setup(name='DtoLib',
      license='MIT License',
      long_description=readme,
      long_description_content_type='text/markdown',
      version='0.0.1',
      keywords='Dto',
      description='Python Dto Library',
      author='Lucas Alves',
      author_email='lucasal072@gmail.com',
      packages=['DtoLib'],
     )