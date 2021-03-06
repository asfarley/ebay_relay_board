from pylibftdi import BitBangDevice
import time
counter=0
 
class UsbRelay:
 
    def SetRelayPattern(self, r1_on, r2_on, r3_on, r4_on, r5_on, r6_on, r7_on, r8_on):
        with BitBangDevice('A904TADX') as bb:
            bb.port = r1_on + (r2_on << 1) + (r3_on << 2) + (r4_on << 3) + (r5_on << 4) + (r6_on << 5) + (r7_on << 6) + (r8_on << 7)
 
import atexit #Turn off motor before exit
def CloseS():
    ur.SetRelayPattern(0,0,0,0,0,0,0,0)
    print("Process terminated")
    print'Total reps: ', counter
    exit()
 
def SingleActuation():
    global counter
    ur.SetRelayPattern(1,1,0,0,0,0,0,0)
    time.sleep(6)
    ur.SetRelayPattern(0,0,0,0,0,0,0,0)
    counter+=1
    print("Rep=", counter)
    time.sleep(10)
    ur.SetRelayPattern(0,0,1,1,0,0,0,0)
    time.sleep(4)
    ur.SetRelayPattern(0,0,0,0,0,0,0,0)
    counter+=1
    print("Rep=", counter)
    time.sleep(10)
 
def ResetActuation():
    ur.SetRelayPattern(0,0,1,1,0,0,0,0)
    time.sleep(2)
    ur.SetRelayPattern(0,0,0,0,0,0,0,0)
    print("Reset position")
    time.sleep(120)
   
 
atexit.register(CloseS)
 
if __name__ == '__main__':
    ur = UsbRelay()
    while(True):
	if counter==0:
		SingleActuation()
	if not counter%10 == 0:
		SingleActuation()
        if counter%10 == 0:
		ResetActuation()
		SingleActuation()

