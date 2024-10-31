from singleton import Singleton
if __name__=="__main__":
    s1=Singleton()
    s2=Singleton()
    print(s1==s2)