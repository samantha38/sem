import hashlib

class BloomFilter:

    def __init__(self, size=200, hash_count=4):
        self.size = size
        self.hash_count = hash_count

        # Create bit array
        self.bit_array = [0] * size

    def _get_hashes(self, item):
        positions = []

        for i in range(self.hash_count):
            data = f"{item}{i}".encode("utf-8")

            hash_value = hashlib.sha256(data).hexdigest()

            position = int(hash_value, 16) % self.size

            positions.append(position)

        return positions

    def add(self, item):
        positions = self._get_hashes(item)

        for position in positions:
            self.bit_array[position] = 1

    def contains(self, item):
        positions = self._get_hashes(item)

        for position in positions:
            if self.bit_array[position] == 0:
                return False

        return True