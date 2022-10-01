import serial


def get_ph_value():
    Sum = 0
    i = 0
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    while True:
        while(i <5):
            if ser.in_waiting > 0:
                try:
                    line = ser.readline().decode('utf-8').rstrip()
                    print(line)
                    Sum += float(line)
                    i+=1
                except:
                    break
        try:
            Sum = Sum/i
        except ZeroDivisionError:
            Sum = Sum
        break
    return round(Sum,2)


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            
            print(float(line))
    #print(get_ph_value())
    