from storednumbers import StoredNumber

class ManyStoredNumbers:
    def __init__(self):
        self.number_list = []

    def add_stored_number(self, st_num):
        self.number_list.append(st_num)

    def __str__(self):
        ret_val = "These are the numbers:\n"
        for number in self.number_list:
            ret_val += str(number) + "\n"
        return ret_val


if __name__ == "__main__":
    many_stored = ManyStoredNumbers()
    many_stored.add_stored_number(StoredNumber(4.6))
    many_stored.add_stored_number(StoredNumber(-3))
    print(many_stored)
    many_stored.add_stored_number(StoredNumber(9.0))
    print(many_stored)
