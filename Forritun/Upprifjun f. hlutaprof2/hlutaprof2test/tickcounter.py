# CLASS DEFINITION FOR TickCounter HERE
class TickCounter:
  def __init__(self):
    self.count = 0
  
  def tick(self):
    self.count += 1
  
  def get_count(self):
    return self.count
  
  def reset(self):
    self.count = 0


if __name__ == "__main__":
    counter = TickCounter()
    for _ in range(45):
        counter.tick()
    print("The current count: ", counter.get_count())
    for _ in range(12):
        counter.tick()
    print("The current count: ", counter.get_count())
    counter.reset()
    for _ in range(31):
        counter.tick()
    print("The current count: ", counter.get_count())