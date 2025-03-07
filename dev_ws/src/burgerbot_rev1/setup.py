from setuptools import find_packages, setup

package_name = 'burgerbot_rev1'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/' + package_name, ['package.xml', 'resource/' + package_name]),
        ('share/' + package_name + '/launch', ['launch/display.launch.py']),
        ('share/' + package_name + '/launch', ['launch/rsp.launch.py']),
        ('share/' + package_name + '/urdf', [
            'urdf/robot_core.xacro',
            'urdf/robot_dimensions.xacro',
            'urdf/color.xacro'
        ]),
    ],
    install_requires=['setuptools', 'pyserial'],
    zip_safe=True,
    maintainer='sufruuu',
    maintainer_email='192777954+sufruuu@users.noreply.github.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
		'motor_controller_node = burgerbot_rev1.motor_controller_node:main'
        ],
    },
)
