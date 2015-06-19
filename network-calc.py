import unittest                                                                                               
                                                                                                              
# Here's our "unit".                                                                                          
def prefix(network_mask):
    total=0
    for mask in network_mask.split("."):
        b = bin(int(mask))
        total += b.count("1")
    return total

def network_addr(ipaddr, network_mask):
	na_list=[]
	ip_list = ipaddr.split(".")
	mask_list = network_mask.split(".")
	for i in range(len(ip_list)):
		na_list.append(str(int(ip_list[i]) & int(mask_list[i])))
	return '.'.join(na_list)

def bcast_addr(ipaddr, network_mask):
	host_mask=[]
	mask_list =network_mask.split(".")
	for i in range(len(mask_list)):
		host_mask.append(~ int(mask_list[i]) & 0xFF)

	ip_list = ipaddr.split(".")
	bcast_list=[]
	for i in range(len(ip_list)):
		bcast_list.append(str(int(ip_list[i]) | int(host_mask[i])))
	return '.'.join(bcast_list) 

def host_num(ipaddr, network_mask):
	host_mask=[]
	mask_list =network_mask.split(".")
	for i in range(len(mask_list)):
		host_mask.append(~ int(mask_list[i]) & 0xFF)

	ip_list = ipaddr.split(".")
	hostnum=[]
	for i in range(len(ip_list)):
		hostnum.append(str(int(ip_list[i]) & int(host_mask[i])))
	return '.'.join(hostnum) 

def max_hosts(ipaddr, network_mask):
	netmask_length = prefix(network_mask)
	return 2**(32 - netmask_length)-2 

# Here's our "unit tests".                                                                                    
class NetworkCalcTests(unittest.TestCase):                                                                          
	def testPrefix(self):                                                                                        
		self.assertEqual(prefix("255.255.0.0"), 16)                                                                            
	def testNetWorkAddr(self):                                                                                        
		self.assertEqual(network_addr("10.3.10.159","255.255.0.0"),"10.3.0.0")                                                                            
	def testBroadCastAddr(self):                                                                                        
		self.assertEqual(bcast_addr("10.3.10.159","255.255.0.0"),"10.3.255.255")                                                                            
	def testHostNum(self):                                                                                        
		self.assertEqual(host_num("10.3.10.159","255.255.0.0"),"0.0.10.159")                                                                            
	def testMaxHosts(self):                                                                                        
		self.assertEqual(max_hosts("10.3.10.159","255.255.0.0"),65534)                                                                            
                                                                                                              
def main():                                                                                                   
    unittest.main()                                                                                           
                                                                                                              
if __name__ == '__main__':                                                                                    
    main()               
