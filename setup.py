from setuptools import setup

package_name = 'robot_spawner_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='msjun-ubuntu',
    maintainer_email='msjun23@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'spawn_turtlebot = robot_spawner_pkg.spawn_turtlebot:main',
        ],
    },
)
