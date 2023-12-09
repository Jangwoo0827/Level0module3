for i in range(1):
   b = 99
   for r in range(100):
      if b == 0:
         print "No bottles of beer on the wall!"
         print "No bottles of beer!"
         print "Go to the store and buy some more"
         print "99 bottles of beer on the wall!"


      else:
         print b, "bottles of beer on  the wall"
         print b, "bottles of beer!"
         print "Take one down, pass it around"
         print b - 1, "bottles of beer on the wall!"
         b = b - 1
