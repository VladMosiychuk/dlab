class Endianify:

    @staticmethod
    def HexToLittleEndian(value: str) -> int:

        return int.from_bytes(bytes.fromhex(value), 'little')

    @staticmethod
    def HexToBigEndian(value: str) -> int:

        return int.from_bytes(bytes.fromhex(value), 'big')

    @staticmethod
    def LittleEndianToHex(value: int, length: int) -> str:

        return bytes.hex(int.to_bytes(value, length, 'little'))

    @staticmethod
    def BigEndianToHex(value: int, length: int) -> str:

        return bytes.hex(int.to_bytes(value, length, 'big'))

    @staticmethod
    def BytesCount(value: str) -> int:

        return len(bytes.fromhex(value))
