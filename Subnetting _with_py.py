def FLSM(ip_num,k):   #Fixed Length Subnet Mask
    value=0
    while True:        #Calculating the Nearest value
        value=2**k
        if value>ip_num:
            break
        k+=1
    print("The Nearest value Of the Given IP'S Range is:",value)
    main_list=[]
    val=''
    bit_val=256
    b_val=0
    if ip_num<=255:
        Prefix_length=24    # Default Prefix Length of class c
        print("The Default subnetmask of Class C is :",C)
        s=C.split('.')
        for j in range(len(s)):
            if int(s[j])==0:
                net_bits=8-k   #Gives us the Network Bits 
                for d in range(8):
                    if d<net_bits:
                        val+='1'
                        bit_val=bit_val//2
                        b_val=b_val+bit_val
                    else:
                        val+='0'
                main_list.append(int(val))
                #print(b_val)
            else:
                main_list.append(int(bin(int(s[j]))[2:]))
        print("The Binary representation of New Subnet Mask is:",*main_list)
        print("The New Subnet mask value is 255.255.255.",b_val)
        print("The Prefix length of the New SubnetMask is:",Prefix_length+net_bits)
        print("No of Networks :",2**net_bits,)
        print("No of Hosts :",2**k)
    elif(ip_num<=65025): #class B
        Prefix_length=16 #Default Prefix Length of class B
        print("Default subnetmask =",B)
        s=B.split('.')
        print(s,"bclass")
        for j in range(len(s)):
            if int(s[j])==0:
                main_list.append(int('00000000'))
            else:
                main_list.append(int(bin(int(s[j]))[2:]))
        #print(main_list) 
    else:  #class A
        Prefix_length=8  #Default Prefix length of Class A
        print("Default subnetmask =",A)
        s=A.split('.')
        print(s,"class c")
        for j in range(len(s)):
            if int(s[j])==0:
                main_list.append('00000000')
            else:
                main_list.append(bin(int(s[j]))[2:])
    #print(main_list) 
def VLSM(ip_num,k):   #Variable Length Subnet Mask
    c=1
    return c
print("Which type of subnetting method do you want to choose either FLSM or VLSM ?")
method=input()
print("How many IP's you required ?")
ip_num=int(input())
k=1
A='255.0.0.0'
B='255.255.0.0'
C='255.255.255.0'
if method=='FLSM':
    FLSM(ip_num,k)
else:
    VLSM(ip_num,k)   
