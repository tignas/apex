from setuptools import setup, find_packages

version = '0.9.0'

install_requires=[
  "cryptacular",
  "velruse",
  "pyramid>1.1.2",
  "pyramid_mailer",
  "wtforms",
  "wtforms-recaptcha",
]

tests_require = install_requires + ['Sphinx', 'docutils', 
                                    'WebTest', 'virtualenv', 'nose']

setup(
    version = version,
    name='Apex',
    long_description='Pyramid starter project to add Velruse, Flash Messages, CSRF, ReCaptcha and Sessions',
    install_requires=install_requires,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    tests_require=tests_require,
    test_suite="apex.tests",
)
