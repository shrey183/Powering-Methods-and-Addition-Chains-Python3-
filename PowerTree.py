# -*- coding: utf-8 -*-

class PowerTree:
  def __init__(self): 
    self.layers=[[1]]
    self.parent={1:1}
  	
  def path_from_root(self,k):  
      if k not in self.parent:
          return -1
      a = [k]
      x = k
      while x != 1:
          x = self.parent[x]
          a.append(x)
      return a[::-1]

  def add_layer(self):
      newleaves = []
      for layer in self.layers:
          for m in layer:
              for i in self.path_from_root(m):
                  if i+m not in self.parent:
                      self.parent[i+m] = m
                      newleaves.append(i+m)
      self.layers.append(newleaves)                     
                      
      
  def draw_tree(self):
    for i in range(len(self.layers)):	
        print("layer",i)
        for j in self.layers[i]: print(j,"->",self.parent[j])





    

