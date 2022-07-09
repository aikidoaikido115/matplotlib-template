import matplotlib.pyplot as plt

# plt.font_manager.fontManager.addfont('thsarabunnew-webfont.ttf')
plt.rc('font', family='TH Sarabun New')


def bar(*args,title,percent):
    plt.title(title,color='orange',fontsize=50)

    plt.xlabel('จังหวัด',color='orange',fontsize=25)
    plt.ylabel('เปอร์เซ็นต์ (%)',color='orange',fontsize=25)

    x = []
    y = percent
    for i in args:
        x.append(i)


    plt.bar(x,y,width=0.42,color='#6de8c3')

    plt.savefig(r'.\bar.jpg')
    # plt.show()
    

if __name__ == '__main__':
    
    bar('กรุงเทพ','ปริมณฑล','อื่นๆ','เชียงใหม่',title='user',percent=[100,50,4,20])