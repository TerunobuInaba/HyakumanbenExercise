class carTraffic:
  def __init__(self, name, mode, arrival, gt):
    
    # name of to/from direction
    self.name = name
    
    # cycle time: c
    self.c = 114
    
    # arrival: α
    self.arrival = arrival
    
    # green time: gt
    self.gt = gt
    
    # red time: rt
    self.rt = self.c - gt
    
    # max flow: beta
    if mode == "straight":
        self.beta = 1400
    elif mode == "left" or mode == "right":
        self.beta = 500
    else:
      raise Exception("Invalid argument: Enter straight, left, or right for mode")
    
    # degree of saturation: rho
    self.rho = self.arrival * self.c / (self.beta * self.gt)

    # uniform delay: wu
    self.wu = 0.5 * (self.rt**(2)) / (self.c * (1 - self.arrival / self.beta))

    # random delay: wr
    self.wr = (self.rho**(2)) / (2 * self.arrival * (1 - self.rho))

    # total delay: w
    self.w = 0.9*(self.wu + self.wr)

    # total delay: W
    self.W = self.w * self.arrival * 114 / 3600

    # queue: q
    self.q = self.rho + 0.5 * (self.rho**(2)) / (1 - self.rho)

  def makeParamsIntoList(self):
    val = []
    val.append(self.name)
    val.append(self.arrival)
    val.append(self.beta)
    val.append(self.gt)
    val.append(self.rho)
    val.append(self.wu)
    val.append(self.wr)
    val.append(self.w)
    val.append(self.W)
    val.append(self.q)
    return val