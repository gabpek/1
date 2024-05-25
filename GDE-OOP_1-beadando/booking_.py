#####################################################################################
###                                   LIBRARIES                                   ###

from collections import defaultdict
from datetime import date

#####################################################################################
###                                   VARIABLES                                   ###


# Fantasy names for the rooms:
roomNames = ['Acapulco','Berlin','Canberra','Dublin','Eljascv']
# Sum of the double rooms:
sumDoubles = 2
# Sum of the single rooms:
sumSingles = 3
# Simple counter for the sumRooms() function
i = 1
j = 0
#####################################################################################
###                                   CLASSES                                     ###


class Hotel:
  brand = 'The Resort'
  rating = 4
  rooms = []

  def __iter__(self):
    return iter(self.rooms)

  def add(self, room):
    self.rooms.append(room)

class Room(Hotel):
  def __init__(self, name, number, price) -> None:
    #self.id = id
    self.name = name
    self.number = number
    self.price = price
    self.reserved = 'false'

  def isOccupied(self):
    if(self.reserved == 'false'):
      print('Sorry, ' + self.name + ' room is reserved')

class Single(Room):
  price = 130

class Double(Room):
  price = 180

class Reservation:
  def __init__(self) -> None:
    self.container = []
    self.reservations_by_date = defaultdict(list) #teszt
  def add_reservation(self, reservation_date, reservation_details):
    self.container.append({
      'date': reservation_date,
      'type': reservation_details
    })
    self.reservations_by_date[reservation_date].append(reservation_details)
  def remove_reservation(self, reservation_date):
    for i in range(len(self.container)):
      print('wow')
      if(self.container[i]['date']== reservation_date):
        print('hopp')
        del self.container[i]
        break
  def get_reservation(self, reservation_date):
    return self.reservations_by_date.get(reservation_date, [])
  def list_reservation(self) -> None:
    #print(self.reservations_by_date.items())
    for reservation in self.container:
      getDate = reservation.get('date')
      getType = reservation.get('type')

      print('dátum: ', reservation.get('date'), '---> szoba:', reservation.get('type'))

#####################################################################################
###                                   FUNCTIONS                                   ###

def sumRooms():
  return sumDoubles + sumSingles

#####################################################################################
###                                   LOGIC                                       ###

if __name__ == '__main__':

  r = Reservation()
  h = Hotel()

  print('Rendelkezésre álló szobák száma: ', sumRooms())

  # Filling up the Hotel.rooms list:
  while i < sumRooms() + 1:
    if(i <= sumDoubles):
      #rooms.append(Double(roomNames[i], i, Double.price))
      h.add(Double(roomNames[i-1], i, Double.price))
    else:
      h.add(Single(roomNames[i-1], i, Single.price))
    i += 1

  #Filling up the Reservations list:
  r.add_reservation(date(2024, 6, 20), 2)

  while True:
    chooseMethod = input('1.) Reservation\n2.) Cancelling \n3.) Listing \nPlease choose: ' )

    if(chooseMethod == '1'):
      try:
        getYear = input('Kérem adja meg a foglalás dátumát (év): ')
        getMonth = input('Kérem adja meg a foglalás dátumát (hónap): ')
        getDay = input('Kérem adja meg a foglalás dátumát (nap): ')

        userDate = date(int(getYear), int(getMonth), int(getDay))

        if(date.today() < userDate):
          getRes = r.get_reservation(userDate)

          if(len(getRes) == 0):
            print('Elérhető')
            chooseRoom = input('1.) Egyágyas\n2.) Kétágyas\nPlease choose: ' )

            r.add_reservation(userDate, chooseRoom)
          else:
            print('Sajnos erre a dátumra már történt foglalás.')
        else:
          print('A dátum a múltban van, vissza a jövőbe?')


      except:
        print(ValueError('Valami gebasz van a d...'))
      # Implementálj egy metódust, ami lehetővé teszi szobák foglalását dátum alapján, visszaadja annak árát. 
      #print('You choosed Reservation')
      #r.add('Room 102')
      #print(r.reservations)
    elif(chooseMethod == '2'):
      print('You choosed Cancelling')
      getYear = input('Kérem adja meg a foglalás dátumát (év): ')
      getMonth = input('Kérem adja meg a foglalás dátumát (hónap): ')
      getDay = input('Kérem adja meg a foglalás dátumát (nap): ')

      userDate = date(int(getYear), int(getMonth), int(getDay))

      r.remove_reservation(userDate)
    elif(chooseMethod == '3'):
      print('You choosed Listing')
      r.list_reservation()

    else:
      print('Please choose one of the following:')
      while True:
          answer = str(input('Run again? (y/n): '))
          if answer in ('y', 'n'):
              break
          print("invalid input.")
      if answer == 'y':
          continue
      else:
          print("Goodbye")
          break

  #####################################################################################
  ###                                   CHECKING                                    ###

