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
	print("Total reps: ", counter)
	exit()

atexit.register(CloseS)

if __name__ == '__main__':
	ur = UsbRelay()
	ur.SetRelayPattern(1,1,0,0,0,0,0,0)
	time.sleep(1)
	ur.SetRelayPattern(0,0,0,0,0,0,0,0)
