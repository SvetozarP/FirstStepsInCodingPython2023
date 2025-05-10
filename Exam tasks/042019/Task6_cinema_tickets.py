movie_name: str = input()

student_ticket: int = 0
standard_ticket: int = 0
kid_ticket: int = 0
ticket_per_movie: int = 0
total_tickets: int = 0
free_spaces: int = 100

while movie_name != "Finish":

    free_spaces: int = int(input())
    ticket_per_movie = 0

    while ticket_per_movie < free_spaces:

        ticket_type: str = input()

        if ticket_type == "End" or ticket_per_movie >= free_spaces:
            break

        elif ticket_type == "student":

            student_ticket += 1
            ticket_per_movie += 1

        elif ticket_type == "standard":

            standard_ticket += 1
            ticket_per_movie += 1

        elif ticket_type == "kid":

            kid_ticket += 1
            ticket_per_movie += 1

    print(f"{movie_name} - {ticket_per_movie / free_spaces * 100:.2f}% full.")
    movie_name: str = input()


total_tickets = student_ticket + standard_ticket + kid_ticket
print(f"Total tickets: {total_tickets}")
print(f"{student_ticket / total_tickets * 100:.2f}% student tickets.")
print(f"{standard_ticket / total_tickets * 100:.2f}% standard tickets.")
print(f"{kid_ticket / total_tickets * 100:.2f}% kids tickets.")
