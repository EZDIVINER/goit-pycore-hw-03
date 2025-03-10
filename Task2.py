import random
def get_numbers_ticket(min, max, quantity):

    # Перевірка коректності введення значень 
    if not (1 <= min <= max <= 1000) or not (min <= quantity <= max):
        return []

    empty_set = set()
    
    while len(empty_set) < quantity:
        target = random.randint(min, max)
        empty_set.add(target)
        
    
    return (sorted(empty_set))

print(get_numbers_ticket(1,49,6))
print(get_numbers_ticket(1,49,6))
print(get_numbers_ticket(1,49,6))
print(get_numbers_ticket(1,49,6))
print(get_numbers_ticket(1,49,6))
print(get_numbers_ticket(1,49,6))

print(get_numbers_ticket(1,1001,6))
print(get_numbers_ticket(1,49,53))                
