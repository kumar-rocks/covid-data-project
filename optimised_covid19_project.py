import matplotlib.pyplot as plt
import pandas as pd



raw_data = pd.read_csv("state_wise_daily.csv")


states_code = raw_data.columns[3:-1].tolist()



raw_date = raw_data['Date'][::3]
date = pd.to_datetime(raw_date)


d_con = {}
for i in states_code:
    con = raw_data[i][::3].tolist()
    d_con[i] = con
    con = []
con_df = pd.DataFrame(d_con, index = date)


d_rec = {}
for i in states_code:
    rec = raw_data[i][1::3].tolist()
    d_rec[i] = rec
    rec = []
rec_df = pd.DataFrame(d_rec, index = date)


d_dec = {}
for i in states_code:
    dec = raw_data[i][2::3].tolist()
    d_dec[i] = dec
    dec = []
dec_df = pd.DataFrame(d_dec, index = date)

states = ['INDIA', 'ANDAMAN AND NICOBAR', 'ANDHRA PRADESH', 'ARUNACHAL PRADESH', 'ASSAM', 'BIHAR','CHANDIGARH',
              'CHATTISGARH', 'DADRA AND NAGAR HAVELI', 'DAMAN AND DIU', 'DELHI', 'GOA', 'GUJARAT', 'HARYANA',
              'HIMACHAL PRADESH', 'JAMMU AND KASHMIR', 'JHARKHAND', 'KARNATAKA', 'KERALA', 'LADAKH', 'LAKSHADWEEP',
              'MADHYA PRADESH', 'MAHARASHTRA', 'MANIPUR', 'MEGHALAYA', 'MIZORAM', 'NAGALAND', 'ODISHA', 'PONDICHERRY',
              'PUNJAB', 'RAJASTHAN', 'SIKKIM', 'TAMIL NADU', 'TELANGANA', 'TRIPURA', 'UTTAR PRADESH', 'UTTARAKHAND',
              'WEST BENGAL']


states_list = pd.DataFrame(states, states_code)



