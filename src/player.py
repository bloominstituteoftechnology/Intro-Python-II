# Write a class to hold player information, e.g. what room they are in
# currently.



class Player:
    def __init__(self,name,location):
        self.name=name
        self.location=location
    def change_location(self,direction):
        if direction =='w':
            self.location=self.location.n_to
        elif direction=='s':
            self.location=self.location.s_to
        elif direction=='a':
            self.location=self.location.w_to
        elif direction =='d':
            self.location=self.location.e_to
            
        # location=['outside','foyer','narrow']
        # for place in location:
        #     if self.location == place:
        #         if self.location=='outside':
        #             print('Outside yall')
        #         elif self.location=='foyer':
        #             self.location='overlook'
        #         elif self.location=='narrow':
        #             self.location='treasure'
        # else:
        #     pass