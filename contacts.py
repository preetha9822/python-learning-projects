
contacts={}
while True:
    print("\n1.Add 2.Search 3.Delete 4.Show all 5.Exit")
    choice=input("Choose :")
    if choice=="1":
       name=input("Name:")
       phone=input("Phone:")
       if name in contacts:
          print(name,"already exists")
          continue
       contacts[name]=phone
       print(name,"added")
    elif choice=="2":
       name=input("Search name:")
       if name in contacts:
          print(name,":",contacts[name])
       else:
          print("Not found")
    elif choice=="3":
        name=input("Delete name:")      
        if name in contacts:
           del contacts[name]
           print(name,"deleted")
        else:
           print("Not found")
    elif choice=="4":
      if len(contacts)==0:
         print("No contacts yet")
      else:   
         for name,phone in contacts.items():
            print(name,":",phone)
    elif choice =="5":
       print("Bye")
       break
    else:
       print("Invalid choice")

      
