import unittest                                                                                               
                                                                                                              
# Here's our "unit".                                                                                          
def IsOdd(n):                                                                                                 
    return n % 2 == 1                                                                                         
                                  
def prefix(network_mask):
    total=0
    mask_list = network_mask.split(".")
    for mask in mask_list:
        b = bin(int(mask))
        total += b.count("1")
    return total
        
                                                                                         
# Here's our "unit tests".                                                                                    
class PrefixTests(unittest.TestCase):                                                                          
                                                                                                              
    def testOne(self):                                                                                        
        self.assertEqual(prefix("255.255.0.0"), 16)                                                                            
                                                                                                              
def main():                                                                                                   
    unittest.main()                                                                                           
                                                                                                              
if __name__ == '__main__':                                                                                    
    main()                         
