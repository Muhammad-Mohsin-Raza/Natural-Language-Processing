class closet_word:
        
    #--------Edit Distance-----------#
    def editDistance(self,source, target):
#         print(source,target)
        slen = len(source)
        tlen = len(target)

        D = []
        for i in range(slen + 1):
            tmp = []
            for j in range(tlen + 1):
                tmp.append(0)
            D.append(tmp)

        for i in range(1, slen + 1):
            D[i][0] = D[i-1][0] + 1
        for j in range(1, tlen + 1):
            D[0][j] = D[0][j-1] + 1

        for i in range(1, slen + 1):
            for j in range(1, tlen + 1):
                if source[i-1] == target[j-1]:
                    D[i][j] = D[i-1][j-1]
                else:
                    D[i][j] = min(D[i-1][j] + 1,
                    D[i][j-1] + 1,
                    D[i-1][j-1] + 2)
#         display(D)
        return D[-1][-1]
    

    
        
        #-------- Process input string by user-----------#
    def process(self,user_str):
        city_name=['Sahiwal','Lahore','Okara','Peshawar','Karachi','Quetta','Swat','Multan','Islamabad','Mardan']
        index=0
        city_dist={}
        #-------- city_dist contain 
        for n in city_name:
            dis=self.editDistance(user_str,n)
#             print('In loop:',n)
            if dis < len(n):
                city_dist[index]=dis
            index+=1
          
        if len(city_dist)!=0:
            print(city_dist.values())
            closetWord_value=min(city_dist.values())
            index_of_closet_word=list(city_dist.keys())[list(city_dist.values()).index(closetWord_value)]
            print('Closet Word :',city_name[index_of_closet_word])
        else:
            print('No word found ')

