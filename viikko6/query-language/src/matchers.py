class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True
    
class Or(And):
    def __init__(self, *matchers):
        super().__init__(*matchers)
    
    def test(self, player):
        for mathcer in self._matchers:
            if mathcer.test(player):

                return True
        return False



class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class Not:
    def __init__(self, term):
        self._term = term

    def test(self, player):
        return not self._term.test(player)

class All:
    def __init__(self):
        pass

    def test(self, player):
        return True
    
class HasFewerThan(HasAtLeast):
    def __init__(self, value, attr):
        super().__init__(value, attr)
    
    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value
    
class QueryBuilder:
    def __init__(self):
        self._matchers = []
        self.one_Of = False

    def playsIn(self, team):
        self._matchers.append(PlaysIn(team))
        return self

    def hasAtLeast(self, value, attr):
        self._matchers.append(HasAtLeast(value, attr))
        return self

    def hasFewerThan(self, value, attr):
        self._matchers.append(HasFewerThan(value, attr))
        return self

    def oneOf(self, *arguments):
        self._matchers = [*arguments]
        self.one_Of = True
        return self

    def build(self):
        re_val = None
        if self.one_Of:
            re_val = Or(*self._matchers)
            self._matchers = []
            return re_val
        re_val = And(*self._matchers)
        self._matchers = []
        return re_val

