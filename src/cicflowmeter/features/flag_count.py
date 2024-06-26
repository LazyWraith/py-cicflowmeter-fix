from scapy.layers.inet import IP, TCP

class FlagCount:
    """This class extracts features related to the Flags Count."""

    def __init__(self, feature):
        self.feature = feature
        self.flags = {
            "F": "FIN",
            "S": "SYN",
            "R": "RST",
            "P": "PSH",
            "A": "ACK",
            "U": "URG",
            "E": "ECE",
            "C": "CWR",
        }

    def has_flag(self, flag, packet_direction=None) -> bool:
        """Count packets by direction.

        Returns:
            packets_count (int):

        """
        packets = (
            (
                packet
                for packet, direction in self.feature.packets
                if direction == packet_direction
            )
            if packet_direction is not None
            else (packet for packet, _ in self.feature.packets)
        )

        for packet in packets:
            if packet.haslayer(TCP) and flag[0] in str(packet[TCP].flags):
                return 1
        return 0
