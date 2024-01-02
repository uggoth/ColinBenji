module_name = 'main_test_paths.py'
print (module_name, 'starting')

from importlib.machinery import SourceFileLoader
gpio = SourceFileLoader('GPIO', '/home/pi/ColinPiClasses/GPIO_Pi_v46.py').load_module()
fred = gpio.GPIO('dummy','INFRA_RED',17)
