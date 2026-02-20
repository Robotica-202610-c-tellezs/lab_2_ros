from setuptools import find_packages, setup

package_name = 'lab_2_ros'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='estudiante',
    maintainer_email='estudiante@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
    'console_scripts': [
        'actividad2_node = lab_2_ros.actividad2_random_cmdvel:main',
        'actividad3_lidar = lab_2_ros.actividad3_lidar:main',
    ],
},
)
