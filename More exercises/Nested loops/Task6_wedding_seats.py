last_sector: str = input()
last_sector_to_a: int = ord(last_sector)
first_sector_rows: int = int(input())
seats_odd: int = int(input())
seats_even: int = seats_odd + 2

first_sector_to_a: int = ord("A")
seat_start_a: int = ord("a")
seat_end_odd: int = seat_start_a + seats_odd
seat_end_even: int = seat_start_a + seats_even
total_seats: int = 0

for sector in range(first_sector_to_a, last_sector_to_a + 1):
    for row in range(1, first_sector_rows + 1):

        if row % 2:

            for seat in range(seat_start_a, seat_end_odd):
                print(f"{chr(sector)}{row}{chr(seat)}")
                total_seats += 1
        elif not row % 2:

            for seat in range(seat_start_a, seat_end_even):
                print(f"{chr(sector)}{row}{chr(seat)}")
                total_seats += 1
    first_sector_rows += 1
print(f"{total_seats}")
