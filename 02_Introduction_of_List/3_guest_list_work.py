#邀请好友参加聚会
guest = ['Tom' ,'Bile' ,'Jack' ,'Lucy' ,'Lily' ,'Steven' ,'James']
print("I will invite some friends to my party!\n")
print(guest)
message = "Dear " + guest[0].title() + ", I invite you to my party."
print(message)
message = "Dear " + guest[1].title() + ",I invite you to my party."
print(message)
message = "Dear " + guest[2].title() + ",I invite you to my party."
print(message)
message = "Dear " + guest[3].title() + ",I invite you to my party."
print(message)
message = "Dear " + guest[4].title() + ",I invite you to my party."
print(message)
message = "Dear " + guest[5].title() + ",I invite you to my party."
print(message)
message = "Dear " + guest[6].title() + ",I invite you to my party."
print(message)
print("目前一共邀请" + str(len(guest)) + "位客人。")


#有一位好友因为有事不能即使参加聚会，重新编写邀请谏
print("\n\nI am sorry to hear that " + guest[2].title() + " have something so that " + guest[2].title() + " can't join the party.\n")
guest[2] = 'Jojo'
print(guest)
message = "Dear " + guest[0].title() + ", I invite you to my party."
print(message)
message = "Dear " + guest[1].title() + ",I invite you to my party."
print(message)
message = "Dear " + guest[2].title() + ",I invite you to my party."
print(message)
message = "Dear " + guest[3].title() + ",I invite you to my party."
print(message)
message = "Dear " + guest[4].title() + ",I invite you to my party."
print(message)
message = "Dear " + guest[5].title() + ",I invite you to my party."
print(message)
message = "Dear " + guest[6].title() + ",I invite you to my party."
print(message)
print("目前一共邀请" + str(len(guest)) + "位客人。")

#因为增大聚会空间，增加人数
print("\n\nI will invite three friends again because I booked a bigger room.\n")
print(guest)
guest.insert(0, 'Mick')
guest.insert(3, 'Jane')
guest.append('Harden')
message = "Dear " + guest[0].title() + ", I invite you to my party."
print(message)
message = "Dear " + guest[1].title() + ",I invite you to my party."
print(message)
message = "Dear " + guest[2].title() + ",I invite you to my party."
print(message)
message = "Dear " + guest[3].title() + ",I invite you to my party."
print(message)
message = "Dear " + guest[4].title() + ",I invite you to my party."
print(message)
message = "Dear " + guest[5].title() + ",I invite you to my party."
print(message)
message = "Dear " + guest[6].title() + ",I invite you to my party."
print(message)
message = "Dear " + guest[7].title() + ",I invite you to my party."
print(message)
message = "Dear " + guest[8].title() + ",I invite you to my party."
print(message)
message = "Dear " + guest[9].title() + ",I invite you to my party."
print(message)
print("目前一共邀请" + str(len(guest)) + "位客人。")

#由于失误，大房间被别人提前预定，删除部分受邀请人
print("\n\nDue to mistakes, the big room was booked in advance, deleting part of the invitee.\n")
g1 = guest.pop(2)
g2 = guest.pop(2)
g3 = guest.pop(2)
g4 = guest.pop(2)
g5 = guest.pop(2)
g6 = guest.pop(2)
g7 = guest.pop(2)
g8 = guest.pop(2)
print(guest)
print("Dear " + g1 + ",Since my mistakes are sorry,I can't invite you to join my party.")
print("Dear " + g2 + ",Since my mistakes are sorry,I can't invite you to join my party.")
print("Dear " + g3 + ",Since my mistakes are sorry,I can't invite you to join my party.")
print("Dear " + g4 + ",Since my mistakes are sorry,I can't invite you to join my party.")
print("Dear " + g5 + ",Since my mistakes are sorry,I can't invite you to join my party.")
print("Dear " + g6 + ",Since my mistakes are sorry,I can't invite you to join my party.")
print("Dear " + g7 + ",Since my mistakes are sorry,I can't invite you to join my party.")
print("Dear " + g8 + ",Since my mistakes are sorry,I can't invite you to join my party.")
message = "Dear " + guest[0].title() + ", I invite you to my party."
print(message)
message = "Dear " + guest[1].title() + ",I invite you to my party."
print(message)
print("目前一共邀请" + str(len(guest)) + "位客人。")
#删除名单
del guest[0]
del guest[0]
print("\nfinal list:")
print(guest)
print("目前一共邀请" + str(len(guest)) + "位客人。")
