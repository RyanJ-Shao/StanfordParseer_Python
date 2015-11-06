from jpype import *
import os


def senParser(jar_path='',model='',Rfile='',Wfile=''):#jar_path:Jar包所在文件夹,model:句法分析模型路径,Rfile:待句法解析的文件夹,Wfile:句法分析结果写入的文件夹
    jvmpath = getDefaultJVMPath() 
    Jar_path =jar_path+"\\"#JAR包所在文件夹 
    jarpath = os.path.join(os.path.abspath('.'), Jar_path)
    startJVM(jvmpath,"-ea", "-Djava.class.path=%s" % (jarpath + 'SFparser.jar')) #启动JVM
    TA = JPackage('pythonParser').SFparser#初始化类
    jd = TA()#类的实例化""
    a=jd.sentencePar(model,Rfile,Wfile)#参数分别是句法分析模型路径，读取文件夹路径，写入文件夹路径    
    
if __name__=="__main__":
    jar_path='D:\\KeyExtraction\\web\\temp'#jar文件所在的文件夹
    jarmodel='D:\\KeyExtraction\\web\\temp\\parsermodel\\englishPCFG.ser.gz'#斯坦福句法分析的模型
    Rfile='D:\\KeyExtraction\\SD\\sentence_temp'#读取分句文本的路径
    Wfile='D:\\KeyExtraction\\SD\\sentence_parsered'#句法分析后写入文本的路径    
    senParser(jar_path,jarmodel,Rfile,Wfile) 
