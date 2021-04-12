def calcRedundantBits(length):
	for i in range(length):
		if(2**i >= length + i + 1):
			return i


def posRedundantBits(data, pos):
	j = 0
	k = 1
	m = len(data)
	res = ''

	for i in range(1, m + pos+1):
		if(i == 2**j):
			res = res + '0'
			j += 1
		else:
			res = res + data[-1 * k]
			k += 1

	return res[::-1]


def calcParityBits(data, pos):
	n = len(data)

	for i in range(pos):
		val = 0
		for j in range(1, n + 1):

			if(j & (2**i) == (2**i)):
				val = val ^ int(data[-1 * j])

		data = data[:n-(2**i)] + str(val) + data[n-(2**i)+1:]
	return data


def detectError(data, nr):
	n = len(data)
	res = 0

	for i in range(nr):
		val = 0
		for j in range(1, n + 1):
			if(j & (2**i) == (2**i)):
				val = val ^ int(data[-1 * j])

		res = res + val*(10**i)

	return int(str(res), 2)

def correctError(data, pos):
    data = list(data)
    if data[-pos] == '0':
        data[-pos] = '1'
    elif data[-pos] == '1':
        data[-pos] = '0'
    
    return str(''.join(data))

if __name__ == "__main__":
    print("SHREYAANS NAHATA: 19BCE2686\n")
    num_bits = int(input("Enter the number of bits in the message: "))
    data = input("Enter the frame to be sent: ")
    print("\n--------- SENDING DATA ---------")
    print("Sending frame: " + data)

    parity_len = calcRedundantBits(num_bits)
    arr = posRedundantBits(data, parity_len)
    arr = calcParityBits(arr, parity_len)

    codeword = ''
    for i in range(parity_len):
        codeword += arr[-2**i]

    print("The Code Word is: " + codeword)
    print("Data to be sent is: " + arr)

    print("\n--------- RECEIVING DATA ---------")
    rec = input("Enter the received message: ")
    correction = detectError(rec, parity_len)

    if correction == 0:
        print("ERROR FREE DATA RECEIVED!")
    else:
        print("The position of the error is: " + str(correction))
        correct_message = correctError(rec, correction)
        print("The corrected message is: " + correct_message)
