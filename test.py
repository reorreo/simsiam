for i in range(6):
    test_log=open('./acc/test+_acc.csv','a') 
    test_log.write(' {:4d},{top1.avg:.3f},{top5.avg:7.3f}\n'
            .format(i, i+1, i*(1+1)))
    test_log.close()