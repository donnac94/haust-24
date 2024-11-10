class StoredNumber:
    def __init__(self, the_number):
        self.__the_number = the_number

    def set_number(self, num):
        self.__the_number = num

    def get_number(self):
        return self.__the_number

    def __str__(self):
        return f"the_number: {self.__the_number}"

if __name__ == "__main__":
    st_num = StoredNumber(5.0)
    print(st_num)
    st_num2 = StoredNumber(1)
    print(st_num2)
    st_num2.set_number(3.4)
    print(st_num2)
    print(st_num2.get_number())
