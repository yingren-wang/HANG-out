

class WeekOfApril8(object):
    def __init__(self):
        self.pranay_active = None
        self.yingren_active = None
        self.blake_active = True
        self.jake_active = None
        self.sean_active = None
        self.yingren_roast_engines = "engaged"
        self.pranay_hype_boosters = "full power"
        self.blake_nap_time = "before gym"
        self.jake_neutrality = "maximum"
        self.sean_missing = True

    def botanical_gardens(self):
        role_list = [self.pranay_active, self.yingren_active, self.blake_active, self.jake_active, self.sean_active]
        going_list = []
        for person in role_list:
            if person:
                going_list.append(person)

        print (f'The following are going to Botanical Gardens: {going_list}')

    def gym(self):
        arm_day = 'good'
        leg_day = 'bad'
        if arm_day == 'good':
            go()
        if leg_day != 'good':
            skip()
        if yingren:
            skip()
        if sean:
            pullups()
