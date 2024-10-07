from dataclasses import dataclass


@dataclass(frozen=True)
class Structure:
    PAYLOAD_SIZE = 7

    command: int
    sequence: int
    reserved: int = 0
    temperature: int = 0
    temperature_p: int = 0

    def cc(self) -> int:
        return self.sequence ^ self.reserved ^ self.temperature ^ self.temperature_p

    def get_full_temperature(self) -> float:
        return self.temperature + (.1 * self.temperature_p)

    def serialize(self) -> bytes:
        return bytes([
            0x88,
            1 + self.command,
            1 + self.sequence,
            1 + self.reserved,
            1 + self.temperature,
            1 + self.temperature_p,
            1 + self.cc(),
        ])

    @classmethod
    def deserialize(cls, data: bytes):
        if len(data) != cls.PAYLOAD_SIZE:
            raise ValueError(f"Invalid data length (len={len(data)})")

        if data[0] != 0x88:
            raise ValueError("Invalid header")

        deserialized = cls(
            command=data[1]-1,
            sequence=data[2]-1,
            reserved=data[3]-1,
            temperature=data[4]-1,
            temperature_p=data[5]-1
        )

        if deserialized.cc() != data[6]-1:
            raise ValueError("Invalid checksum")

        return deserialized

    @classmethod
    def invalid(cls, command: int, sequence: int):
        return cls(
            command=command,
            sequence=sequence,
            reserved=0x00,
            temperature=0x00,
            temperature_p=0x00,
        )
