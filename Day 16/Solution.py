def load_input(file):
    with open(file, 'r') as f:
        return str(f.readline()).strip()

def convert(line):
    translation = {
        "0" : "0000",
        "1" : "0001",
        "2" : "0010",
        "3" : "0011",
        "4" : "0100",
        "5" : "0101",
        "6" : "0110",
        "7" : "0111",
        "8" : "1000",
        "9" : "1001",
        "A" : "1010",
        "B" : "1011",
        "C" : "1100",
        "D" : "1101",
        "E" : "1110",
        "F" : "1111"
    }
    binary = ""
    for x in line:
        binary = "".join([binary, translation[x]])
    return binary


def read_transmission(transmission):
    line = transmission
    packets = []
    packet, i = read_packet(line, 0)
    packets = append_all(packets, packet)
    return packets

def read_packet(line, i):
    version = int(line[i:i+3], 2)
    typeID = int(line[i+3:i+6], 2)
    i += 6
    if typeID == 4:
        packet, i = read_literal(line, version, i)
    else:
        packet, i = read_operator(line, version, typeID, i)
    return packet, i

def read_literal(line, version, i):
    packet = Literal(version)
    value = ""
    bits = ["1"]
    while bits[0]=="1":
        bits = line[i:i+5]
        i += 5
        value = "".join([value, bits[1:]])
    packet.set_value(int(value,2))
    return packet, i

def read_operator(line, version, typeID, i):
    len_type = int(line[i])
    i += 1
    packet = Operator(version, typeID)
    if len_type == 0:
        length = int(line[i:i+15], 2)
        i+=15
        ending = i+length
        while(i<ending):
            subpacket, i = read_packet(line, i)
            packet.add_subpacket(subpacket)
    else:
        subs_number = int(line[i:i+11], 2)
        i+=11
        for _ in range(subs_number):
            subpacket, i = read_packet(line, i)
            packet.add_subpacket(subpacket)
    return packet, i


def append_all(packets, packet):
    packets.append(packet)
    if isinstance(packet, Operator):
        subs = packet.get_subpackets()
        for sub in subs:
            packets = append_all(packets, sub) 
    return packets

def versions_sum(packets):
    sum = 0
    for packet in packets:
        sum += packet.version
    return sum

def main():
    # load file
    transmission = convert(load_input("input.txt"))
    packets = read_transmission(transmission)

    # part 1
    sum = versions_sum(packets)
    print("Part 1: " + str(sum))
    
    # part 2
    packets[0].calc_value() #outermost packet - makes all subpackets calc their values
    print("Part 2: " + str(packets[0].value))
    

class Packet:
    def __init__(self, version, typeID):
        self.version = version
        self.typeID = typeID

class Literal(Packet):
    #version - int
    #typeID = 4
    #value - int

    def __init__(self, version):
        super().__init__(version, 4)
        self.value = 0

    def set_value(self, value):
        self.value = value

class Operator(Packet):
    #version - int
    #typeID - int
    #subpackets - list
    #value - int

    def __init__(self, version, typeID):
        super().__init__(version, typeID)
        self.subpackets = []
        self.value = None

    def add_subpacket(self, subpacket):
        self.subpackets.append(subpacket)

    def get_subpackets(self):
        return self.subpackets

    def calc_value(self):
        for sub in self.subpackets:
            if isinstance(sub, Operator) and sub.value == None:
                sub.calc_value()
        match self.typeID:
            case 0:         #sum
                sum = 0
                for sub in self.subpackets:
                    sum += sub.value
                self.value = sum
            case 1:         #product
                prod = 1
                for sub in self.subpackets:
                    prod *= sub.value
                self.value = prod
            case 2:         #minimum
                numbers = [sub.value for sub in self.subpackets]
                self.value = min(numbers)
            case 3:         #maximum
                numbers = [sub.value for sub in self.subpackets]
                self.value = max(numbers)
            case 5:         #a>b
                if self.subpackets[0].value>self.subpackets[1].value:
                    self.value = 1
                else:
                    self.value = 0
            case 6:         #a<b
                if self.subpackets[0].value<self.subpackets[1].value:
                    self.value = 1
                else:
                    self.value = 0
            case 7:         #a=b
                if self.subpackets[0].value==self.subpackets[1].value:
                    self.value = 1
                else:
                    self.value = 0

if __name__ == '__main__':
    main()