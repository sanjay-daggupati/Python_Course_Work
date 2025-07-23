def whatapp_chat_analysis(users):
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
        no_of_messages=0
        for k in users.keys():
            no_of_messages+=len(users[k])
        words_count=0
        for v in users.values():
            for i in v.split():
                words_count+=len(i.split())
        return round((words_count/no_of_messages),2)
    
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
    



messages=int(input("Enter the number of messages: "))
print("messages shouldb be in format Name: message")
users={}
for i in range(messages):
    user,message=input("Enter the conversation: ").split(":")
    if user not in users:
        users[user]=[message]
    else:
        users[user].append(message)
print(users)
