from setuptools import setup

setup(
   name = 'snapshotalyzer-30000',
   version = '0.1',
   author = 'RN',
   author_email='abc@123.com',
   summary="snapshotalyzer is a tool to manage AWS EC2 snapshots",
   license="GPLb3+",
   packages=['shotty'],
   url = "https://github.com/rpdevops/snapshotalyzer-30000.git",
   install_requires=['click','boto3'],
   entry_points='''
       [console_scripts]
       shotty=shotty.shotty:cli
       '''


)
