class add:
    def addition(*val1,**val2):
        sum=0
        for i in val1:
            sum=sum+i
        for n in val2.values():
            sum=sum+n

        return sum

