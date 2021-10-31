from dataextract import get_row

class Investor (object):
    """
    A really cautious investor.  He never buys or sells anything.
    Extend it by making your own decide method.
    """
    def __init__(self, cash, num_markets):
        self.cash = cash
        self.account = [ 0 for i in range(0, num_markets) ]        
            
    def cash_out(self, prices):
        print "Cashing out"
        for i, a in enumerate(self.account):
            print "Market %d -> %d * %f = %f" % (i, a, prices[i], a * prices[i])
            self.cash += a * prices[i]
    
    def buysell(self, idx, qty, price):
        print "buy %d %d" % (idx, qty)
        self.account[idx] += qty
        self.cash -= qty * price
        
    def decide(self, data):
        pass

class InvestorOne (Investor):
    def __init__(self, cash, num_markets):
        Investor.__init__(self, cash, num_markets)
    
    def decide(self, data):
        if len(data) < 2:
            return
        
        # see which market is the most expensive
        highidx = -1
        highprice = -1
        prev = data[-2]
        cur = data[-1]
        hmove = 0        
        for i, p in enumerate(cur):
            if i == 0 or highprice < p:
                highidx = i
                highprice = p
                hmove = p - prev[i]
                                
        # see what the movement was for all but the most expensive
        tmove = 0
        for i, p in enumerate(cur):
            if i != highidx:
                tmove += p - prev[i]
                
        # if all the others moved and the highest didn't, buy or sell the expensive one
        if hmove == 0:
            if tmove < 0:
                # buy 1
                if self.cash >= highprice:
                    self.buysell(highidx, 1, highprice)
            elif tmove > 0 and self.account[highidx] > 0:
                # sell 1
                self.buysell(highidx, -1, highprice)


def main():
    data = [ ]
    dr = None
    prevdt = None
    for row in get_row():
        dt = row[1]
        if dr is None or len(dr) == 0 or prevdt != dt:
            dr = [ ]
            data.append(dr)
            prevdt = dt
        dr.append(float(row[2]))
        
    num_markets = len(dr)
    cash = 1000
    
    inv = InvestorOne(cash, num_markets)

    # feed the investor all the data, but only let it
    # see the history grow one item at a time.
    d_cur = [ ]    
    for r in data:
        d_cur.append(r)
        inv.decide(d_cur)
        
    # force a cash-out
    inv.cash_out(data[-1])    
    print inv.cash

if __name__ == '__main__':
    main()
