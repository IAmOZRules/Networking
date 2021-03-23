# Splits the data into frames
def splitdata(data, frame_size):
    if len(data) % 2 == 0:
        data = data
    else:
        data = data.zfill(len(data)+1)

    m = [data[i:i+frame_size] for i in range(0, len(data), frame_size)]
    return m

# Outputs the complement of the input message
def complement(message):
    complement = ""
    for i in message:
        if i == '1':
            complement += '0'
        else:
            complement += '1'
    return complement

# Creates the checksum of the input message
def checksum(message_bits, frame_size):
    sum = message_bits[0]
    for i in range(1, len(message_bits)-1):
        sum = bin(int(sum, 2) + int(message_bits[i], 2))
        sum = sum[2:]
        if len(sum) > frame_size:
            extra = sum[0]; frame = sum[1:]
            sum = bin(int(frame, 2) + int(extra, 2))
            sum = sum[2:]
    checksum = complement(sum)
    return checksum

# check if received data is correct or not
def check(message_bits, frame_size, checksum):
    sum = message_bits[0]
    for i in range(1, len(message_bits)):
        sum = bin(int(sum, 2) + int(message_bits[i], 2))
        sum = sum[2:]
        if len(sum) > frame_size:
            extra = sum[0]; frame = sum[1:]
            sum = bin(int(frame, 2) + int(extra, 2))
            sum = sum[2:]
    
    check = bin(int(sum,2) + int(checksum,2))
    check = check[2:]

    if '0' in check:
        return False, complement(sum)
    return True, complement(sum)
def sender(send, checksum, frame_no):
    print("\n--------------- SENDER ---------------")
    print("> Frame {}: {}".format(frame_no, send))
    sending_frame = send + checksum

    print("Appending checksum bit: {}".format(checksum))
    print("Sending frame {} -> {}".format(frame_no, sending_frame))
    return sending_frame

def receiver(receiving_frame, sender_checksum, frame_no):
    print("\n--------------- RECEIVER ---------------")
    print("-> Receiving FRAME {}: {}".format(frame_no, receiving_frame))

    receiver_bits = splitdata(receiving_frame, frame_size)
    receive, receive_checksum = check(receiver_bits, frame_size, checksum)
    print("Checksum is: {}".format(receive_checksum))

    print("\n--> Sending ACK 1")

    while not receive:
        print("--> ACK 1 Failed")
        print("--> Received data with error in frame {}!".format(frame_no))

        sender(receiving_frame, sender_checksum, frame_no)

        print("\n--------------- RECEIVER ---------------")
        receiving_frame=input("Enter the received frame {} again: ".format(i))
        print("\n-> Receiving FRAME: {}".format(receiving_frame))

        receiver_bits = splitdata(receiving_frame, frame_size)
        receive, receive_checksum = check(receiver_bits, frame_size, checksum)
        print("--> Checksum is: {}".format(receive_checksum))

    if receive:
        print("--> ACK 1 Received")
        print("--> Error Free data received!")
        
# Driver code
data = input("\nEnter the data to be sent: ")
frame_size = 4
message_bits = splitdata(data, frame_size)
checksum = checksum(message_bits, frame_size)
for i in range(len(message_bits)):
    print("> FRAME {}: {}".format(i, message_bits[i]))

# send_data = ['0110', '1001']
for i in range(len(message_bits)):
    sending_frame = sender(message_bits[i], checksum, i)
    receive = receiver(message_bits[i], checksum, i)

print("")
