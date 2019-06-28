from os.path import dirname, join

from setuptools import setup

import pm4pybpmn


def read_file(filename):
    with open(join(dirname(__file__), filename)) as f:
        return f.read()


setup(
    name=pm4pybpmn.__name__,
    version=pm4pybpmn.__version__,
    description=pm4pybpmn.__doc__.strip(),
    long_description=read_file('README.md'),
    author=pm4pybpmn.__author__,
    author_email=pm4pybpmn.__author_email__,
    py_modules=[pm4pybpmn.__name__],
    include_package_data=True,
    packages=['pm4pybpmn', 'pm4pybpmn.objects', 'pm4pybpmn.objects.bpmn', 'pm4pybpmn.objects.bpmn.util',
              'pm4pybpmn.objects.bpmn.exporter', 'pm4pybpmn.objects.bpmn.importer', 'pm4pybpmn.objects.conversion',
              'pm4pybpmn.objects.conversion.bpmn_to_petri', 'pm4pybpmn.objects.conversion.bpmn_to_petri.versions',
              'pm4pybpmn.objects.conversion.petri_to_bpmn', 'pm4pybpmn.objects.conversion.petri_to_bpmn.util',
              'pm4pybpmn.objects.conversion.petri_to_bpmn.versions', 'pm4pybpmn.visualization',
              'pm4pybpmn.visualization.bpmn', 'pm4pybpmn.visualization.bpmn.util',
              'pm4pybpmn.visualization.bpmn.versions'],
    url='http://www.pm4py.org',
    license='GPL 3.0',
    install_requires=[
        'pm4py',
        'networkx>=2.2',
        'bpmn_python==0.0.18',
        'intervaltree',
        'lime',
        'joblib',
        'pydotplus'
    ],
    project_urls={
        'Documentation': 'http://pm4py.pads.rwth-aachen.de/documentation/',
        'Source': 'https://github.com/pm4py/pm4py-source',
        'Tracker': 'https://github.com/pm4py/pm4py-source/issues',
    }
)
