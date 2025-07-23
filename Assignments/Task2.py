def whatsapp_chat_analysis(users):
    def total_no_of_messages():
        no_of_messages=0
        for k in users.keys():
            no_of_messages+=len(users[k])
        return no_of_messages
    
    def Unique_users():
        return set(users.keys())
    
    def total_words_in_chat():
        words_count=0
        for v in users.values():
            for i in v:
                words_count+=len(i.split())
        return words_count
    
    def words_per_message():
        return round(total_words_in_chat() / total_no_of_messages(), 2)
    
    def longest_message():
        longest_message_length=""
        key=""
        for keys,values in users.items():
            for value in values:
                if(len(value)>len(longest_message_length)):
                    longest_message_length=value
                    key=keys
        print(f"Longest message {key}:{longest_message_length}")
    
    def most_active_user():
        active_user=""
        total_no_of_messages_by_active_user=0
        for k,values in users.items():
            if len(values)>total_no_of_messages_by_active_user:
                total_no_of_messages_by_active_user=len(values)
                active_user=k
        print(f"Most active user {active_user} {(total_no_of_messages_by_active_user)} messages")
    
    def message_count(key):
        if key in users:
            print(f" message sent by {key} : {len(users[key])}")
        else:
            print(-1)

    def most_frequent_word_by_user(key):
        words_count={}
        if key in users:
            for values in users[key]:
                for i in values.split():
                    if i not in words_count:
                        words_count[i]=1
                    else:
                        words_count[i]+=1
        print(f"Most frequent word used by {key}:{max(words_count,key=words_count.get)}")

    def first_last_message_by_user(key):
        if key in users:
            first_message=users[key][0]
            last_message=users[key][-1]
            print(f"first message by {key} :{first_message} \nlast by {key} :{last_message}")
        else:
            print(-1)
    
    def check_user(key):
        if key in users:
            print(f"User {key} is in the chat")
        else:
            print(f"User {key} is not found in the chat") 

    def commonly_repeated_words():
        words_count={}
        for value in users.values():
            for messages in value:
                for word in messages.split():
                    words_count[word]=words_count.get(word,0)+1
        maximum_repeated= max(words_count.values())
        result=[word for word,count in words_count.items() if count == maximum_repeated]
        print(f"Common repeated words :{set(result)}")
    
    def user_longest_average():
        s={}
        for key ,values in users.items():
            word_count=0
            no_of_message=len(values)
            for msgs in values:
                    word_count+=len(msgs.split())
            s[key]=word_count/no_of_message
        longest_user=max(s,key=s.get)
        print(f"User with longest average message{longest_user} (avg {s[longest_user]:.2f} words)")

    def mention_user_in_message(key):
        count=0
        for value in users.values():
            for msgs in value:
                if key in msgs.split():
                    count+=1
        print(f"Message mentioning {key}:{count}")
    
    def unique_message():
        d=set()
        for values in users.values():
            for msgs in values:
                d.add(msgs)
        print(f"Unique messages count: {len(d)}")
        for msg in d:
            print(msg)
    
    def sort_messages():
        d=[]
        for msgs in users.values():
            d.extend(msgs)
        d.sort()
        print("\n".join(d))

    def questions_in_chat():
        d=[]
        for values in users.values():
            for msgs in values:
                if msgs.endswith("?"):
                    d.append(msgs)
        print("\n".join(d))

    def reply_ratio(name1,name2):
        count =0 
        if name2 in users:
            for msg in users[name2]:
                if name1 in msg:
                    count+=1 
        print(f"Reply ratio from {name2} to {name1} : {count} replies")    

    def check_for_deleted():
        count=0
        for values in users.values():
            for msg in values:
                if msg=="This message was deleted":
                    count+=1
        print(f"Deleted messages found :{count}")
    
    while True:
        print("\nWhat do you want to do?")
        print("1. Total number of messages")
        print("2. Unique users")
        print("3. Total words in chat")
        print("4. Words per message")
        print("5. Longest message")
        print("6. Most active user")
        print("7. Message count for a user")
        print("8. Most frequent word by a user")
        print("9. First and last message by a user")
        print("10. Check if user exists")
        print("11. Commonly repeated word(s)")
        print("12. User with longest average message")
        print("13. Mentions of a user")
        print("14. Unique messages")
        print("15. Sort all messages")
        print("16. Questions in chat")
        print("17. Reply ratio between two users")
        print("18. Check for deleted messages")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print(f"Total messages: {total_no_of_messages()}")
        elif choice == 2:
            print(f"Unique users: {Unique_users()}")
        elif choice == 3:
            print(f"Total words: {total_words_in_chat()}")
        elif choice == 4:
            print(f"Words per message: {words_per_message()}")
        elif choice == 5:
            longest_message()
        elif choice == 6:
            most_active_user()
        elif choice == 7:
            key = input("Enter user name: ")
            message_count(key)
        elif choice == 8:
            key = input("Enter user name: ")
            most_frequent_word_by_user(key)
        elif choice == 9:
            key = input("Enter user name: ")
            first_last_message_by_user(key)
        elif choice == 10:
            key = input("Enter user name: ")
            check_user(key)
        elif choice == 11:
            commonly_repeated_words()
        elif choice == 12:
            user_longest_average()
        elif choice == 13:
            key = input("Enter user name to check mentions: ")
            mention_user_in_message(key)
        elif choice == 14:
            unique_message()
        elif choice == 15:
            sort_messages()
        elif choice == 16:
            questions_in_chat()
        elif choice == 17:
            name1 = input("Enter user being replied to: ")
            name2 = input("Enter user replying: ")
            reply_ratio(name1, name2)
        elif choice == 18:
            check_for_deleted()
        elif choice == 0:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")

messages=int(input("Enter the number of messages: "))
print("messages should  be in format Name: message")
users={}
for i in range(messages):
    user,message=input("Enter the conversation: ").split(":")
    user=user.strip()
    message=message.strip()
    if user not in users:
        users[user]=[message]
    else:
        users[user].append(message)
print(users)

whatsapp_chat_analysis(users)
