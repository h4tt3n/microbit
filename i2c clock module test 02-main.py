from microbit import *

devices = i2c.scan()
print(devices)

# Clear Clock Halt bit and start clock at 00 seconds
i2c.write(0x68, b'\x00\x00')

# Convert from BCD (Binary-Coded Decimal) to an integer
def from_bcd(bcd):
    return ((bcd >> 4) * 10) + (bcd & 0x0F)

# Convert numbers to BCD (Binary-Coded Decimal)
def to_bcd(n):
    return (n // 10) << 4 | (n % 10)

seconds = to_bcd(0)  # Clear CH bit and set seconds
minutes = to_bcd(50)
hours = to_bcd(14)  # 12-hour or 24-hour format
day_of_week = 2  # Monday = 1, etc.
day = to_bcd(11)
month = to_bcd(2)
year = to_bcd(25)  # 2025 -> store only last two digits

# Write to DS1307/DS3231
i2c.write(0x68, bytes([0x00, seconds, minutes, hours, day_of_week, day, month, year]))

print("Time set!")

while True:
    sleep(1000)
    i2c.write(0x68, b'\x00')  # Set read pointer
    data = i2c.read(0x68, 7)  # Read 7 bytes
    
    seconds = from_bcd(data[0] & 0x7F)  # Mask out CH bit
    minutes = from_bcd(data[1])
    hours = from_bcd(data[2] & 0x3F)  # Mask out 24-hour format bits
    day_of_week = data[3]
    day = from_bcd(data[4])
    month = from_bcd(data[5] & 0x1F)  # Mask out century bit
    year = 2000 + from_bcd(data[6])  # Convert two-digit year

    # Use string formatting instead of f-strings
    print("Time: {:02}:{:02}:{:02}, Date: {}-{:02}-{:02}".format(hours, minutes, seconds, year, month, day))
    #print(f"Time: {hours:02}:{minutes:02}:{seconds:02}, Date: {year}-{month:02}-{day:02}")
