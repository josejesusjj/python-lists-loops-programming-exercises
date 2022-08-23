parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:
def get_parking_lot(item):
  not_parking_slots = 0
  available_slots = 0
  occupied_slots = 0

  for x in item:
    for y in x:
      if y == 1:
        occupied_slots +=1
      elif y == 2:
        available_slots +=1
      elif y == 0:
        not_parking_slots +=1
  total_slots = not_parking_slots + available_slots + occupied_slots
  state  = {'total_slots':total_slots, 'available_slots':available_slots, 'occupied_slots':occupied_slots}
  return state 

parking = get_parking_lot(parking_state)
print(parking)
  

