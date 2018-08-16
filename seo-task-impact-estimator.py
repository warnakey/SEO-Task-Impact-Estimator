# GIVE THE OPTION TO START THE PROGRAM OVER FROM THE BEGINNING
start_program = True
while start_program == True:
    
    # START THE MAIN PROGRAM
    print("What is the estimated impact of an SEO action?\n")

    # WHAT WAS THE WEBSITE'S TRAFFIC OVER THE LAST YEAR (to benchmark against) ?
    website_existed_last_year = True
    while website_existed_last_year == True:
        last_year_visitors = int(input("\nHow many Organic Visitors did the website have over the last 365 days? "))
        # Realistically, a website won't have more than 999 billion visitors in one year (if you do, congratulations!)
        if 1 <= last_year_visitors < 999999999999:
            break
        else:
            print("\nInvalid selection. Type a number representing how many people search for your target keyword each month.")
            continue

    # HOW MANY PEOPLE SEARCH FOR THE SITE'S MOST IMPORTANT KEYWORD ?
    target_keyword_volume_unknown = True
    while target_keyword_volume_unknown == True:
        target_keyword_volume = int(input("\nHow many people search for your target keyword each month? "))
        # Realistically, there should never be more than 99 billion people searching for something in one month
        if 1 <= target_keyword_volume < 99999999999:
            break
        else:
            print("\nInvalid selection. Type a number representing how many people search for your target keyword each month.")
            continue

    # LOCAL, NATIONAL OR INTERNATIONAL ?
    geo_target_unknown = True
    while geo_target_unknown == True:
        geo_target = input("\nIs the website targetting users on a local, national or international level?\nType 'local', 'national', or 'international.' ")
        geo = print("\nThe website has a " + geo_target + " focus.\n")
        if geo_target == "local" or geo_target == "national":
            geo
            break
        elif geo_target == "international":
            print("\nThe website has an " + geo_target + " focus.\n")
            break
        else:
            print("\nInvalid selection. Type either 'local', 'national', or 'international'.")
            continue

    # HOW MANY PEOPLE SEARCH FOR THE SITE'S MOST IMPORTANT KEYWORD ?
    population_size_unknown = True
    while population_size_unknown == True:
        market_population = int(input("How many people live in the area the site targets: "))
        # Realistically, there should never be more than 99 billion people living in one metro area
        if 1 <= market_population < 99999999999:
            break
        else:
            print("\nInvalid selection. Type a number representing how many people live in the area the site serves.")
            continue        

    # DOES THE SITE HAVE A BLOG ?
    blog_check = True
    while blog_check == True:
        blog = input("Does the site have a blog that is regularly updated with good content? ")
        if blog == "yes" or blog == "no":
            break
        else:
            print("\nInvalid selection. Type either 'yes' or 'no'.")
            continue

    # ADD THE OPTION TO ALLOW PEOPLE TO SEE THE IMPACT OF MULTIPLE SEO TASKS USING THE SAME INFORMATION GIVEN ABOVE

    task_impact_loop = True
    while task_impact_loop == True:

        # WHAT SEO ACTION DO YOU WANT TO ESTIMATE THE IMPACT OF ?
        action_not_yet_chosen = True
        while action_not_yet_chosen == True: 
            print("\nWhat is the SEO action you would like to estimate the impact of?\n1 - Allowing a site to be indexed\n2 - Ranking #1 on Google for the target keyword\n3 - Ranking #1 on Google for many target keywords\n4 - Getting several great backlinks\n5 - Creating a new Google My Business profile\n6 - Adding 10 new images and 1 new video to Google My Business\n7 - Creating a great Google Post\n8 - Creating 1 great piece of longform content\n9 - Disavowing spammy backlinks")

            action_choice = int(input("Choose an option: "))

            if 1 <= action_choice <= 10:        
                # MEASURE THE IMPACT OF AN SEO ACTION (these are my subjective opinion)
                if action_choice == 1:
                    action_value = 1000
                    break
                elif action_choice == 2:
                    action_value = (target_keyword_volume*12)*0.35
                    break
                elif action_choice == 3:
                    action_value = ((target_keyword_volume*12)*0.35)*4
                    break
                elif action_choice == 4:
                    action_value = (target_keyword_volume*12)*0.23
                    break
                elif action_choice == 5:
                    action_value = last_year_visitors+(target_keyword_volume*0.03)
                    break
                elif action_choice == 6:
                    action_value = last_year_visitors+(target_keyword_volume*0.07)
                    break
                elif action_choice == 7:
                    action_value = last_year_visitors+(target_keyword_volume*0.01)
                    break
                elif action_choice == 8:
                    action_value = (target_keyword_volume*12)*0.17
                    break
                else:
                    action_value = last_year_visitors*0.02
                    break
                break
            else:
                print("\nInvalid selection. Please enter a number between 1 and 9.\n")

        # FINISH CALCULATING THE IMPACT OF AN SEO ACTION AND OUTPUT THE ANSWER
        impact = last_year_visitors + action_value
        print()
        print(f"If this task were performed, the site is estimated to gain {action_value} visitors, totaling {impact} visitors over the next year.\n")
        print("\n-------------------------------------------------------------------------------------\n")
        
        # ASK TO RUN THE PROGRAM AGAIN USING THE SAME DATA
        ask_to_run_again_same_data = True
        while ask_to_run_again_same_data == True:
            again_same = input("Do you want to see the impact of a different SEO task using the same information you entered above? ")
            if again_same == "yes" or again_same == "no":
                break
            else:
                print("\nInvalid selection. Type either 'yes' or 'no'.")
                continue
                
        if again_same == "yes":
            continue
        elif again_same == "no":
            break
            
    # ASK TO RUN THE PROGRAM AGAIN FROM THE BEGINNING
    ask_to_run_again = True
    while ask_to_run_again == True:
        print()
        again = input("Do you want to restart the program? ")
        if again == "yes" or again == "no":
            break
        else:
            print("\nInvalid selection. Type either 'yes' or 'no'.")
            continue
            
    if again == "yes":
        continue
    elif again == "no":
        break
        
print("\nEnd.")
