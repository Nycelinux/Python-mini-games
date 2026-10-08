def bubble_sort(a): 
    n=len(a)
    for p in range(n-1):
        swapped= False 
        for i in range(n-1-p):
            if a[i]> a[i+1]:
                a[i], a[i+1]=a[i+1], a[i]
                swapped=True
        if not swapped:
            break
    return a

user_input= input("Gib deine Zahlen durch Leerzeichen getrennt ein: ")
user_numbers=[int(zahl) for zahl in user_input.split()]
print(f"\n Deine originale Liste: {user_numbers}")
sorted_list= bubble_sort(user_numbers)
print(f"Sortierte Liste: {sorted_list}")