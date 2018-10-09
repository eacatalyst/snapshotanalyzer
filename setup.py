from setuptools import setup

setup (

     name = 'SnapshotAnalyzer'
    ,version = '0.1'
    ,author = 'Lampard'
    ,author_email='claysonwillis@gmail.com'
    ,description = 'Snapshot Analyzer is a tool to manage AWS EC2 snapshots'
    ,licence = 'GPLv3+'
    ,packages=['shotty']
    ,url="https://github.com/eacatalyst/snapshotanalyzer"
    ,install_requires = [
         'click'
        ,'boto3'
    ]
    ,entry_points = '''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