while True:
    print()
    print("WELCOME TO COVID DATA MANAGEMENT SYSTEM!")

    print('''
    HI!
    I AM PY.
    WHAT IS YOUR NAME?''')

    user_name = input().upper()

    if user_name == "EXIT":
        break

    print('''
    NICE TO MEET YOU''', user_name + ''' :)
    I AM HERE TO GUIDE YOU.''')



    while True:
        print('''
        1. DATA VISUALISATION
        2. NUMERIC DATA
        ENTER THE GIVEN OPTION OR ENTER EXIT TO EXIT''')
        option = input().upper()
        if option == "1":
            while True:
                print('''YOU WANT TO PLOT THE GRAPH:
                1. LINE GRAPH
                2. BAR GRAPH
                3. PIE GRAPH''')
                graph_option = input().upper()
                if graph_option == "1":
                    while True:
                        print('''SELECT
                        1. ONE STATE GRAPH
                        2. MULTI STATE GRAPH(COMPARING)''')
                        type_graph = input().upper()
                        if type_graph == "1":
                            while True:
                                print("ENTER THE CODE NAME OF STATE(TO SEE THE STATE CODE NAME LIST ENTER 'SHOW LIST')")
                                user_state_name = input().upper()
                                if user_state_name == 'SHOW LIST':
                                    print(states_list)
                                if user_state_name in states_code:
                                    while True:
                                        print('''PLEASE SELECT PARAMETER
                                        1. CONFIRMED
                                        2. RECOVERED
                                        3. DECEASED''')
                                        para_option = input().upper()
                                        if para_option == "1":
                                            plt.plot(date, con_df[user_state_name], color = "navy")
                                            plt.title("CONFIRMED CASES GRAPH OF "
                                                      + states_list.loc[user_state_name].to_list()[0])
                                            plt.xlabel("DATE")
                                            plt.ylabel("CONFIRMED CASES")
                                        elif para_option == "2":
                                            plt.plot(date, rec_df[user_state_name], color = "darkgreen")
                                            plt.title("RECOVERED CASES GRAPH OF "
                                                      + states_list.loc[user_state_name].to_list()[0])
                                            plt.xlabel("DATE")
                                            plt.ylabel("RECOVERED CASES")
                                        elif para_option == "3":
                                            plt.plot(date, dec_df[user_state_name], color = "maroon")
                                            plt.title("DECEASED CASES GRAPH OF "
                                                      + states_list.loc[user_state_name].to_list()[0])
                                            plt.xlabel("DATE")
                                            plt.ylabel("DECEASED CASES")
                                        elif para_option == "EXIT":
                                            break
                                        else:
                                            print("ENTER THE CORRECT OPTION")
                                        plt.gcf().autofmt_xdate()
                                        plt.show()
                                elif user_state_name == "EXIT":
                                    break
                                else:
                                    print("ENTER THE CORRECT OPTION")
                        elif type_graph == "2":
                            while True:
                                multi_state = []
                                print("HOW MANY STATES YOU WANT TO COMPARE")
                                num = input().upper()
                                print(states_list)
                                if num == "EXIT":
                                    break
                                for i in range(int(num)):
                                    print("ENTER THE STATES CODE NAME")
                                    multi_name = input().upper()
                                    if multi_name in states_code:
                                        multi_state.append(multi_name)
                                    elif multi_name == "EXIT":
                                        break
                                if len(multi_state) == int(num):
                                    while True:
                                        print('''PLEASE SELECT PARAMETER
                                        1. CONFIRMED
                                        2. RECOVERED
                                        3. DECEASED''')
                                        para_option = input().upper()
                                        if para_option == "1":
                                            plt.title("CONFIRMED CASES GRAPH")
                                            plt.xlabel("DATE")
                                            plt.ylabel("CONFIRMED CASES")
                                            for i in multi_state:
                                                plt.plot(date, con_df[i], label = states_list.loc[i].to_list()[0])
                                        elif para_option == "2":
                                            plt.title("RECOVERED CASES GRAPH OF")
                                            plt.xlabel("DATE")
                                            plt.ylabel("RECOVERED CASES")
                                            for i in multi_state:
                                                plt.plot(date, rec_df[i], label = states_list.loc[i].to_list()[0])
                                        elif para_option == "3":
                                            plt.title("DECEASED CASES GRAPH OF")
                                            plt.xlabel("DATE")
                                            plt.ylabel("DECEASED CASES")
                                            for i in multi_state:
                                                plt.plot(date, dec_df[i], label = states_list.loc[i].to_list()[0])
                                        elif para_option == "EXIT":
                                            break
                                        else:
                                            print("ENTER THE CORRECT OPTION")
                                        plt.gcf().autofmt_xdate()
                                        plt.legend()
                                        plt.show()
                                else:
                                    break
                        elif type_graph == 'EXIT':
                            break
                        else:
                            print("ENTER THE CORRECT OPTION")
                elif graph_option == "2":
                    while True:
                        print("ENTER THE CODE OF NAME OF STATE(TO SEE THE STATE CODE LIST ENTER 'SHOW LIST')")
                        user_state_name = input().upper()
                        if user_state_name == 'SHOW LIST':
                            print(states_list)
                        if user_state_name in states_code:
                            list_of_data = [con_df[user_state_name].sum(), rec_df[user_state_name].sum(),
                                            dec_df[user_state_name].sum()]
                            list_of_para = ['CONFIRMED', 'RECOVERED', 'DECEASED']
                            plt.bar(list_of_para, list_of_data, color=['navy', 'darkgreen', 'maroon'])
                            plt.title("BAR GRAPH OF " + states_list.loc[user_state_name].to_list()[0] + " CASES")
                            plt.ylabel("NUMBER OF CASES")
                            plt.show()
                        elif user_state_name == "EXIT":
                            break
                        else:
                            print("ENTER THE CORRECT OPTION")
                elif graph_option == "3":
                    while True:
                        print("ENTER THE CODE NAME OF STATE(TO SEE THE STATE CODE LIST ENTER 'SHOW LIST')")
                        user_state_name = input().upper()
                        if user_state_name == 'SHOW LIST':
                            print(states_list)
                        if user_state_name in states_code:
                            labels = ['ACTIVE', 'RECOVERED', 'DECEASED']
                            size = [con_df[user_state_name].sum() - (rec_df[user_state_name].sum()
                                                                     + dec_df[user_state_name].sum()),
                                    rec_df[user_state_name].sum(), dec_df[user_state_name].sum()]
                            explode = [0.1, 0, 0]
                            plt.pie(size, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False,
                                    colors=['blue', 'green', 'maroon'])
                            plt.title(states_list.loc[user_state_name].to_list()[0])
                            plt.show()
                        elif user_state_name == "EXIT":
                            break
                        else:
                            print("ENTER THE CORRECT OPTION")
                elif graph_option == "EXIT":
                    break
                else:
                    print("ENTER THE CORRECT OPTION")
        elif option == "2":
            while True:
                print("ENTER THE CODE OF NAME OF STATE(TO SEE THE STATE CODE LIST ENTER 'SHOW LIST')")
                user_state_name = input().upper()
                if user_state_name == 'SHOW LIST':
                    print(states_list)
                if user_state_name in states_code:
                    print('''YOU COULD EXPLORE NUMERIC DATA OF''', user_state_name, '''IN THESE WAYS:
                           PARAMETER                       ENTER
                           -----------------------------------------
                           CONFIRMED                       CON
                           ACTIVE                          ACT
                           RECOVERED                       REC
                           DECEASED                        DEC
                           MAXIMUM CONFIRMED CASE          MAX CON
                           MAXIMUM RECOVERED CASE          MAX REC
                           MAXIMUM DECEASED CASE           MAX DEC
                           MINIMUM CONFIRMED CASE          MIN CON
                           MINIMUM RECOVERED CASE          MIN REC
                           MINIMUM DECEASED CASE           MIN DEC
                           AVERAGE CONFIRMED CASE          MEAN CON
                           AVERAGE RECOVERED CASE          MEAN REC
                           AVERAGE DECEASED CASE           MEAN DEC
                           -----------------------------------------''')
                    while True:
                        print("ENTER THE PARAMETER")
                        para_3 = input().upper()
                        if para_3 == "CON":
                            print("TOTAL CONFIRMED CASES OF", states_list.loc[user_state_name].tolist()[0], "IS",
                                  con_df[user_state_name].sum())
                        elif para_3 == "REC":
                            print("TOTAL RECOVERED CASES OF", states_list.loc[user_state_name].to_list()[0], "IS",
                                  rec_df[user_state_name].sum())
                        elif para_3 == "ACT":
                            print("TOTAL ACTIVE CASES OF", states_list.loc[user_state_name].to_list()[0], "IS",
                                  (con_df[user_state_name].sum() - (rec_df[user_state_name].sum()
                                                                    + dec_df[user_state_name].sum())))
                        elif para_3 =="DEC":
                            print("TOTAL DECEASED CASES OF", states_list.loc[user_state_name].to_list()[0], "IS",
                                  dec_df[user_state_name].sum())
                        elif para_3 == "MAX CON":
                            print("MAXIMUM CONFIRMED CASE IN A DAY IN", states_list.loc[user_state_name].to_list()[0],
                                  "IS", con_df[user_state_name].max())
                        elif para_3 == "MAX REC":
                            print("MAXIMUM RECOVERED CASE IN A DAY IN", states_list.loc[user_state_name].to_list()[0],
                                  "IS", rec_df[user_state_name].max())
                        elif para_3 == "MAX DEC":
                            print("MAXIMUM DECEASED CASE IN A DAY IN", states_list.loc[user_state_name].to_list()[0],
                                  "IS", dec_df[user_state_name].max())
                        elif para_3 == "MIN CON":
                            print("MINIMUM CONFIRMED CASE IN A DAY IN", states_list.loc[user_state_name].to_list()[0],
                                  "IS", con_df[user_state_name].min())
                        elif para_3 == "MIN REC":
                            print("MINIMUM RECOVERED CASE IN A DAY IN", states_list.loc[user_state_name].to_list()[0],
                                  "IS", rec_df[user_state_name].min())
                        elif para_3 == "MIN DEC":
                            print("MINIMUM DECEASED CASE IN A DAY IN", states_list.loc[user_state_name].to_list()[0],
                                  "IS", dec_df[user_state_name].min())
                        elif para_3 == "MEAN CON":
                            print("AVERAGE CONFIRMED CASES OF", states_list.loc[user_state_name].to_list()[0], "IS",
                                  con_df[user_state_name].mean())
                        elif para_3 == "MEAN REC":
                            print("AVERAGE RECOVERED CASES OF", states_list.loc[user_state_name].to_list()[0], "IS",
                                  rec_df[user_state_name].mean())
                        elif para_3 == "MEAN DEC":
                            print("AVERAGE DECEASED CASES OF", states_list.loc[user_state_name].to_list()[0], "IS",
                                  dec_df[user_state_name].mean())
                        elif para_3 == "EXIT":
                            break
                        else:
                            print("ENTER THE CORRECT OPTION")
                elif user_state_name == "EXIT":
                    break
                else:
                    print("ENTER THE CORRECT OPTION")
        elif option == "EXIT":
            break
        else:
            print("ENTER THE CORRECT OPTION")
