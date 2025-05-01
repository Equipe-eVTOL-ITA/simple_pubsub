from setuptools import setup

package_name = 'velocity_control'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Yago Ximenes',
    maintainer_email='yago@example.com',
    description='Minimal ROS 2 publisher/subscriber package with QoS and parameters',
    license='MIT',
    entry_points={
        'console_scripts': [
            'publisher_node = velocity_control.publisher_node:main',
            'subscriber_node = velocity_control.subscriber_node:main',
        ],
    },
)
