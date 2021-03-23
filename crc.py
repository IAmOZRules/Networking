def splitdata(data, frame_size):
    if len(data) % 2 == 0:
        data = data
    else:
        data = data.zfill(len(data)+1)

    m = [data[i:i+frame_size] for i in range(0, len(data), frame_size)]
    return m

# performs XOR operation on inputs
def xor(a, b): 
    result = [] 
   
    for i in range(1, len(b)): 
        if a[i] == b[i]: 
            result.append('0') 
        else: 
            result.append('1') 
   
    return ''.join(result) 
   
   
# Performs Modulo-2 division 
def mod2div(divident, divisor): 
    pick = len(divisor) 
    tmp = divident[0 : pick] 
   
    while pick < len(divident): 
        if tmp[0] == '1': 
            tmp = xor(divisor, tmp) + divident[pick] 
        else:   # If leftmost bit is '0' 
            tmp = xor('0'*pick, tmp) + divident[pick] 
        pick += 1

    if tmp[0] == '1': 
        tmp = xor(divisor, tmp) 
    else: 
        tmp = xor('0'*pick, tmp) 
   
    checkword = tmp 
    return checkword 

def sender(data, CRC_generator, frame_size, frame_no):
    checkword = mod2div(data, CRC_generator)
    message = data + checkword

    print("\n--------------- SENDER ---------------")
    print("Sending Frame {} -> {}".format(frame_no, data))
    print("Appending checkword to data: {}".format(checkword))
    print("Sending message -> {}".format(message))
    return CRC_generator, message

def receiver(received_message, data, CRC_generator, frame_size, frame_no):
    print("\n--------------- RECEIVER ---------------")
    # received_message = input("-> Enter the receiving data: ")
    check = mod2div(received_message, CRC_generator)
    print("-> Receiving data: {}".format(received_message))
    print("Generated CRC is: {}".format(check))

    print("\n--> Sending ACK 1")

    while '1' in check:
        print("--> ACK 1 Failed")
        print("--> Received frame {} with error".format(frame_no))

        CRC = sender(data, CRC_generator, frame_size, frame_no)
        
        print("\n--------------- RECEIVER ---------------")
        received_message = input("-> Enter the receiving data again: ")
        check = mod2div(received_message, CRC_generator)
        print("Generated CRC is: {}".format(check))

    if '1' not in check:
        print("--> ACK 1 Received")
        print("--> Error Free data received!\n")

# driver code
data = input("Enter the data to be sent -> ")
frame_size = 4
split_data = splitdata(data, frame_size)
CRC_generator = input("Enter the CRC generator string -> ")
print("")

for i in range(len(split_data)):
    print(">> FRAME {} -> {}".format(i, split_data[i]))

# send_data = ['1010011', '1001001']
for i in range(len(split_data)):
    CRC, message = sender(split_data[i], CRC_generator, frame_size, i)
    receiver(message, split_data[i], CRC, frame_size, i)
