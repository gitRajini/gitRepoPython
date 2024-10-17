try:
    with open('tessxt.txt') as read:
        read.read()

except Exception as e:
    print("Something went wrong!", e)

finally:
    print("Finally successfully done!")




