for i in range(6):
    test_log=open('./acc/test+_acc.csv','a') 
    test_log.write(' {:4d},{:.3f},{:7.3f}\n'
            .format(i, i+1, i*(1+1)))
    test_log.close()