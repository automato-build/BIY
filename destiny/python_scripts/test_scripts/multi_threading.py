import threading
import time

def calc_square(number):
	while True:
		print('Square:' , number * number)
		time.sleep(2)

def calc_quad(number):
	while True:
		print('Quad:' , number * number * number * number)
		time.sleep(7)




if __name__ == "__main__":
    number = 7

    thread1 = threading.Thread(target=calc_square, args=(number,))
    # thread2 = threading.Thread(target=calc_quad, args=(number,))

    thread1.start()
    # thread2.start()

    # thread1.join()
    # thread2.join()

    calc_quad(number)
    