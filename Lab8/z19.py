class Manager:
    def put_driver_to_trip(self,driver,trip,car):
        driver.trip=trip
        driver.car=car
        print('Водитель',driver.name,'отправился в рейс',trip.name,'на машине',car.name)
    def unput_driver_from_trip(self,driver):
        print('Водитель',driver.name,'снят с рейса',driver.trip.name)
        driver.car=Car('','')
        driver.trip=Trip('')

class Trip:
    name=''
    done=False
    def __init__(self, name):
        self.name=name
        self.done=False

class Car:
    name=''
    state=''
    def __init__(self,name,state):
        self.name=name
        self.state=state

class Driver:
    name=''
    car=Car('','')
    trip=Trip('')
    def __init__(self,name):
        self.name=name
        self.car = Car('','')
        self.trip = Trip('')
    def make_fix_request(self):
        print('Водитель',self.name,': Мое авто',self.car.name,'нуждается в ремонте!')
    def make_report(self):
        self.trip.done=True
        print('Водитель',self.name,'рейс',self.trip.name,'завершил, состояние машины',self.car.state)
        if self.car.state=='плохое':
            self.make_fix_request()
        self.trip=Trip('')
        self.car=Car('','')

Max=Driver('Макс')
fordtr=Car('Ford Transit','хорошее')
kiev=Trip('Киев')
Alex=Driver('Алекс')
sprinter=Car('Mercedes-Benz Sprinter','плохое')
lviv=Trip('Львов')
manager=Manager()
manager.put_driver_to_trip(Max,kiev,fordtr)
manager.put_driver_to_trip(Alex,lviv,sprinter)
Alex.make_report()
manager.unput_driver_from_trip(Max)
