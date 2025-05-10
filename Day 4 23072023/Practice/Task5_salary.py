num_tabs = int(input())
salary_amount = int(input())

count_facebook = 0
count_instagran = 0
count_reddit = 0

for i in range(1, num_tabs+1):
    website_open = input()
    if website_open == "Facebook":
        count_facebook += 1
    elif website_open == "Instagram":
        count_instagran += 1
    elif website_open == "Reddit":
        count_reddit += 1
    elif website_open == "":
        break

lost_facebook = count_facebook * 150
lost_instagram = count_instagran * 100
lost_reddit = count_reddit * 50

salary_post_fines = salary_amount - lost_facebook - lost_instagram - lost_reddit


if salary_post_fines <= 0:
    print("You have lost your salary.")
else:
    print(f"{salary_post_fines:0}")
