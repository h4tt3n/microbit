from microbit import *

I2C_ADDRESS = 0x68  # DS1307/DS3231 I2C Address

# Convert integer to Binary-Coded Decimal (BCD)
def to_bcd(n):
    return (n // 10) << 4 | (n % 10)

# Convert Binary-Coded Decimal (BCD) to integer
def from_bcd(bcd):
    return ((bcd >> 4) * 10) + (bcd & 0x0F)

# Set the RTC time (24-hour format)
def set_rtc(hours, minutes, seconds, day_of_week, day, month, year):
    """ Set RTC time (24-hour format). Year should be last two digits (e.g., 25 for 2025). """
    
    # Convert values to BCD format
    seconds_bcd = to_bcd(seconds) & 0x7F  # Ensure Clock Halt (CH) bit is cleared
    minutes_bcd = to_bcd(minutes)
    hours_bcd = to_bcd(hours) & 0x3F      # Ensure 24-hour format
    day_of_week_bcd = day_of_week         # No BCD conversion needed
    day_bcd = to_bcd(day)
    month_bcd = to_bcd(month)
    year_bcd = to_bcd(year)               # Store last two digits (e.g., 25 for 2025)

    # Write to RTC registers
    i2c.write(I2C_ADDRESS, bytes([0x00, seconds_bcd, minutes_bcd, hours_bcd, day_of_week_bcd, day_bcd, month_bcd, year_bcd]))

# Read RTC time and return a formatted string
def read_rtc():
    """ Read RTC time and return as a formatted string. """

    # Set read pointer to 0 (start of time registers)
    i2c.write(I2C_ADDRESS, b'\x00')
    
    # Read 7 bytes (seconds, minutes, hours, day_of_week, day, month, year)
    data = i2c.read(I2C_ADDRESS, 7)

    # Decode BCD values
    seconds = from_bcd(data[0] & 0x7F)  # Mask out CH bit
    minutes = from_bcd(data[1])
    hours = from_bcd(data[2] & 0x3F)    # Ensure 24-hour format
    day_of_week = data[3]               # No conversion needed
    day = from_bcd(data[4])
    month = from_bcd(data[5] & 0x1F)    # Mask out century bit
    year = 2000 + from_bcd(data[6])     # Convert two-digit year

    # Return formatted string
    return "Time: {:02}:{:02}:{:02}, Date: {}-{:02}-{:02}, Day of Week: {}".format(hours, minutes, seconds, year, month, day, day_of_week)

# 🧪 Test Code
print("Setting RTC to: 12:34:56, 2025-02-11 (Tuesday)")

# Set the RTC (Hours, Minutes, Seconds, Day of Week, Day, Month, Year)
set_rtc(12, 34, 56, 2, 11, 2, 25)

while True:
    sleep(1000)
    print(read_rtc())  # Continuously display the updated time
