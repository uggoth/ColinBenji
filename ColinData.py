module_name = 'ColinData.py'

class ColinData():
    def __init__(self):
        self.pi_name = 'BENJI'
        #  To obtain the port name use:    ls /dev/serial/by-id
        self.ax12_path = '/dev/serial/by-id/usb-FTDI_USB__-__Serial_Converter_FT4TCJWH-if00-port0'
        self.ax12_speed = 1000000
        self.ax12_list = [20,21]
        self.params =  {'PI_NAME':self.pi_name,
                        'AX12_PATH':self.ax12_path,
                        'AX12_SPEED':self.ax12_speed,
                        'AX12_LIST':self.ax12_list}

if __name__ == "__main__":
    print (module_name, 'starting')
    my_data = ColinData()
    import pprint
    pp = pprint.PrettyPrinter()
    pp.pprint(my_data.params)
    print (module_name, 'finished')
