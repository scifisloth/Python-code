from threading import Thread
import time

database_value = 0


def increase():
    global database_value
    local_copy = database_value
    local_copy += 1
    time.sleep(0.1)
    database_value = local_copy


if __name__ == "__main__":

    print("Start value", database_value)
# This raises a race condition as multiple threads are
# trying to modify the same variable at the same time
    thread1 = Thread(target=increase)
    thread2 = Thread(target=increase)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("End value", database_value)

    print("End Main")
