class Read_Write_Txt:
    def token_read(self):
        file1=open("/Users/arkapdas/PycharmProjects/REST_API_Final_Project/TestData/token.txt")
        x=file1.read()
        file1.close()
        return x

    def token_write(self,value):
        file1 = open("/Users/arkapdas/PycharmProjects/REST_API_Final_Project/TestData/token.txt", "w")
        file1.write(value)
        file1.close()