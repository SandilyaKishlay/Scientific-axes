import numpy as np

class AxisRange:
    def __init__(self, start, stop, transform=None):
      self.start=start
      self.stop=stop
      self.transform=transform
    def ApplyTransform(self, value):
      if self.transform is None:
        return value
      else:
        return self.transform(value)
class LinierRange(AxisRange):
    def __init__(self,start,stop):
      super().__init__(start,stop)
    def __repr__(self):
      return f'LinearRange({self.start}, {self.stop})'
class LogRange(AxisRange):
    def __init__(self, start, stop, base=10):
        super().__init__(start, stop, transform=lambda x: np.log(x) / np.log(base))
        self.base = base
        
    def __repr__(self):
        return f'LogRange({self.start}, {self.stop}, base={self.base})'
        
class PolarRange(AxisRange):
    def __init__(self, start, stop):
        super().__init__(start, stop, transform=lambda x: np.deg2rad(x))
        
    def __repr__(self):
        return f'PolarRange({self.start}, {self.stop})'
        
class HyperbolicRange(AxisRange):
    def __init__(self, start, stop):
        super().__init__(start, stop, transform=lambda x: np.arcsinh(x))
        
    def __repr__(self):
        return f'HyperbolicRange({self.start}, {self.stop})'
  
      
