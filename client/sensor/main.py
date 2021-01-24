import time
import RPi.GPIO as GPIO

INTAVAL = 2
IS_HORLD = False
HORLD_TIME = 1.5
SLEEPTIME = 0.5
SENSOR_PIN = 18

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

st = time.time()
ht = time.time()

def main(self):
    while True:
		print(GPIO.input(SENSOR_PIN))
		if(GPIO.input(SENSOR_PIN) == GPIO.HIGH):
			if (IS_HORLD):
				if((st + HORLD_TIME) < time.time()):
					IS_HORLD = False
					print("人を検知しました")
					time.sleep(INTAVAL)
			else:
				IS_HORLD = True
				st = time.time()
		else:
			IS_HORLD = False
		time.sleep(SLEEPTIME)


if __name__ == '__main__'
	main()