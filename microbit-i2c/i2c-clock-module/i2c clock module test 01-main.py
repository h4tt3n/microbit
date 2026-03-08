from microbit import *

devices = i2c.scan()
print(devices)

# Clear Clock Halt bit and start clock at 00 seconds
i2c.write(0x68, b'\x00\x00')

# Convert numbers to BCD (Binary-Coded Decimal)
def to_bcd(n):
    return (n // 10) << 4 | (n % 10)

seconds = to_bcd(56)  # Clear CH bit and set seconds
minutes = to_bcd(34)
hours = to_bcd(12)  # 12-hour or 24-hour format
day_of_week = 2  # Monday = 1, etc.
day = to_bcd(11)
month = to_bcd(2)
year = to_bcd(25)  # 2025 -> store only last two digits

# Write to DS1307/DS3231
i2c.write(0x68, bytes([0x00, seconds, minutes, hours, day_of_week, day, month, year]))

print("Time set!")

while True:
    # Wait a bit and read again
    sleep(1000)
    i2c.write(0x68, b'\x00')  # Set read pointer
    data = i2c.read(0x68, 7)  # Read 7 bytes
    print(list(data))  # Should now show updated time




i2c.write(0x68, b'\x00')  # Set read pointer
data = i2c.read(0x68, 7)  # Read 7 bytes
print(list(data))  # Should now show updated time