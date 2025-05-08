from setuptools import find_packages, setup

# NOME DO PACOTE
package_name = ''

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yago',
    maintainer_email='yago@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # EXECUTAVEIS
            # 'nome_executavel = pasta.arquivo:main',
    
        ],
    },
)
